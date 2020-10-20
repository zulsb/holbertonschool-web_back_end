#!/usr/bin/env python3
""" Basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes an int argument and
        waits for a random delay seconds.
        Args:
            max_delay: integer argument.
        Return:
            Random float.
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
