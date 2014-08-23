#!/usr/bin/env python3
import random
import os

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
            os.system("clear") 
            f.setFont(font = random.choice(f.getFonts()))
            print(color + f.renderText(text))
except KeyboardInterrupt:
    pass
