from unittest import TestCase
from proba import Op


class TestOp(TestCase):
    def test_pair(self):
        self.assertEqual(Op.yams([0, 0, 0, 0, 0], 4), 0.01)

    def test_four(self):
        self.assertEqual(Op.four([0, 0, 0, 0, 0], 4), 1.86)
