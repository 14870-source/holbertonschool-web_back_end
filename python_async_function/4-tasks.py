#!/usr/bin/env python3
"""Execute multiple tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple tasks and return delays in completion order."""
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
