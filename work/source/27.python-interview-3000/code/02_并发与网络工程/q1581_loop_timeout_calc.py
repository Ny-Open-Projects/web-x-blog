"""事件循环的超时计算: IO 与定时器混合调度。

一轮循环的骨架:
1) 取定时器堆顶到期时刻, 算出本轮 select 的阻塞上限
   timeout = max(0, next_timer - now); 没有定时器时给兜底值;
2) select(timeout) —— IO 就绪提前醒, 否则睡到最近的定时器;
3) 先跑到点定时器, 再处理就绪 IO。
本演示观察"唤醒延迟": 三个事件(两个定时器 + 一次 IO)的实际触发误差。
"""
import heapq
import select
import socket
import threading
import time


class MiniLoop:
    def __init__(self):
        self.timers = []            # (when, seq, tag)
        self.seq = 0
        self.fired = []             # (kind, tag, now, lateness)

    def call_later(self, delay, tag):
        self.seq += 1
        heapq.heappush(self.timers, (time.monotonic() + delay, self.seq, tag))

    def run_until(self, rsock, io_slot, deadline):
        while time.monotonic() < deadline and (self.timers or io_slot[0] is None):
            now = time.monotonic()
            # 1) 计算本轮阻塞上限: 有定时器睡到最近一个, 没有给兜底
            if self.timers:
                timeout = max(0.0, self.timers[0][0] - now)
            else:
                timeout = 0.2
            # 2) IO 就绪提前醒; 没有任何事件时靠兜底超时防永久睡眠
            ready, _, _ = select.select([rsock], [], [], timeout)
            if ready:
                rsock.recv(4096)
                now = time.monotonic()
                io_slot[0] = now
                self.fired.append(("io", "wake", now, 0.0))
            # 3) 先跑到点定时器
            now = time.monotonic()
            while self.timers and self.timers[0][0] <= now:
                when, _, tag = heapq.heappop(self.timers)
                self.fired.append(("timer", tag, now, now - when))


def main():
    a, b = socket.socketpair()
    a.setblocking(False)
    b.setblocking(False)
    loop = MiniLoop()
    io_slot = [None]
    loop.call_later(0.10, "timer-1")
    loop.call_later(0.35, "timer-2")

    def late_writer():
        time.sleep(0.50)
        b.send(b"wake")             # IO 事件: 0.5s 后从另一端写醒它

    threading.Thread(target=late_writer, daemon=True).start()
    loop.run_until(a, io_slot, deadline=time.monotonic() + 1.0)

    for kind, tag, now, late in loop.fired:
        print("%-5s %-8s 触发, 迟到 %.1fms" % (kind, tag, late * 1000))
    tags = [tag for _, tag, _, _ in loop.fired]
    assert tags == ["timer-1", "timer-2", "wake"], "三个事件都应触发且按序"
    for kind, tag, now, late in loop.fired:
        if kind == "timer":
            assert late < 0.09, "定时器唤醒延迟应在几十毫秒量级"
    print("结论: 超时计算是循环的心跳——睡到最近定时器, IO 一来立刻打断")


if __name__ == "__main__":
    main()
