#!/usr/bin/env python3
"""contains solution to task 1"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """call wait_random n times with the specified max_delay"""

    return [await wait_random(max_delay) for i in range(n)]
