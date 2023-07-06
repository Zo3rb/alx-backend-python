#!/usr/bin/env python3
'''8. Complex types - functions'''

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies a float by the given multiplier.

    Args:
      multiplier (float): The multiplier value.

    Returns: Callable[[float], float]: A function to multiply a float by the multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply

