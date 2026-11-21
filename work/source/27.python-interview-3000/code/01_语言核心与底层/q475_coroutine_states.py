import inspect
import types

@types.coroutine
def suspend_once():
    yielded = yield "suspended"           # 挂起点
    return "wake value"

async def worker():
    got = await suspend_once()
    return f"got {got}"

if __name__ == "__main__":
    coro = worker()
    print(inspect.getcoroutinestate(coro))   # CORO_CREATED
    print(coro.send(None))                   # 穿透 yield,协程挂起
    print(inspect.getcoroutinestate(coro))   # CORO_SUSPENDED
    try:
        coro.send("resumed")
    except StopIteration as stop:
        print("result:", stop.value)
    print(inspect.getcoroutinestate(coro))   # CORO_CLOSED
