def extend_iv(iv: int, block_size: int = 8) -> str:
    """
    Extends an initialization vector to the needed block_size
    :param iv: The IV to extend
    :param block_size: Block size, by default set to 8
    :return: The extended IV as a string
    """
    binary_iv = bin(iv)[2:]
    return '0' * (block_size - len(binary_iv)) + binary_iv


def increment_iv(iv: str) -> str:
    """
    Increments the initialization vector by 1
    :param iv: The IV to extend
    :return: IV + 1 in a binary string
    :raises OverflowError: If there occurs an overflow
    """
    binary = bin(int(iv, 2) +1)[2:]
    if len(binary) > len(iv):
        raise OverflowError("IV Overflow")
    return '0' * (len(iv) - len(binary)) + binary
