# -------------------- IMPORTS -------------------- #
import Essentials.converter as converter
from Essentials.xoring import xor
import Essentials.iv_actions as iv_actions
import Essentials.miscellaneous as misc
from preprocessing import preprocess
import math


# -------------------- METHODS -------------------- #
def cbc_encryption(plaintext: str, key: str, iv: int, block_size: int = 8, return_as_ascii: bool = False, is_binary_step: bool = False) -> str:
    """
    The method to convert a plaintext into an CBC-encrypted ciphertext in hex, using a given key and block_size
    :param iv: Random initialization vector, given as string in ASCII format
    :param plaintext: The plaintext to encrypt
    :param key: The key, with which the plaintext shall be encrypted
    :param block_size: Block size to encrypt, can be added as binary step or ASCII character steps
    :param return_as_ascii: Boolean to return the ascii representation of the ciphertext, by default set to false
    :param is_binary_step: Set to true if the block_size is measured in binary and not in the amount of ASCII characters, by default set to False
    :return: The CBC-mode encrypted text in hexadecimal representation
    :raises AttributeError: If the key isn't from the same size as the value of block_size is
    :raises ValueError: If block_size isn't dividable by 8
    """
    preprocess(key, block_size, is_binary_step)
    binary_plaintext = converter.ascii_to_binary(plaintext)
    binary_key = converter.ascii_to_binary(key)
    binary_iv = iv_actions.extend_iv(iv, block_size*(1 if is_binary_step else 8))
    divided_text = misc.divide(binary_plaintext, int(block_size)*(1 if is_binary_step else 8))
    resulting_blocks = []

    for i in range(len(divided_text)):
        if i == 0:
            tmp = xor(divided_text[i], binary_iv)
        else:
            tmp = xor(divided_text[i], resulting_blocks[i - 1])
        resulting_blocks.append(xor(tmp, binary_key))

    hex_result = misc.leading_zeros(resulting_blocks)
    if return_as_ascii:
        return converter.hex_to_ascii(hex_result + converter.binary_to_hex(''.join(resulting_blocks)))
    return hex_result + converter.binary_to_hex(''.join(resulting_blocks))


def ctr_encryption(plaintext: str, key: str, iv: int, block_size: int = 8, return_as_ascii: bool = False, is_binary_step: bool = False) -> str:
    """
    The method to convert a plaintext into an CTR-encrypted ciphertext in hex, using a given key and block_size
    :param iv: Random initialization vector, given as string in ASCII format
    :param plaintext: The plaintext to encrypt
    :param key: The key, with which the plaintext shall be encrypted
    :param block_size: Block size to encrypt, can be added as binary step or ASCII character steps
    :param return_as_ascii: Boolean to return the ascii representation of the ciphertext, by default set to false
    :param is_binary_step: Set to true if the block_size is measured in binary and not in the amount of ASCII characters, by default set to False
    :return: The CTR-mode encrypted text in hexadecimal representation
    :raises AttributeError: If the key isn't from the same size as the value of block_size is
    :raises ValueError: If block_size isn't dividable by 8
    """
    preprocess(key, block_size, is_binary_step)
    binary_plaintext = converter.ascii_to_binary(plaintext)
    binary_key = converter.ascii_to_binary(key)
    extended_iv = iv_actions.extend_iv(iv, block_size*(1 if is_binary_step else 8))
    divided_text = misc.divide(binary_plaintext, int(block_size)*(1 if is_binary_step else 8))
    resulting_blocks = []

    for i in range(len(divided_text)):
        extended_iv = iv_actions.increment_iv(extended_iv)
        encrypted = xor(extended_iv, binary_key)
        resulting_blocks.append(xor(divided_text[i], encrypted))

    hex_result = misc.leading_zeros(resulting_blocks)
    if return_as_ascii:
        return converter.hex_to_ascii(hex_result + converter.binary_to_hex(''.join(resulting_blocks)))
    return hex_result + converter.binary_to_hex(''.join(resulting_blocks))


def ecb_encryption(plaintext: str, key: str, block_size: int = 8, return_as_ascii: bool = False, is_binary_step: bool = False) -> str:
    """
    The method to convert a plaintext into an ECB- encrypted ciphertext in hex, using a given key and block_size
    :param plaintext: The plaintext to encrypt
    :param key: The key, with which the plaintext shall be encrypted
    :param block_size: Block size to encrypt, can be added as binary step or ASCII character steps
    :param return_as_ascii: Boolean to return the ascii representation of the ciphertext, by default set to false
    :param is_binary_step: Set to true if the block_size is measured in binary and not in the amount of ASCII characters, by default set to False
    :return: The ECB- mode encrypted text in hexadecimal representation
    :raises AttributeError: If the key isn't from the same size as the value of block_size is
    :raises ValueError: If block_size isn't dividable by 8
    """
    preprocess(key, block_size, is_binary_step)
    binary_plaintext = converter.ascii_to_binary(plaintext)
    binary_key = converter.ascii_to_binary(key)
    divided_text = misc.divide(binary_plaintext, int(block_size)*(1 if is_binary_step else 8))
    resulting_blocks = []
    for block in divided_text:
        resulting_blocks.append(xor(block, binary_key))
    hex_result = misc.leading_zeros(resulting_blocks)
    if return_as_ascii:
        return converter.hex_to_ascii(hex_result + converter.binary_to_hex(''.join(resulting_blocks)))
    return hex_result + converter.binary_to_hex(''.join(resulting_blocks))
