from unittest import TestCase
from proba import Op


class TestOp(TestCase):
    def test_yams(self):
        self.assertEqual(Op.yams([0, 0, 0, 0, 0], 4), 0.01)
        # self.assertEqual(Op.yams([4, 1, 1, 1, 1], 4), Op.four([0, 0, 0, 0, 0], 4))

    def test_four(self):
        self.assertEqual(Op.four([0, 0, 0, 0, 0], 4), 0.33)

    def test_three(self):
        self.assertEqual(Op.three([0, 0, 0, 0, 0], 4), 3.55)

    # def test_pair(self):
    #     self.assertEqual(Op.pair([0, 0, 0, 0, 0], 4), 19.62)
