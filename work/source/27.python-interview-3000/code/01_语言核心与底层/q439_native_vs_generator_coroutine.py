import types
import inspect

@types.coroutine
def generator_sleep():
    """生成器协程:yield 一个值给底层驱动者"""
    yielded = yield "SLEEP"
    return yielded

async def native_main():
    result = await generator_sleep()      # await 可以等待生成器协程
    return f"resumed with {result}"

if __name__ == "__main__":
    coro = native_main()
    print(type(coro).__name__)            # coroutine
    print("iscoroutine:", inspect.iscoroutine(coro))
    print("isgenerator:", inspect.isgenerator(coro))
    print(coro.send(None))                # 穿透到生成器协程的 yield:打印 SLEEP
    try:
        coro.send("wake")
    except StopIteration as stop:
        print("result:", stop.value)
