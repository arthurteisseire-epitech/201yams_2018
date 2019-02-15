import math


class Op:

    @staticmethod
    def yams(dices, x):
        res = lb(len(dices) - dices.count(x), 5 - dices.count(x))
        print("chances to get a %d yams:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def four(dices, x):
        res = lb(len(dices) - dices.count(x), 4 - dices.count(x))
        print("chances to get a %d four-of-a-kind:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def three(dices, x):
        res = lb(len(dices) - dices.count(x), 3 - dices.count(x))
        print("chances to get a %d three-of-a-kind:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def pair(dices, x):
        res = lb(len(dices) - dices.count(x), 2 - dices.count(x))
        print("chances to get a %d pair:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def straight(dices, x):
        exp_arr = [1 if x == 6 else 6]
        for dice in dices:
            if dice not in exp_arr:
                exp_arr.append(dice)
        res = 1
        for i in range(1, 6 - (len(exp_arr) - 1)):
            res *= i / 6
        return res * 100


def lb(n, k):
    if k > n:
        return 0
    proba_ok = pow(1.0 / 6.0, k)
    proba_ko = pow(5.0 / 6.0, n - k)
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return proba_ok * proba_ko * comb * 100 + lb(n, k + 1)
