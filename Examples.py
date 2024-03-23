# -------------------- Imports --------------------#
from Essentials.converter import hex_to_ascii
from encryption_modes import ecb_encryption as ecb
from encryption_modes import cbc_encryption as cbc
from encryption_modes import ctr_encryption as ctr

# -------------------- Examples --------------------#

print(
    ecb("Just a random plaintext", "This is our key", 15)
)

print(
    cbc("Now, lets try CBC Encryption and convert the result to ASCII", "Remember the IV", 11, 15, True)
)

print(
    ctr("Remember: BlockSize should be equal to the length of the key", "In this case, the key has length 35", 0, 35)
)
