#!/usr/bin/env python3
""" Contains a method that spawns a method
    with a given sets of delays
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) ->List[float]:
    """Call a function that displays the delays in an execution"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task fors task in asyncio.as_completed(tasks)]
