import Essentials.converter as converter
from Essentials.xoring import xor
import Essentials.iv_actions as iv_actions
import Essentials.miscellaneous as misc
import math


def cbc_decryption(ciphertext: str, key: str, iv: int, block_size: int = 8, is_binary_step: bool = False) -> str:
    if is_binary_step:
        block_size = block_size / 8
    if not block_size == math.floor(block_size):
        raise ValueError("Block_size should be dividable by 8")
    if not len(key) == block_size:
        raise AttributeError(f"Key should have block size!\nExpected block size {len(key)}, but got {block_size}."
                             f"\n Did you forget that there is an IV in CBC Mode :-)? \n"
                             f"Try changing the input block_size or set is_binary_step to true.")
    binary_plaintext = converter.ascii_to_binary(ciphertext)
    binary_key = converter.ascii_to_binary(key)
    binary_iv = iv_actions.extend_iv(iv, block_size*8)
    divided_text = misc.divide(binary_plaintext,  int(block_size)*8)
    resulting_blocks = []

    for i in range(len(divided_text)):
        tmp = xor(divided_text[i], binary_key)
        if i == 0:
            resulting_blocks.append(xor(tmp, binary_iv))
        else:
            resulting_blocks.append(xor(tmp, divided_text[i-1]))

    hex_result = misc.leading_zeros(resulting_blocks)
    return hex_result + converter.binary_to_hex(''.join(resulting_blocks))


def ctr_decryption(ciphertext: str, key: str, iv: int, block_size: int = 8, is_binary_step: bool = False) -> str:
    if is_binary_step:
        block_size = block_size / 8
    if not block_size == math.floor(block_size):
        raise ValueError("Block_size should be dividable by 8")
    if not len(key) == block_size:
        raise AttributeError(f"Key should have block size!\nExpected block size {len(key)}, but got {block_size}."
                             f"\n Did you forget that there is an IV in CTR Mode :-)? \n"
                             f"Try changing the input block_size or set is_binary_step to true.")
    binary_plaintext = converter.ascii_to_binary(ciphertext)
    binary_key = converter.ascii_to_binary(key)
    extended_iv = iv_actions.extend_iv(iv, block_size*8)
    divided_text = misc.divide(binary_plaintext,  int(block_size)*8)
    resulting_blocks = []

    for i in range(len(divided_text)):
        extended_iv = iv_actions.increment_iv(extended_iv)
        encrypted = xor(extended_iv, binary_key)
        resulting_blocks.append(xor(divided_text[i], encrypted))

    hex_result = misc.leading_zeros(resulting_blocks)
    return hex_result + converter.binary_to_hex(''.join(resulting_blocks))


def ecb_decryption(ciphertext: str, key: str, block_size: int = 8, is_binary_step: bool = False) -> str:
    if is_binary_step:
        block_size = block_size / 8
    if not block_size == math.floor(block_size):
        raise ValueError("Block_size should be dividable by 8")
    if not len(key) == block_size:
        raise AttributeError(f"Key should have block size\nExpected block size = {len(key)}, but got {block_size}."
                             f"\nTry changing the input block_size or set is_binary_step to true.")
    binary_ciphertext = converter.ascii_to_binary(ciphertext)
    binary_key = converter.ascii_to_binary(key)
    divided_text = misc.divide(binary_ciphertext, int(block_size)*8)
    resulting_blocks = []
    for block in divided_text:
        resulting_blocks.append(xor(block, binary_key))
    hex_result = misc.leading_zeros(resulting_blocks)
    return hex_result + converter.binary_to_hex(''.join(resulting_blocks))
