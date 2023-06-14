import unittest
from kod.main import Calculator


class Test(unittest.TestCase):

    def setUp(self):
        self.calculation = Calculator(8, 3)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 11, 'The sum is wrong')

    def test_sub(self):
        self.assertEqual(self.calculation.get_sub(), 5, 'The sub is wrong')

    def test_div(self):
        self.assertEqual(self.calculation.get_div(), 2.67, 'The div is wrong')

    def test_multi(self):
        self.assertEqual(self.calculation.get_multi(), 24, 'The multi is wrong')

    def test_expo(self):
        self.assertEqual(self.calculation.get_expo(), 512, 'The expo is wrong')

    def test_rootext(self):
        self.assertEqual(self.calculation.get_root_ext(), 2, 'The root ext is wrong')



if __name__ == '__main__':
    unittest.main()