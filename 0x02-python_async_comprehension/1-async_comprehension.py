#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """ Coroutine will collect 10 random numbers.
        Return the 10 random numbers.
    """
    return [g async for g in async_generator()]
