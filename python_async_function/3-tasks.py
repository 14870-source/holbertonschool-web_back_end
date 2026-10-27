#!/usr/bin/env python3
"""Create an asyncio task for a random delay."""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> "asyncio.Task[Any]":
    """Create and return an asyncio task."""
    return asyncio.create_task(wait_random(max_delay))
