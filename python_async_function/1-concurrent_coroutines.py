
#!/usr/bin/env python3
"""Execute multiple coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return delays in ascending order."""
    delays = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delays.append(task)

    results = []
    for task in asyncio.as_completed(delays):
        results.append(await task)

    return results
