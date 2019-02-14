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
            print("for full dices values mustn't be the sames")
            exit(84)
        print("full:")
        print(dices, x, y)


    def get_proba(self):
        print("proba")

