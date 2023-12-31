#!/usr/bin/env python3
""" Contains a function that measure
    execution time of a function
"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measuring total execution time of a function
    Args:
        n: the number of coroutines to launch
        max_delay: maximum amount to wait for execution
    Returns: Time spent in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
