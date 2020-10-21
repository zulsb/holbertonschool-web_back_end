#!/usr/bin/env python3
""" Tasks """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Async routine.
        Args:
            max_delay: integer argument.
            n: integer argument.
        Return:
            List of all the delays random float.
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
