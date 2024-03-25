# ################## Imports ################### #
from encryption_modes import ecb_encryption as ecb
from encryption_modes import cbc_encryption as cbc
from encryption_modes import ctr_encryption as ctr

# ################## Examples ################## #

"""
args:
--- 1. plaintext: str
--- 2. key: str
--- 3. block_size: int
"""
print(
    ecb("Just a random plaintext", "This is our key", 15)
)

"""
args:
--- 1. plaintext: str
--- 2. key: str
--- 3. iv: int
--- 4. block_size: int
--- 5. return_as_ascii: bool
"""
print(
    cbc("Now, lets try CBC Encryption and convert the result to ASCII", "Remember the IV", 11, 15, True)
)

"""
args:
--- 1. plaintext: str
--- 2. key: str
--- 3. iv: int
--- 4. block_size: int
"""
print(
    ctr("Remember: BlockSize should be equal to the length of the key", "In this case, the key has length 35", 0, 35)
)
