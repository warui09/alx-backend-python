#!/usr/bin/env python3
"""solution to task 2"""

import asyncio, time
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n"""

    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()

    return (end - start) / n
