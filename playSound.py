# playSound.py
'''

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
    for i in range(count):
        tcount = randint(0, 0xffff)
        RandomLed.rdisplay(count=tcount)
        await asyncio.sleep(interval)

async def main():                          # Don't forget the async!
    led_task = asyncio.create_task(blink(board.GP20, 0.25, 5))
    led_task2 = asyncio.create_task(blink(board.GP18, 0.20, 6))
    led_task3 = asyncio.create_task(blink(board.GP19, 0.18, 4))
    randomblink_task = asyncio.create_task(randomblink(0.25, 6))
    await asyncio.gather(led_task, led_task2, led_task3, randomblink_task)         # Don't forget the await!
    
def PlaySound(SoundNum):
    SoundList= ['Scotty_ayesir.wav',
                'Scotty_upurshaft.wav',
                'tos-computer-working.wav',
                'tos-intercom.wav',
                'tos-photon-torpedo-1.wav']
    ASSETS = 'assets/'

    current_message = ASSETS + SoundList[SoundNum]
    audio = audiopwmio.PWMAudioOut(board.GP27_A1)
    with open(current_message, "rb") as data:
        wav = audiocore.WaveFile(data)
        audio.play(wav)
        asyncio.run(main())
        tcount = randint(0, 0xffff)
        RandomLed.rdisplay(count=tcount)
        while audio.playing:
            pass
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
