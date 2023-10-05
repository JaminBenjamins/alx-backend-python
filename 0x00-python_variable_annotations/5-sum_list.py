#!/usr/bin/env python3
""" A function that sums a list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sum a list of floats
    Args:
        Input_list(list): A list of floats
    Returns:
        float: The sum of floats in the list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
