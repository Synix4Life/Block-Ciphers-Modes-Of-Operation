import math

def preprocess(key: str, block_size: int, is_binary_step: bool) -> None:
    """
    Method to preprocess the input data
    :param key: The key
    :param block_size: The block size
    :param is_binary_step: If block_size is binary
    """
    if is_binary_step:
        block_size = block_size / 8
        if not block_size == math.floor(block_size):
            raise ValueError("Block_size should be dividable by 8")
    if not len(key) == block_size:
        raise AttributeError(f"InsideKey should have block size!\nExpected block size {len(key)}, but got {block_size}.")