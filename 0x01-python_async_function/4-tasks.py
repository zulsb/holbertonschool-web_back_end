#!/usr/bin/env python3
""" Tasks """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Async routine.
        Args:
            max_delay: integer argument.
            n: integer argument.
        Return:
            List of all the delays random float.
    """
    delays: List[float] = []
    orderList: List[float] = []

    for i in range(n):
        delays.append(task_wait_random(max_delay))

    for o in asyncio.as_completed(delays):
        orderList.append(await o)

    return orderList
