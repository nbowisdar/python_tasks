import asyncio


async def do_async_work():
    print("Call external api")
    await asyncio.sleep(3)


async def main():
    tasks = [do_async_work() for _ in range(5)]
    await asyncio.gather(*tasks)
    print("Done")


asyncio.run(main())
