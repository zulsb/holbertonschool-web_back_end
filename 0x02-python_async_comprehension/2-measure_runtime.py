#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine will collect 10 random numbers.
        Return the 10 random numbers.
    """
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(3)))
    totalRuntime = time.perf_counter() - s
    return totalRuntime
