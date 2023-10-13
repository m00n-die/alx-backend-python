import asyncio
import random

async def wait_random(max_delay=10):
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time

# Create an event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(wait_random())
loop.close()
