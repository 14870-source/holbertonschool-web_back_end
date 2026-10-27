#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values() -> None:
    """Collect and print all values yielded by the async generator."""
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)


asyncio.run(print_yielded_values())
