# phazer.py
"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Uses 16 LED's and speaker.
Plays phazer fire and random lights in loop.
2021-12-18
Larry T. Priest priestlt at protonmail dot com
"""
import board
import audiocore
import audiomp3
import audiopwmio
import time
from RandomLed import RandomLed
import random


def PhazerFire():
    ASSETS = 'assets/'
    WORKING_MSG = ASSETS + "tos-photon-torpedo-1.wav"
    audio = audiopwmio.PWMAudioOut(board.GP27_A1)
    with open(WORKING_MSG, "rb") as data:
        wav = audiocore.WaveFile(data)
        audio.play(wav)
        while audio.playing:
            tcount = random.randint(0, 0xffff)
            RandomLed.rdisplay(count=tcount)
        audio.stop()
        audio.deinit()


if __name__ == '__main__':
    RandomLed()
    while True:
        PhazerFire()
        RandomLed.RandomLedClose()
    RandomLed.__exit__()
