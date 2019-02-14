import numpy as np
import math

_round = 2


class Op:

    @staticmethod
    def yams(dices, x):
        return lb(len(dices), 5)

    @staticmethod
    def four(dices, x):
        return lb(len(dices), 4) + Op.yams(dices, x)

    @staticmethod
    def three(dices, x):
        return lb(len(dices), 3) + Op.four(dices, x)

    @staticmethod
    def pair(dices, x):
        return lb(len(dices), 2) + Op.three(dices, x)


def lb(n, k):
    proba_ok = pow(1.0 / 6.0, k)
    proba_ko = pow(5.0 / 6.0, n - k)
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return proba_ok * proba_ko * comb * 100
