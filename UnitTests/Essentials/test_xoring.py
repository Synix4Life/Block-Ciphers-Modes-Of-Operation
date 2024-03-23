import unittest
from Essentials.xoring import xor


# ------------------------- PASSED -------------------------#


class TestXOR(unittest.TestCase):
    def test_xor_1(self):
        self.assertEqual("", xor("", ""))

    def test_xor_2(self):
        self.assertEqual("11000110", xor("10001011", "01001101"))

    def test_xor_3(self):
        self.assertRaises(ValueError, lambda: xor("0101", ""))

    def test_xor_4(self):
        self.assertEqual("11", xor("01", "1011010"))


if __name__ == '__main__':
    unittest.main()
