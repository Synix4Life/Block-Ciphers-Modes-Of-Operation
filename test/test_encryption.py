# -------------------- IMPORTS -------------------- #
import unittest
from encryption_modes import *


# ######################### PASSED ######################### #


# -------------------- METHODS -------------------- #
class TestEncryption(unittest.TestCase):
    # -------------------- ECB -------------------- #
    def test_ECB_1(self):
        self.assertEqual("021212", ecb_encryption("CSS", "A", 8, False, True))

    def test_ECB_2(self):
        self.assertEqual("02086A2D2F143E046B", ecb_encryption("Hi Leute!", "Ja", 2))

    def test_ECB_ERROR_1(self):
        self.assertRaises(AttributeError, lambda: ecb_encryption("Sometext", "key", 4, True))

    def test_ECB_ERROR_2(self):
        self.assertRaises(ValueError, lambda: ecb_encryption("HERE WE GOOOO", "key", 25, False, True))

    # -------------------- CBC -------------------- #
    def test_CBC_1(self):
        self.assertEqual("0C0607", cbc_encryption("TRY", "X", 0, 1))

    # -------------------- CTR -------------------- #
    def test_CTR_1(self):
        self.assertEqual("1E2C3B3B", ctr_encryption("Test", "K", 0, 1))


if __name__ == '__main__':
    unittest.main()
