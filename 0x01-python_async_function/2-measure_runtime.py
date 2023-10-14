#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delya: int) -> float:
    """measures the total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elasped_time = (time.time() - start_time) / n
    return elasped_time
