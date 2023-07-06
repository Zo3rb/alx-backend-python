#!/usr/bin/env python3
'''7. Complex types - string and int/float to tuple'''

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an int or float.

    Args:
        k (str): The string element of the tuple.
        v (Union[int, float]): The int or float element of the tuple.

    Returns:
        Tuple[str, float]: The tuple containing the string and the square of the int/float.
    """
    return k, v ** 2.0

