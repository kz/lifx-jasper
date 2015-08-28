# -*- coding: utf-8-*-
import os
import re
import subprocess
import lifx
import time

WORDS = ["LIGHT", "LIGHTS", "ON", "OFF"]

home = os.getenv("HOME")
config_path = home + "/.config/lifx-jasper/lifx-cli-path"
f = open(config_path, 'r')
lifx_cli_path = f.readline().rstrip()
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

    lights = lifx.Client()
    time.sleep(1)

    if isOn(text):
        print 'Turning lights on.'
        # return_code = subprocess.call(lifx_cli_path + " on", shell=True)
        for l in lights.get_devices():
            print 'Turning on %s' % l.label
            l.power = True
    elif isOff(text):
        print 'Turning lights off.'
        return_code = subprocess.call(lifx_cli_path + " off", shell=True)
        for l in lights.get_devices():
            print 'Turning off %s' % l.label
            l.power = False
    else:
        print 'Toggling lights.'
        for l in lights.get_devices():
            print 'Toggling %s' % l.label
            l.toggle()
        # return_code = subprocess.call(lifx_cli_path + " toggle", shell=True)

    # if return_code != 0:
    #     mic.say("Error. Try again.")


def isValid(text):
    """
        Returns True if the input is related to lights.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\blight\b', text, re.IGNORECASE))


def isOn(text):
    return bool(re.search(r'\bon\b', text, re.IGNORECASE))


def isOff(text):
    return bool(re.search(r'\boff\b', text, re.IGNORECASE))