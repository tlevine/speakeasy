#!/usr/bin/env python3
import pyfiglet
import colorama as c

text = 'Pirate ship'

COLORS = [
    c.Fore.CYAN,
    c.Fore.YELLOW,
    c.Fore.MAGENTA,
    c.Fore.BLACK,
]
try:
    while True:
        for color in COLORS:
            _ = input()
            print(color + text)
except KeyboardInterrupt:
    pass
