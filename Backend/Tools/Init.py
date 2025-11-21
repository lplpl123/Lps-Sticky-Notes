import os
import random
from Backend.Config.Colors import COLORS


def InitLocalFiles():
    if not os.path.exists("./Cache/cache.txt"):
        with open('./Cache/cache.txt', 'w') as f:
            pass
    if not os.path.exists("./Cache"):
        os.mkdir("./Cache")


def InitColors():
    colors = COLORS
    keysList = list(colors.keys())
    maxIndex = len(keysList)
    countIndex = random.randint(0, maxIndex - 1)
    showIndex = random.randint(0, 1)

    colorFront = colors[keysList[countIndex]][showIndex]
    colorBack = colors[keysList[countIndex]][1 - showIndex]

    return colorFront, colorBack