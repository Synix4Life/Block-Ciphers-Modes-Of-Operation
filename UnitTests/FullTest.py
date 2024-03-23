import unittest

import decryption_modes
import encryption_modes


# ------------------------- PASSED -------------------------#


class FullTest(unittest.TestCase):
    def test_full_ecb(self):
        self.assertEqual("This is a text, couldn't guess that...", decryption_modes.ecb_decryption(
            encryption_modes.ecb_encryption(
                "This is a text, couldn't guess that...", "key", 3, True
            )
            , "key", 3, True
        ))

    def test_full_ctr(self):
        self.assertEqual("CTRTXT", decryption_modes.ctr_decryption(
            encryption_modes.ctr_encryption(
                "CTRTXT", "ll", 25, 2, True
            )
            , "ll", 25, 2, True
        ))

    def test_full_cbc(self):
        self.assertEqual("whatever", decryption_modes.cbc_decryption(
            encryption_modes.cbc_encryption(
                "whatever", "key", 0, 3, True
            )
            , "key", 0, 3, True
        ))


if __name__ == '__main__':
    unittest.main()
