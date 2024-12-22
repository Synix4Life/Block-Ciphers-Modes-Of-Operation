# ################## Imports ################### #
from src.encryption_modes import ecb_encryption, ctr_encryption, cbc_encryption

# ################## Examples ################## #

"""
args:
--- 1. plaintext: str
--- 2. key: str
--- 3. block_size: int
"""
print(
    ecb_encryption("Just a random plaintext", "This is our key", 15)
)

# Output: >> 1E1D1A07000853520E1B164F0645093809001D540C0B54

"""
args:
--- 1. plaintext: str
--- 2. key: str
--- 3. iv: int
--- 4. block_size: int
--- 5. return_as_ascii: bool
"""
print(
    cbc_encryption("Now, lets try CBC Encryption and convert the result to ASCII", "Remember the IV", 11, 15, True)
)

# Output: >> �IMSTYi
# T)0-�oL�QTU
#        _,_-MA|:<,@

"""
args:
--- 1. plaintext: str
--- 2. key: str
--- 3. iv: int
--- 4. block_size: int
"""
print(
    ctr_encryption("Remember: BlockSize should be equal to the length of the key", "In this case, the key has length 35", 0, 35)
)

# Output: >> 1B0B4D11050B16525941310943431F3B0C5A0E450A4807141F444C070B471119555258691A4F541C0116000F041D025848540703001F0D1C0003040A
