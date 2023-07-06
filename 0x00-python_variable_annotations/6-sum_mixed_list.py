#!/usr/bin/env python3
'''6. Complex types - mixed list'''

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)

