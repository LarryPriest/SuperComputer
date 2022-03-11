# code.py
"""
CircuitPython
2021.12.04 Larry T. Priest  priestlt@protonmail.com
Main program for Super Computer interface.
"""

import sys
from RandomLed import RandomLed
from playSound import PlaySound
from buttonSelect import ButtonSelect


if __name__ == '__main__':
    RandomLed()
    PlaySound(4)
    PlaySound(2)

    ButtonSelect()
    while True:
        ButtonSelect.SelectButton()

    RandomLed.RandomLedClose()
    sys.exit()
