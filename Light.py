# -*- coding: utf-8-*-
import random
import re
from client import jasperpath

WORDS = ["LIGHT", "LIGHTS", "ON", "OFF"]


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
        mic.say('Turning lights on.')
    elif isOff(text):
        mic.say('Turning lights off.')
    else:
        mic.say('Toggling lights.')

    mic.say(text)


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
