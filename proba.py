class Op:

    @staticmethod
    def pair(dices, x):
        print("pair:")
        print(dices, x)
        for dice in dices:
            print(dice)
        return "pair"

    @staticmethod
    def full(dices, x, y):
        if x == y:
            print("Full dices values mustn't be the sames")
            exit(84)
        print("full:")
        print(dices, x, y)

    @staticmethod
    def straight(dices, x):
        if x < 5:
            print("Straight expected combination must be 5 or 6")
            exit(84)
        print("straight:")
        print(dices, x)

    @staticmethod
    def yams(dices, x):
        return round(pow(1 / 6, 5) * 100, 2)
