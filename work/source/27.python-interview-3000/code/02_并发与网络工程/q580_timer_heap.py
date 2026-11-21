import asyncio
import heapq


class TimerHeap:
    """复刻 asyncio 定时器堆: 惰性删除 + seq 保证同时到期 FIFO。"""

    def __init__(self) -> None:
        self._heap = []
        self._seq = 0

    def call_later(self, delay: float, callback, *args):
        deadline = asyncio.get_running_loop().time() + delay
        self._seq += 1
        handle = {"cancelled": False, "cb": callback, "args": args}
        heapq.heappush(self._heap, (deadline, self._seq, handle))
        return handle

    def cancel(self, handle) -> bool:
        if handle["cancelled"]:
            return False
        handle["cancelled"] = True  # 惰性删除: 只标记
        return True

    def fire_due(self, now: float) -> int:
        fired = 0
        while self._heap and self._heap[0][0] <= now:
            deadline, _seq, handle = heapq.heappop(self._heap)
            if not handle["cancelled"]:  # 已取消的直接丢弃
                handle["cb"](*handle["args"])
                fired += 1
        return fired


async def main() -> None:
    loop = asyncio.get_running_loop()
    fired = []

    heap = TimerHeap()
    # 乱序注册: 0.15 最晚注册却最先到期
    h1 = heap.call_later(0.15, lambda: fired.append("0.15s"))
    heap.call_later(0.05, lambda: fired.append("0.05s-a"))
    heap.call_later(0.05, lambda: fired.append("0.05s-b"))
    heap.call_later(0.10, lambda: fired.append("0.10s"))
    heap.cancel(h1)  # 取消 0.15 那个

    start = loop.time()
    while heap._heap:
        loop_time = loop.time()
        if heap._heap[0][0] > loop_time:
            await asyncio.sleep(heap._heap[0][0] - loop_time)
        heap.fire_due(loop.time())
    print("手写堆触发顺序:", fired)
    assert fired == ["0.05s-a", "0.05s-b", "0.10s"], "同时到期应 FIFO, 已取消应跳过"

    # 对照: 真实 loop.call_later 行为一致
    order = []
    loop.call_later(0.05, lambda: order.append("a"))
    loop.call_later(0.05, lambda: order.append("b"))
    cancel_me = loop.call_later(0.01, lambda: order.append("never"))
    cancel_me.cancel()
    await asyncio.sleep(0.1)
    print("asyncio.call_later 顺序:", order)
    assert order == ["a", "b"]


asyncio.run(main())
