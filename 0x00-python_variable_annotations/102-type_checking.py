#!/usr/bin/env python3
'''12. Type Checking'''

from typing import List

def zoom_array(lst: List, factor: int = 2) -> List:
	'''Zoom in on the elements of a list by repeating each element a given number of times.

    Args:
        lst (List): The list containing elements to zoom in on.
        factor (int, optional): The zoom factor indicating how many times to repeat each element.
    Defaults to 2.

    Returns:
      List: The zoomed-in list, where each element is repeated according to the zoom factor.
	'''
  zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in
