import math


class Op:

    @staticmethod
    def yams(dices, x):
        return lb(len(dices), 5 - dices.count(x))

    @staticmethod
    def four(dices, x):
        return lb(len(dices), 4 - dices.count(x))

    @staticmethod
    def three(dices, x):
        return lb(len(dices), 3 - dices.count(x))

    @staticmethod
    def pair(dices, x):
        return lb(len(dices), 2 - dices.count(x))


def lb(n, k):
    if k > n:
        return 0
    proba_ok = pow(1.0 / 6.0, k)
    proba_ko = pow(5.0 / 6.0, n - k)
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return proba_ok * proba_ko * comb * 100 + lb(n, k + 1)
