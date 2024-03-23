import unittest

from encryption_modes import *


# ------------------------- PASSED -------------------------#


class TestEncryption(unittest.TestCase):
    # -------------------- ECB -------------------- #
    def test_ECB_1(self):
        self.assertEqual("021212", ecb_encryption("CSS", "A", 8, False, True))

    def test_ECB_2(self):
        self.assertEqual("02086A2D2F143E046B", ecb_encryption("Hi Leute!", "Ja", 2))

    # -------------------- CBC -------------------- #
    def test_CBC_1(self):
        self.assertEqual("0C0607", cbc_encryption("TRY", "X", 0, 1))

    # -------------------- CTR -------------------- #
    def test_CTR_1(self):
        self.assertEqual("1E2C3B3B", ctr_encryption("Test", "K", 0, 1))


if __name__ == '__main__':
    unittest.main()
