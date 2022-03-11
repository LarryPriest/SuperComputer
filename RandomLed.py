# RandomLed.py
'''
2021.21.35 Larry T. Priest  priestlt@protonmail.com
random LED display a st of binary numbers
august 28, 2021
16 LED's on pins GPIO0 - GPIO15
'''
import board
import digitalio
import time
import random


class RandomLed():
    '''Random LED generator'''
    # delay = 0.15  # seconds
    count = 0xffff  # any interger (hex 'cause it makes sense)
    LEDbits = []
    TOTALBITS = 16

    def __init__(self, delay=0.15, bits=16):
        '''Requires # of bits'''
        RandomLed.TOTALBITS = bits
        RandomLed.delay = delay
        subcommand = 'RandomLed.LEDbits.append(digitalio.DigitalInOut(board.GP'
        for i in range(RandomLed.TOTALBITS):
            fullcommand = subcommand + str(i) + '))'
            exec(fullcommand)
            RandomLed.LEDbits[i].direction = digitalio.Direction.OUTPUT

    def ByteList(count):
        # Takes an integer and creates a list of 'bits' representing LEDs
        counterBits = bin(count)[2:]  # leading zero + b chopped
        while len(counterBits) < 16:
            counterBits = '0' + counterBits
        byte_list = []
        for bit in iter(counterBits):
            byte_list.append(bit)
        return byte_list

    def rdisplay(count=0x0ffff):
        '''Requires max interger'''
        count = count
        byte_list = RandomLed.ByteList(count)
        if count < 256:
            byte_list = byte_list[8:]
        bit_count = 0
        for i in iter(byte_list):
            if i == '1':
                RandomLed.LEDbits[bit_count].value = True
            else:
                RandomLed.LEDbits[bit_count].value = False
            bit_count += 1
        time.sleep(RandomLed.delay)

    def RandomLedClose():
        for i in range(len(RandomLed.LEDbits)):
            RandomLed.LEDbits[i].value = False

    def __exit__():
        for i in range(len(RandomLed.LEDbits)):
            RandomLed.LEDbits[i].value = False
        for i in range(len(RandomLed.LEDbits)):
            print('Closing output GP', i)
            RandomLed.LEDbits[i].deinit()


if __name__ == '__main__':
    RandomLed(delay=0.15, bits=16)
    while True:
        tcount = random.randint(0, 0xffff)
        RandomLed.rdisplay(count=tcount)
    RandomLed.__exit__()
