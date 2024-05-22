# -------------------- IMPORTS -------------------- #
import unittest
import Essentials.converter as converter


# ######################### PASSED ######################### #


# -------------------- METHODS -------------------- #
class TestConverter(unittest.TestCase):
    # ------------ Essentials.converter.hex_to_binary ------------ #
    def test_hex_to_binary_1(self):
        self.assertEqual("1010", converter.hex_to_binary("A"))

    def test_hex_to_binary_2(self):
        self.assertEqual("010010100111111111110000", converter.hex_to_binary("4A7FF0"))

    def test_hex_to_binary_3(self):
        self.assertEqual("0000", converter.hex_to_binary("0"))

    def test_hex_to_binary_4(self):
        self.assertEqual("00000001000000000001", converter.hex_to_binary("01001"))

    # ------------ Essentials.converter.ascii_to_binary ------------ #
    def test_ascii_to_binary_1(self):
        self.assertEqual("010000110101001101010011", converter.ascii_to_binary("CSS"))

    def test_ascii_to_binary_2(self):
        self.assertEqual("00100000", converter.ascii_to_binary(" "))

    def test_ascii_to_binary_3(self):
        self.assertEqual("010000010110100001000001", converter.ascii_to_binary("AhA"))

    def test_ascii_to_binary_4(self):
        self.assertEqual("0010000100111111", converter.ascii_to_binary("!?"))

    # ------------ Essentials.converter.binary_to_hex ------------ #
    def test_binary_to_hex_1(self):
        self.assertEqual("6C", converter.binary_to_hex("01101100"))

    def test_binary_to_hex_2(self):
        self.assertEqual("1B5A229A", converter.binary_to_hex("00011011010110100010001010011010"))

    def test_binary_to_hex_3(self):
        self.assertEqual("58BAB3B15C", converter.binary_to_hex("0101100010111010101100111011000101011100"))

    def test_binary_to_hex_4(self):
        self.assertEqual("0", converter.binary_to_hex("0000"))

    def test_binary_to_hex_5(self):
        self.assertEqual("1", converter.binary_to_hex("1"))

    # ------------ Essentials.converter.hex_to_ascii ------------ #
    def test_hex_to_ascii_1(self):
        self.assertEqual("-E7o", converter.hex_to_ascii("0x2D45376F"))

    def test_hex_to_ascii_2(self):
        self.assertEqual("", converter.hex_to_ascii(""))

    def test_hex_to_ascii_3(self):
        self.assertEqual("UUUU", converter.hex_to_ascii("55555555"))


if __name__ == '__main__':
    unittest.main()
