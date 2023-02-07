#!/usr/bin/env python3
"""Contains a method that spawns wait_random n times with a
specified delay between each call."""
import asyncio
from typing import List

wait_random = __import__('1-concurrent_coroutines').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of a function
    Args:
        n: the number of coroutines to launch
        max_delay: the maximum amount of time to wait for each coroutine
    Returns: elapsed time in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
