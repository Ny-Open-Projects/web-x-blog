import heapq
import selectors
import socket
import time
from collections import deque


class MiniLoop:
    def __init__(self) -> None:
        self._ready: deque = deque()
        self._timers = []  # 堆: (deadline, seq, task)
        self._seq = 0
        self._sel = selectors.DefaultSelector()
        self._fd_task = {}  # fd -> task

    def spawn(self, gen) -> None:
        self._ready.append({"gen": gen, "value": None})

    def sleep(self, delay: float):
        return ("sleep", delay)  # 生成器 yield 这个元组表示 trap

    def read(self, sock):
        return ("read", sock)

    def _step(self, task: dict) -> None:
        try:
            trap = task["gen"].send(task["value"])
        except StopIteration:
            return
        op = trap[0]
        if op == "sleep":
            self._seq += 1
            heapq.heappush(self._timers, (time.monotonic() + trap[1], self._seq, task))
        elif op == "read":
            sock = trap[1]
            sock.setblocking(False)
            self._sel.register(sock, selectors.EVENT_READ, task)
            self._fd_task[sock.fileno()] = sock

    def run(self) -> None:
        while self._ready or self._timers or self._fd_task:
            timeout = None
            if not self._ready:
                if self._timers:
                    timeout = max(0.0, self._timers[0][0] - time.monotonic())
                for key, _ in self._sel.select(timeout):
                    sock = self._fd_task.pop(key.fd)
                    self._sel.unregister(sock)
                    task = key.data
                    task["value"] = sock.recv(1024)  # 内核代劳读取后回传
                    self._ready.append(task)
            now = time.monotonic()
            while self._timers and self._timers[0][0] <= now:
                task = heapq.heappop(self._timers)[2]
                task["value"] = None
                self._ready.append(task)
            if self._ready:
                self._step(self._ready.popleft())
            elif self._timers:
                continue  # 没有就绪任务, 回去 select 等最近定时器


def producer(sock: socket.socket, loop: MiniLoop) -> None:
    for i in range(3):
        sock.sendall(f"msg{i} ".encode())
        yield loop.sleep(0.1)
    print("producer 结束")


def consumer(sock: socket.socket, loop: MiniLoop) -> None:
    got = b""
    for _ in range(3):
        chunk = yield loop.read(sock)  # 挂起等 fd 就绪, 恢复时拿到数据
        got += chunk
        print("consumer 收到:", chunk.decode())
    print("consumer 汇总:", got.decode())


if __name__ == "__main__":
    a, b = socket.socketpair()
    loop = MiniLoop()
    loop.spawn(consumer(b, loop))
    loop.spawn(producer(a, loop))
    t0 = time.perf_counter()
    loop.run()
    print(f"迷你事件循环跑完, 耗时 {time.perf_counter() - t0:.2f}s")
