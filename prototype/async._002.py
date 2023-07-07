import asyncio


async def fetch_data():
    print("start fetch")
    await asyncio.sleep(2)
    print("finish fetch")
    return {"data": 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task_001 = asyncio.create_task(fetch_data())
    task_002 = asyncio.create_task(print_numbers())

    value_wrong = task_001
    print(value_wrong)
    value = await task_001
    print(value)
    await task_002  # ensures the second task also completes


asyncio.run(main())
