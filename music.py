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
f = pyfiglet.Figlet()
try:
    while True:
        for color in COLORS:
            _ = input()
            print(color + f.renderText(text))
except KeyboardInterrupt:
    pass
