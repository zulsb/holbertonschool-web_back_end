#!/usr/bin/env python3
""" Multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """ Async routine.
        Args:
            max_delay: integer argument.
            n: integer argument.
        Return:
            List of all the delays random float.
    """
    delays: List[float] = []

    for i in range(n):
        delays.append(wait_random(max_delay))

    return [await ordered for ordered in asyncio.as_completed(delays)]
