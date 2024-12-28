def xor(value1: str, value2: str) -> str:
    """
    A method to XOR two individual values
    :param value1: XOR value 1
    :param value2: XOR value 2
    :return:The XORed text
    :raises ValueError: If value1 is larger then value2
    """
    if len(value1) > len(value2):
        raise ValueError(f"Value1 shouldn't be longer then value2: Got value1 {value1}, value2 {value2}")
    return ''.join([str(int(value1[i]) ^ int(value2[i])) for i in range(len(value1))])