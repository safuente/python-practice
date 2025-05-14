import asyncio
import time


async def greet(name: str):
    await asyncio.sleep(1)
    print(f"Hello {name}!")


async def main():
    start = time.perf_counter()
    await asyncio.gather(
        greet("Peter"),
        greet("Parker")
    )
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")


asyncio.run(main())
