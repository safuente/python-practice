import asyncio
import time

semaphore = asyncio.Semaphore(2)


async def greet(name: str):
    async with semaphore:
        await asyncio.sleep(1)
        print(f"Hello {name}!")


async def main():
    start = time.perf_counter()
    await asyncio.gather(
        greet("Peter"),
        greet("Parker"),
        greet("Spiderman")
    )
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")


asyncio.run(main())

