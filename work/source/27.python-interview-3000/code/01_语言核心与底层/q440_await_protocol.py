class SimpleFuture:
    """最小可等待对象:yield 一次交给驱动者,被唤醒后返回结果"""
    def __init__(self, done_value):
        self.done_value = done_value

    def __await__(self):
        woke = yield self             # 挂起:把这个对象抛给驱动者
        return woke or self.done_value

async def fetch():
    value = await SimpleFuture(42)
    return value * 2

if __name__ == "__main__":
    coro = fetch()
    yielded = coro.send(None)         # 拿到 yield 出的 SimpleFuture
    print("yielded to driver:", type(yielded).__name__)
    try:
        coro.send(100)                # 驱动者「就绪后」唤醒协程
    except StopIteration as stop:
        print("final:", stop.value)   # 200
