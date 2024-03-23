def divide(text: str, block_size: int) -> list[str]:
    """
    Function to divide a string into substrings with a specific length
    :param text: Input string to divide
    :param block_size: Size to which it shall be divided
    :return: An array of strings, which represents the substrings
    """
    array = []
    while len(text) > 0:
        array.append(text[:block_size])
        text = text[block_size:]
    return array


def leading_zeros(array: list[str]) -> str:
    """
    Method to add leading zeros before converting a string array to a hexadecimal string
    :param array: The array, to look at the amount of zeros to add
    :return: A string with the amount of leading zeros
    """
    result = ''
    for array_block in array:
        if array_block[:4] != '0000':
            break
        else:
            result = result + '0'
        if array_block[4:] != '0000':
            break
        else:
            result = result + '0'
    return result
