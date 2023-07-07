import asyncio


async def main():
    print("Hello")
    task = asyncio.create_task(foo("world"))
    await task
    print("beautiful")


async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print("bye")  # will not print unless awaited


asyncio.run(main())
