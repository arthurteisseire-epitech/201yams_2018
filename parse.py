import argparse
from proba import *


def dice_range(dice):
    dice = int(dice)
    if dice < 0 or dice > 6:
        raise argparse.ArgumentTypeError("Dices must be between 1 and 6 included")
    return dice


class Parser:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("d1", type=dice_range, help="value of the first die (0 if not thrown)")
        parser.add_argument("d2", type=dice_range, help="value of the second die (0 if not thrown)")
        parser.add_argument("d3", type=dice_range, help="value of the third die (0 if not thrown)")
        parser.add_argument("d4", type=dice_range, help="value of the fourth die (0 if not thrown)")
        parser.add_argument("d5", type=dice_range, help="value of the fifth die (0 if not thrown)")
        parser.add_argument("c", type=str, help="expected combination")
        args = parser.parse_args()
        return args

    @staticmethod
    def exec_func():
        args = Parser.parse_args()
        dices = [args.d1, args.d2, args.d3, args.d4, args.d5]

        if dices.count(0) == 5 or dices.count(0) == 0:
            array = str(args.c).split("_")
            func_name = array[0]
            exec("Op." + func_name + "(dices," + ",".join(array[1:]) + ")")
        else:
            print("All dices must be 0 or none of it")
            exit(84)
