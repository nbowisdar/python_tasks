import asyncio


async def do_async_work():
    print("Call external api")
    await asyncio.sleep(3)
    
    

async def main():
    for _ in range(5):
        await do_async_work()


    """
    Зробити так що б функція do_async_work викликалась 5 разів одночасно. 
    """

    
asyncio.run(main())


