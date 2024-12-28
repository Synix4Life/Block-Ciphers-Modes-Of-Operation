# -------------------- IMPORTS -------------------- #
import Essentials.converter as converter
from Essentials.xoring import xor
import Essentials.iv_actions as iv_actions
import Essentials.miscellaneous as misc
from preprocessing import preprocess
from encryption_modes import ecb_encryption, ctr_encryption
import math


# -------------------- METHODS -------------------- #
def cbc_decryption(ciphertext: str, key: str, iv: int, block_size: int = 8, return_as_ascii: bool = False, is_binary_step: bool = False) -> str:
    """
    The method to convert a CBC-encrypted ciphertext into a decrypted plaintext in hex, using a given key and block_size
    :param iv: Random initialization vector, given as string in ASCII format
    :param ciphertext: The CBC-encrypted ciphertext to decrypt
    :param key: The key, with which the ciphertext shall be decrypted
    :param block_size: Block size to decrypt, can be added as binary step or ASCII character steps
    :param return_as_ascii: Boolean to return the ascii representation of the plaintext, by default set to false
    :param is_binary_step: Set to true if the block_size is measured in binary and not in the amount of ASCII characters, by default set to False
    :return: The decrypted text in hexadecimal representation
    :raises AttributeError: If the key isn't from the same size as the value of block_size is
    :raises ValueError: If block_size isn't dividable by 8
    """
    preprocess(key, block_size, is_binary_step)
    binary_plaintext = converter.ascii_to_binary(ciphertext)
    binary_key = converter.ascii_to_binary(key)
    binary_iv = iv_actions.extend_iv(iv, block_size*(1 if is_binary_step else 8))
    divided_text = misc.divide(binary_plaintext,  int(block_size)*(1 if is_binary_step else 8))
    resulting_blocks = []

    for i in range(len(divided_text)):
        tmp = xor(divided_text[i], binary_key)
        if i == 0:
            resulting_blocks.append(xor(tmp, binary_iv))
        else:
            resulting_blocks.append(xor(tmp, divided_text[i-1]))

    hex_result = misc.leading_zeros(resulting_blocks)
    if return_as_ascii:
        return converter.hex_to_ascii(hex_result + converter.binary_to_hex(''.join(resulting_blocks)))
    return hex_result + converter.binary_to_hex(''.join(resulting_blocks))


def ctr_decryption(ciphertext: str, key: str, iv: int, block_size: int = 8, return_as_ascii: bool = False, is_binary_step: bool = False) -> str:
    """
    The method to convert a CTR-encrypted ciphertext into a decrypted plaintext in hex, using a given key and block_size
    :param iv: Random initialization vector, given as string in ASCII format
    :param ciphertext: The CTR-encrypted ciphertext to decrypt
    :param key: The key, with which the ciphertext shall be decrypted
    :param block_size: Block size to decrypt, can be added as binary step or ASCII character steps
    :param return_as_ascii: Boolean to return the ascii representation of the plaintext, by default set to false
    :param is_binary_step: Set to true if the block_size is measured in binary and not in the amount of ASCII characters, by default set to False
    :return: The decrypted text in hexadecimal representation
    :raises AttributeError: If the key isn't from the same size as the value of block_size is
    :raises ValueError: If block_size isn't dividable by 8
    """
    return ctr_encryption(ciphertext, key, iv, block_size, return_as_ascii, is_binary_step)


def ecb_decryption(ciphertext: str, key: str, block_size: int = 8, return_as_ascii: bool = False, is_binary_step: bool = False) -> str:
    """
    The method to convert a ECB-encrypted ciphertext into an decrypted plaintext in hex, using a given key and block_size
    :param ciphertext: The ECB-encrypted ciphertext to decrypt
    :param key: The key, with which the ciphertext shall be decrypted
    :param block_size: Block size to decrypt, can be added as binary step or ASCII character steps
    :param return_as_ascii: Boolean to return the ascii representation of the plaintext, by default set to false
    :param is_binary_step: Set to true if the block_size is measured in binary and not in the amount of ASCII characters, by default set to False
    :return: The decrypted text in hexadecimal representation
    :raises AttributeError: If the key isn't from the same size as the value of block_size is
    :raises ValueError: If block_size isn't dividable by 8
    """
    return ecb_encryption(ciphertext, key, block_size, return_as_ascii, is_binary_step)