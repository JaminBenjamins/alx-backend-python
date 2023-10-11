#!/usr/bin/env python3
""" A python looping ten times and returning a random number"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        async_generator - function to loop 10 times
        Arguments:
            None
        return a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
