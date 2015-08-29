# -*- coding: utf-8-*-
import os
import re
import subprocess
import lifx
import time
import yaml

WORDS = ["LIGHT", "LIGHTS", "ON", "OFF", "OF", "ENABLE", "DISABLE", "TOGGLE", "PRESET", "ALPHA", "BRAVO", "CHARLIE",
         "DELTA", "ECHO"]

home = os.getenv("HOME")
config_path = home + "/.lifx-jasper/config.yml"
f = open(config_path, 'r')
config = yaml.load(f)
f.close()


def handle(text, mic):
    """
        Responds to user-input, typically speech text, by turning a light on/off

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    if isOn(text):
        print 'Turning lights on.'
        if config['force-cloud']:
            sendCloud('on', mic)
        else:
            lights = lifx.Client()
            time.sleep(1)
            devices = lights.get_devices()
            if len(devices) > 0:
                power(devices, 'on')
            elif config['cloud-fallback']:
                print 'Falling back to cloud.'
                sendCloud('power on', mic)
            else:
                mic.say("No devices found. Please try again.")

    elif isOff(text):
        print 'Turning lights off.'
        if config['force-cloud']:
            sendCloud('off', mic)
        else:
            lights = lifx.Client()
            time.sleep(1)
            devices = lights.get_devices()
            if len(devices) > 0:
                time.sleep(1)
                power(devices, 'off')
            elif config['cloud-fallback']:
                print 'Falling back to cloud.'
                sendCloud('power off', mic)
            else:
                mic.say("No devices found. Please try again.")

    elif isPreset(text):
        preset = getPreset(text)
        if not preset:
            mic.say("The preset you stated is invalid. Please try again.")
        else:
            print 'Setting preset.'
            colors = config['presets'][preset]

            lights = lifx.Client()
            time.sleep(1)
            devices = lights.get_devices()
            if len(devices) > 0:
                color = lifx.color.HSBK(colors['hue'], colors['saturation'], colors['brightness'], colors['kelvin'])
                setPreset(devices, color)
            # lifx-cli does not work with this; investigating
            # elif config['cloud-fallback']:
            #     print 'Falling back to cloud.'
            #     sendCloud(
            #         'color -h {} -s {} -b {} -k {}'.format(colors['hue'], colors['saturation'], colors['brightness'],
            #                                                colors['kelvin']), mic)
            else:
                mic.say("No devices found. Please try again.")

    else:
        print 'Toggling lights.'
        if config['force-cloud']:
            sendCloud('toggle', mic)
        else:
            lights = lifx.Client()
            time.sleep(1)
            devices = lights.get_devices()
            if len(devices) > 0:
                time.sleep(1)
                toggle(devices)
            elif config['cloud-fallback']:
                print 'Falling back to cloud.'
                sendCloud('toggle', mic)
            else:
                mic.say("No devices found. Please try again.")


def isValid(text):
    """
        Returns True if the input is related to lights.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(light|lights)\b', text, re.IGNORECASE))


def isOn(text):
    return bool(re.search(r'\b(on|enable)\b', text, re.IGNORECASE))


def isOff(text):
    return bool(re.search(r'\b(off|disable|of)\b', text, re.IGNORECASE))


def isPreset(text):
    return bool(re.search(r'\bpreset\b', text, re.IGNORECASE))


def getPreset(text):
    if bool(re.search(r'\b(alpha)\b', text, re.IGNORECASE)):
        return 'alpha'
    elif bool(re.search(r'\b(bravo)\b', text, re.IGNORECASE)):
        return 'bravo'
    elif bool(re.search(r'\b(charlie)\b', text, re.IGNORECASE)):
        return 'charlie'
    elif bool(re.search(r'\b(delta)\b', text, re.IGNORECASE)):
        return 'delta'
    elif bool(re.search(r'\b(echo)\b', text, re.IGNORECASE)):
        return 'echo'
    else:
        return False


def sendCloud(parameter, mic):
    return_code = subprocess.call(config['lifx-cli-path'] + " " + parameter, shell=True)

    if return_code != 0:
        mic.say("An error occurred while accessing your lights. Please try again.")


def power(devices, state='off'):
    for l in devices:
        print 'Turning %s %s' % (state, l.label)
        if state == 'on':
            l.power = True
        elif state == 'off':
            l.power = False


def toggle(devices):
    for l in devices:
        print 'Toggling %s' % l.label
        l.power_toggle()


def setPreset(devices, color):
    for l in devices:
        if not l.power:
            l.color = color
            l.fade_power(True)
        else:
            l.fade_color(color)
