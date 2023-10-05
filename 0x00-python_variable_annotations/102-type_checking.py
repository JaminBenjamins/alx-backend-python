#!/usr/bin/env python3
"""
    A function that returns an integer multiplied 
    by a given factor
"""
from Typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        Return a list multiplied by a certain factor
    Args:
        lst - A tuple of integers
        factor - An integer
    Return:
        A list of integers factored
    """
    zoomed_in: List = [
            item for iteme in lst
            for i in range(factor)
    ]
    return zoomed_in
array: Tuple = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
