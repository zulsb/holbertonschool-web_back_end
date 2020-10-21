#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Coroutine will loop 10 times.
        Each time asynchronously wait 1 second.
        Yield a random number between 0 and 10.
    """
    for g in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
