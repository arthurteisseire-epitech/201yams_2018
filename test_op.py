from unittest import TestCase
from proba import Op


class TestOp(TestCase):
    def test_yams(self):
        self.assertEqual(round(Op.yams([0, 0, 0, 0, 0], 4), 2), 0.01)

    def test_four(self):
        self.assertEqual(round(Op.four([0, 0, 0, 0, 0], 4), 2), 0.33)
        self.assertEqual(round(Op.four([1, 2, 3, 4, 5], 4), 2), 1.62)

    def test_three(self):
        self.assertEqual(round(Op.three([0, 0, 0, 0, 0], 4), 2), 3.55)

    def test_pair(self):
        self.assertEqual(round(Op.pair([0, 0, 0, 0, 0], 4), 2), 19.62)

    def test_straight(self):
        self.assertEqual(round(Op.straight([2, 2, 5, 4, 6], 6), 2), 16.67)

    def test_full(self):
        self.assertEqual(round(Op.full([0, 0, 0, 0, 0], 2, 3), 2), 0.13)
        self.assertEqual(round(Op.full([2, 3, 2, 3, 2], 2, 3), 2), 100.00)
