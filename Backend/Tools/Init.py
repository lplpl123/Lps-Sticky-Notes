import os


def InitLocalFiles():
    if not os.path.exists("./Cache/cache.txt"):
        with open('./Cache/cache.txt', 'w') as f:
            pass
    if not os.path.exists("./Cache"):
        os.mkdir("./Cache")