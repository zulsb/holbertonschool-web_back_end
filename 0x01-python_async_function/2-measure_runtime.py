#!/usr/bin/env python3
""" Measure the runtime """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function that measures the total execution time
        for the wait_n function.
        Args:
            n: integer argument.
            max_delay: integer argument.
        Return:
            Float.
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
