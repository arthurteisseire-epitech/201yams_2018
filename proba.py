import numpy as np
import math


class Op:

    @staticmethod
    def yams(dices, x):
        return lb(len(dices), 5)


def lb(n, k):
    proba_ok = pow(1.0 / 6.0, k)
    proba_ko = pow(5.0 / 6.0, n - k)
    comb = math.factorial(n) / math.factorial(k) * math.factorial(n - k)
    return round(proba_ok * proba_ko * comb * 100, 2)

