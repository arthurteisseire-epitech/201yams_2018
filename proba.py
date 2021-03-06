import math


class Op:

    @staticmethod
    def yams(dices, x):
        res = lb(len(dices) - dices.count(x), 5 - dices.count(x))
        print("chances to get a %d yams:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def four(dices, x):
        res = lb(len(dices) - min(dices.count(x), 4), 4 - min(dices.count(x), 4))
        print("chances to get a %d four-of-a-kind:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def three(dices, x):
        res = lb(len(dices) - min(dices.count(x), 3), 3 - min(dices.count(x), 3))
        print("chances to get a %d three-of-a-kind:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def pair(dices, x):
        res = lb(len(dices) - min(dices.count(x), 2), 2 - min(dices.count(x), 2))
        print("chances to get a %d pair:  %.2f%%" % (x, res))
        return res

    @staticmethod
    def full(dices, n1, n2):
        if n1 == n2:
            exit(84)
        n = len(dices) - min(dices.count(n1), 3) - min(dices.count(n2), 2)
        k = 3 - min(dices.count(n1), 3)
        comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        res = pow(1 / 6, n) * comb * 100
        print("chances to get a %d full of %d:  %.2f%%" % (n1, n2, res))
        return res

    @staticmethod
    def straight(dices, x):
        if x != 5 and x != 6:
            exit(84)
        exp_arr = [1 if x == 6 else 6]
        for dice in dices:
            if dice not in exp_arr:
                exp_arr.append(dice)
        res = 1
        for i in range(1, 6 - (len(exp_arr) - 1)):
            res *= i / 6
        res *= 100
        print("chances to get a %d straight:  %.2f%%" % (x, res))
        return res


def lb(n, k):
    if k > n:
        return 0
    proba_ok = pow(1.0 / 6.0, k)
    proba_ko = pow(5.0 / 6.0, n - k)
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return proba_ok * proba_ko * comb * 100 + lb(n, k + 1)
