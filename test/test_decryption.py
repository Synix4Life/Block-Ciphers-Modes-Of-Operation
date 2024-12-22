# -------------------- IMPORTS -------------------- #
import unittest
from decryption_modes import *
from src.Essentials.converter import hex_to_ascii


# ######################### PASSED ######################### #


# -------------------- METHODS -------------------- #
class TestDecryption(unittest.TestCase):
    # -------------------- ECB -------------------- #
    def test_ECB_1(self):
        self.assertEqual("CSS",
                         ecb_decryption(hex_to_ascii("021212"), "A", 8, True, True)
                         )

    def test_ECB_2(self):
        self.assertEqual("Hi Leute!",
                         ecb_decryption(hex_to_ascii("02086A2D2F143E046B"), "Ja", 16, True, True)
                         )

    # -------------------- CBC -------------------- #
    def test_CBC_1(self):
        self.assertEqual("TRY",
                         cbc_decryption(hex_to_ascii("0C0607"), "X", 0, 1, True)
                         )

    # -------------------- CTR -------------------- #
    def test_CTR_1(self):
        self.assertEqual("Test",
                         ctr_decryption(hex_to_ascii("1E2C3B3B"), "K", 0, 1, True)
                         )


if __name__ == '__main__':
    unittest.main()
