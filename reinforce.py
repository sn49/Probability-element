class rein:
    def __init__(self, level):
        self.level = level

    def dorein(self):
        sucnum = 2.77
        failnum = 1.53
        desnum = 0.56

        level = self.level

        success = 100 - sucnum * level
        fail = failnum * (level - 1)
        destroy = desnum * (level - 1)