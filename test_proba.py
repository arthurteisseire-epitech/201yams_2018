import unittest
from proba import get_proba


class TestGetProba(unittest.TestCase):

    def test_get_element(self):
        dices = {1, 2, 3, 4, 5, 6}
        element = get_proba(dices, "pair")

        self.assertEqual(element, 'pair')

    def run(self):
        unittest.main()
