#!/usr/bin/env python3
"""this module contains the solution to task 0"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits a random amoint of seconds and then returns the seconds"""

    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
