class Op:

    @staticmethod
    def pair(dices, x):
        print("pair:")
        print(dices, x)

    @staticmethod
    def full(dices, x, y):
        if x == y:
            print("for full dices values mustn't be the sames")
            exit(84)
        print("full:")
        print(dices, x, y)

