from unittest import TestCase
from proba import Op


class TestOneHundred(TestCase):
    def test_yams(self):
        self.assertEqual(100.00, round(Op.yams([4, 4, 4, 4, 4], 4), 2))

    def test_four(self):
        self.assertEqual(100.00, round(Op.four([4, 4, 4, 4, 2], 4), 2))

    def test_three(self):
        self.assertEqual(100.00, round(Op.three([4, 4, 4, 2, 2], 4), 2))

    def test_pair(self):
        self.assertEqual(100.00, round(Op.pair([4, 4, 2, 2, 2], 4), 2))

    def test_straight(self):
        self.assertEqual(100.00, round(Op.straight([1, 2, 3, 4, 5], 5), 2))

    def test_full(self):
        self.assertEqual(100.00, round(Op.full([4, 4, 4, 2, 2], 4, 2), 2))


class TestSpecialCases(TestCase):
    def test_full(self):
        self.assertEqual(16.67, round(Op.full([4, 4, 2, 2, 2], 4, 2), 2))


class TestOp(TestCase):
    def test_yams(self):
        self.assertEqual(0.01, round(Op.yams([0, 0, 0, 0, 0], 4), 2))

    def test_four(self):
        self.assertEqual(0.33, round(Op.four([0, 0, 0, 0, 0], 4), 2))
        self.assertEqual(1.62, round(Op.four([1, 2, 3, 4, 5], 4), 2))

    def test_three(self):
        self.assertEqual(3.55, round(Op.three([0, 0, 0, 0, 0], 4), 2))

    def test_pair(self):
        self.assertEqual(19.62, round(Op.pair([0, 0, 0, 0, 0], 4), 2))

    def test_straight(self):
        self.assertEqual(16.67, round(Op.straight([2, 2, 5, 4, 6], 6), 2))

    def test_full(self):
        self.assertEqual(0.13, round(Op.full([0, 0, 0, 0, 0], 2, 3), 2))
