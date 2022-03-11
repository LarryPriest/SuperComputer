# playSound.py
'''
CircuitPython
2021-12-18
Larry T. Priest priestlt at protonmail dot com
play a sound from the assets folder
'''
import board
import audiocore
import audiomp3
import audiopwmio
import time
import asyncio
import digitalio
from random  import randint
from RandomLed import RandomLed

async def blink(pin, interval, count):     # Don't forget the async!
    with digitalio.DigitalInOut(pin) as led:
        led.switch_to_output(value=False)
        for i in range(count):
            led.value = True
            await asyncio.sleep(interval)  # Don't forget the await!
            led.value = False
            await asyncio.sleep(interval)  # Don't forget the await!
    led.deinit()

async def randomblink(interval, count):
    # print('randomblink')
    for i in range(count):
        tcount = randint(0, 0xffff)
        RandomLed.rdisplay(count=tcount)
        await asyncio.sleep(interval)  # do this loop then sleep this time??

async def main(soundTime):     # Don't forget the async!
    # print('main async')
    led_task = asyncio.create_task(blink(board.GP16, soundTime/30, 5))
    led_task2 = asyncio.create_task(blink(board.GP17, soundTime/30, 6))
    led_task3 = asyncio.create_task(blink(board.GP18, soundTime/30, 4))
    randomblink_task = asyncio.create_task(randomblink(soundTime/100, 6))
    await asyncio.gather(led_task, led_task2, led_task3, randomblink_task)         # Don't forget the await!

def PlaySound(SoundNum):
    SoundList= [{'Scotty_ayesir.wav':0.44},
                {'Scotty_upurshaft.wav':1.28},
                {'tos-computer-working.wav':0.64},
                {'tos-intercom.wav':1.36},
                {'tos-photon-torpedo-1.wav':1.5}]
    ASSETS = 'assets/'
    for s in SoundList[SoundNum]:
        soundFileName = s
        soundFileTime = SoundList[SoundNum][s]
    current_message = ASSETS + soundFileName
    audio = audiopwmio.PWMAudioOut(board.GP27_A1)
    with open(current_message, "rb") as data:
        wav = audiocore.WaveFile(data)
        audio.play(wav)
        asyncio.run(main(soundFileTime))
        tcount = randint(0, 0xffff)
        RandomLed.rdisplay(count=tcount)
        while audio.playing:
            # pass
            tcount = randint(0, 0xffff)
            RandomLed.rdisplay(count=tcount)
        audio.stop()
        audio.deinit()

if __name__ == '__main__':
    RandomLed()
    SoundNum = randint(0, 4)
    print(SoundNum)
    PlaySound(SoundNum)
    RandomLed.__exit__()
