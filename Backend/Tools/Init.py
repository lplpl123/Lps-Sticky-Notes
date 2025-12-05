import os
import json
import random
from Backend.Config.Colors import COLORS


def InitColors():
    try:
        with open("./Backend/Config/Theme.json", 'r') as f:
            out = json.load(f)
            print("out", out)
            return tuple(out["frontColor"]), tuple(out["backColor"])
    except:
        colors = COLORS
        keysList = list(colors.keys())
        maxIndex = len(keysList)
        countIndex = random.randint(0, maxIndex - 1)
        showIndex = random.randint(0, 1)

        colorFront = colors[keysList[countIndex]][showIndex]
        colorBack = colors[keysList[countIndex]][1 - showIndex]
        print(colorFront, colorBack)

        return colorFront, colorBack