#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """ Coroutine will collect 10 random numbers.
        Return the 10 random numbers.
    """
    return [g async for g in async_generator()]
