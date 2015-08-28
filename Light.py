# -*- coding: utf-8-*-
import os
import re
import subprocess
import lifx
import time
import yaml

WORDS = ["LIGHT", "LIGHTS", "ON", "OFF", "OF", "ENABLE", "DISABLE", "TOGGLE"]

home = os.getenv("HOME")
config_path = home + "/.lifx-jasper/config.yml"
f = open(config_path, 'r')
config = yaml.load(f)
f.close()


def handle(text, mic, profile):
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


def isValid(text):
    """
        Returns True if the input is related to lights.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\blight\b', text, re.IGNORECASE))


def isOn(text):
    return bool(re.search(r'\b(on|enable)\b', text, re.IGNORECASE))


def isOff(text):
    return bool(re.search(r'\b(off|disable|of)\b', text, re.IGNORECASE))


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
