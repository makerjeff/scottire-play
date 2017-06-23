#!/usr/local/bin/python

import time
import datetime
from bcolors import bcolors

prefix = '\033['
suffix = 'm'

def millis():
    return int(round(time.time() * 1000))

def print_colors_sleep():
    for i in range(0, 255):
        print prefix + str(i) + suffix + 'color %d' % i + '\033[0m'
        time.sleep(0.05)
        print millis()

def print_colors_no_sleep():



def Main():
    print_colors_sleep()


if __name__ == '__main__':
    Main()