#!/usr/bin/env python3
"""task 1 solution"""

import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """collect and return 10 random numbers using an async comprehensing
    over async_generator"""

    return [random_float async for random_float in async_generator()]
