from unittest import TestCase
from proba import Op


class TestOp(TestCase):
    def test_yams(self):
        self.assertEqual(round(Op.yams([0, 0, 0, 0, 0], 4), 2), 0.01)
        # self.assertEqual(Op.yams([4, 1, 1, 1, 1], 4), Op.four([0, 0, 0, 0, 0], 4))

    def test_four(self):
        self.assertEqual(round(Op.four([0, 0, 0, 0, 0], 4), 2), 0.33)

    def test_three(self):
        self.assertEqual(round(Op.three([0, 0, 0, 0, 0], 4), 2), 3.55)

    def test_pair(self):
        self.assertEqual(round(Op.pair([0, 0, 0, 0, 0], 4), 2), 19.62)
