#!/usr/bin/env python3
import random
import os

import pyfiglet
import colorama as c

texts = [
]

COLORS = [
    c.Fore.WHITE,
    c.Fore.CYAN,
    c.Fore.YELLOW,
    c.Fore.MAGENTA,
]
f = pyfiglet.Figlet()

try:
    while True:
        for color in COLORS:
            _ = input()
            os.system("clear") 
            f.setFont(font = random.choice(f.getFonts()))
            print(color + f.renderText(random.choice(texts)))
except KeyboardInterrupt:
    pass
