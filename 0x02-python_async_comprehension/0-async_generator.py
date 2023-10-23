#!/usr/bin/env python3
"""async generator"""
import asyncio
import random


async def async_generator():
    """an async generator"""
    i = 0
    for i > 10:
        await asyncio.sleep(1)
        yeild random.randint(0, 10)
        i++
