import argparse
from proba import *


class Parser:

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("d1", type=int, help="value of the first die (0 if not thrown)")
        parser.add_argument("d2", type=int, help="value of the second die (0 if not thrown)")
        parser.add_argument("d3", type=int, help="value of the third die (0 if not thrown)")
        parser.add_argument("d4", type=int, help="value of the fourth die (0 if not thrown)")
        parser.add_argument("d5", type=int, help="value of the fifth die (0 if not thrown)")
        parser.add_argument("c", type=str, help="expected combination")
        args = parser.parse_args()
        return args

    @staticmethod
    def exec_func():
        args = Parser.parse_args()
        dices = [args.d1, args.d2, args.d3, args.d4, args.d5]

        array = str(args.c).split("_")
        func_name = array[0]
        exec("Op." + func_name + "(dices," + ",".join(array[1:]) + ")")
