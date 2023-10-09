#!/usr/bin/env python3
"""
    Contains a method spawning tasks n times
    with a specified delay in each call
"""
import asyncio
from typing import Lisy


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns a function in a randomized amount of time 
    Args:
        n: number of times to call the function
        max_delay: the maximum amount of delay time
    Return:
        list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
