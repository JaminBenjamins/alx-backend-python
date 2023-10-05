#!/usr/bin/env python3
""" A function that multiplies a float by a multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiplies a float by a multiplier
    Args: 
        multiplier (float): The multiplier
    Returns:
        A function that multiplies by a value 
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by a multiplier"""
        return multiplier * number

    return multiplier_func
