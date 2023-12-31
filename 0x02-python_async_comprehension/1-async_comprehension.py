#!/usr/bin/env python3
""" A function to return 10 random numbers using async comprehension """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        async_comprehension - function to return ten random numbers
        Arguments:
            no arguments
        Return:
            10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
