# buttonSelect.py
"""
CircuitPython
2021-12-18
Larry T. Priest priestlt at protonmail dot com
Button example for Pico. Prints button pressed state to serial consloe
REQUIRED HARDWARE:
* Button switch on pin GP13 ( I use GP20)
Adafruit Learn Guide:
Getting Started with Raspberry Pi Pico and CircuitPython
By Kattni Rembor
"""
import board
import time
import digitalio
from RandomLed import RandomLed
import phazer
from playSound import PlaySound
import random
# amber = 0
# red = 1
# green = 2
class ButtonSelect():
    buttons = []
    buttonpins = [19, 20, 21, 22]  # buttons 1 thru 4

    pressed = False
    def __init__(self):
        subcommand = 'ButtonSelect.buttons.append(digitalio.DigitalInOut(board.GP'
        for pin in range(len(ButtonSelect.buttonpins)):
            fullcommand = subcommand + str(ButtonSelect.buttonpins[pin]) + '))'
            exec(fullcommand)
            ButtonSelect.buttons[pin].direction = digitalio.Direction.OUTPUT


    def SelectButton():
        if ButtonSelect.buttons[0].value:
            print("You pressed the #1 button!")
            PlaySound(0)

        elif ButtonSelect.buttons[1].value:
            print("You pressed the #2 button!")
            PlaySound(1)

        elif ButtonSelect.buttons[2].value:
            print("You pressed the #3 button!")
            PlaySound(2)

        elif ButtonSelect.buttons[3].value:
            print("You pressed the #4 button!")
            PlaySound(3)

        else:
            tcount = random.randint(0, 0xffff)
            RandomLed.rdisplay(count=tcount)

if __name__ == '__main__':
    RandomLed()
    ButtonSelect()
    while True:
        tcount = random.randint(0, 0xffff)
        RandomLed.rdisplay(count=tcount)
        ButtonSelect.SelectButton()
