# -------------------- IMPORTS -------------------- #
import unittest
from Essentials.miscellaneous import *


# ######################### PASSED ######################### #


# -------------------- METHODS -------------------- #
class TestMiscellaneous(unittest.TestCase):
    # ------------ Essentials.miscellaneous.leading_zeros ------------ #
    def test_leading_zeros_1(self):
        self.assertEqual("00", leading_zeros(["00000000", "11111111"]))

    def test_leading_zeros_2(self):
        self.assertEqual("", leading_zeros(["01000000", "11111111"]))

    def test_leading_zeros_3(self):
        self.assertEqual("", leading_zeros([""]))

    def test_leading_zeros_4(self):
        self.assertEqual("00000", leading_zeros(["00000000", "00000000", "00000100"]))

    def test_leading_zeros_edge_1(self):
        self.assertEqual("0", leading_zeros(["00001000"]))

    def test_leading_zeros_edge_2(self):
        self.assertEqual("", leading_zeros(["00010000"]))

    # ------------ Essentials.miscellaneous.divide ------------ #
    def test_divide_1(self):
        self.assertEqual(["11", "01", "1"], divide("11011", 2))

    def test_divide_2(self):
        self.assertEqual(["011011010", "110100111", "1011"], divide("0110110101101001111011", 9))

    def test_divide_3(self):
        self.assertEqual(["0"], divide("0", 10))

    def test_divide_4(self):
        self.assertEqual(["1", "0", "1", "0", "1", "0", "1"], divide("1010101", 1))

    def test_divide_5(self):
        self.assertEqual(["1111"], divide("1111", 9))

    def test_divide_edge(self):
        self.assertEqual([], divide("", 5))


if __name__ == '__main__':
    unittest.main()
