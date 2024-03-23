import unittest

from Essentials.iv_actions import *


# ------------------------- PASSED -------------------------#


class TestIV(unittest.TestCase):
    # ------------ Essentials.iv_actions.extend_iv_by_one ------------ #
    def test_extend_iv_1(self):
        self.assertEqual("10011111", extend_iv(159, 8))

    def test_extend_iv_2(self):
        self.assertEqual("00000100", extend_iv(4))

    def test_extend_iv_3(self):
        self.assertEqual("00000000000000000000000000000000", extend_iv(0, 32))

    def test_extend_iv_4(self):
        self.assertEqual("0000000000000000000000000000000000000000000000000000000000000001", extend_iv(1, 64))

    # ------------ Essentials.iv_actions.increment_iv ------------ #
    def test_increment_iv_1(self):
        self.assertEqual("011010", increment_iv("011001"))

    def test_increment_iv_2(self):
        self.assertEqual("001", increment_iv("000"))

    def test_increment_iv_3(self):
        self.assertEqual("10101010", increment_iv("10101001"))

    def test_increment_iv_4(self):
        self.assertRaises(OverflowError, lambda: increment_iv("11111111"))


if __name__ == '__main__':
    unittest.main()
