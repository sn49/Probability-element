import random


def dorein(level):
    sucnum = 3
    desnum = 1
    resetnum = 1.2

    destroy = 0
    reset = 0

    success = 80 - sucnum * (level - 1)

    if level >= 2:
        destroy = 10 - desnum * (level - 2)
        if level >= 3:
            reset = reset = 15 - resetnum * (level - 3)

        if destroy < 0:
            destroy = 0
        if reset < 0:
            reset = 0
    fail = 100 - reset - destroy - success

    result = random.random() * 100

    if result < success:
        return 1
    elif result < success + fail:
        return 0
    elif result < success + fail + reset:
        return -5
    else:
        return -10


level = 1
maxlevel = 20

while level != maxlevel:
    result = dorein(level)

    if result == 1:
        level += 1
    elif result == -5:
        level = 1
    elif result == -10:
        break

    print(level)