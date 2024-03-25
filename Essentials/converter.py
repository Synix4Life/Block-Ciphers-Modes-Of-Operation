def ascii_to_binary(text: str) -> str:
    """
    Method to convert the input text as binary representation using ASCII
    :param text: Text as ASCII to be converted to binary
    :return: Converted binary string
    """
    return ''.join([bin(ord(char))[2:].zfill(8) for char in text])


def binary_to_hex(text: str) -> str:
    """
    Method to convert a binary string input into a hexadecimal string
    :param text: Uncut binary string that shall be converted
    :return: The hexadecimal string
    """
    return hex(int(text, 2))[2:].upper()


def hex_to_ascii(text: str) -> str:
    """
    Method to convert a hex string input into an ASCII string
    :param text: Hexadecimal string
    :return: The ASCII representation of the hexadecimal string
    """
    if text[:2] == "0x":
        text = text[2:]
    return bytes.fromhex(text).decode("ascii")


def hex_to_binary(text: str) -> str:
    """
    Method to convert the input hex string to binary representation
    :param text: Hexadecimal string
    :return: Converted binary string
    """
    try:
        if text[:2] == "0b":
            text = text[2:]
        binary_str = bin(int(text, 16))[2:]
        return "0" * (len(text) * 4 - len(binary_str)) + binary_str
    except ValueError:
        return "Invalid hexadecimal string"


def binary_to_ascii(text: str) -> str:
    """
    Method to convert the binary string to an ASCII string
    :param text: Binary string
    :return: The ASCII string
    """
    return hex_to_ascii(binary_to_hex(text))


def ascii_to_hex(text: str) -> str:
    """
    Method to convert the ASCII string to hexadecimal string
    :param text: ASCII string
    :return: The hexadecimal string
    """
    return binary_to_hex(ascii_to_binary(text))
