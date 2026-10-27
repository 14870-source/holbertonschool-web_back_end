#!/usr/bin/env python3

import asyncio

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def main() -> None:
    """Run the asynchronous comprehension."""
    print(await async_comprehension())


asyncio.run(main())