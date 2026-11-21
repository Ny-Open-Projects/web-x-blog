import concurrent.futures
import threading
import time


def slow_work() -> None:
    time.sleep(0.05)


def unbounded_queue(jobs: int, workers: int = 4) -> dict:
    start = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futs = [pool.submit(slow_work) for _ in range(jobs)]
        concurrent.futures.wait(futs)
    return {"served": jobs, "shed": 0,
            "tail_s": time.monotonic() - start,
            "reject_latency_s": 0.0}


class ShedingGate:
    def __init__(self, workers: int, queue_cap: int) -> None:
        self._slots = threading.BoundedSemaphore(workers + queue_cap)
        self._pool = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
        self.served = 0
        self.shed = 0

    def handle(self, timeout: float = 2.0) -> str:
        if not self._slots.acquire(blocking=False):
            self.shed += 1
            return "SHED 503"          # 排队区满: 立刻拒绝
        fut = self._pool.submit(slow_work)
        try:
            fut.result(timeout=timeout)
            self.served += 1
            return "200"
        finally:
            self._slots.release()

    def close(self) -> None:
        self._pool.shutdown(wait=True)


def main() -> None:
    jobs = 60
    r1 = unbounded_queue(jobs)
    print(f"全部排队: 服务 {r1['served']}, 拒绝 {r1['shed']}, 尾请求等待 {r1['tail_s']:.2f}s")

    gate = ShedingGate(workers=4, queue_cap=10)
    start = time.monotonic()

    def one_call(_):
        t0 = time.monotonic()
        kind = gate.handle()
        return kind, time.monotonic() - t0

    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as clients:
        results = list(clients.map(one_call, range(jobs)))
    wall = time.monotonic() - start
    gate.close()
    shed_n = [k for k, _ in results].count("SHED 503")
    print(f"快速失败: 服务 {gate.served}, 立刻拒绝 {shed_n}, 总耗时 {wall:.2f}s")
    print(f"拒绝响应即回即走, 上游立刻知道该退避, 而不是白等一个必败的超时")
    assert shed_n > 0 and gate.served + shed_n == jobs
    # 断言采用确定性设计: 墙钟受机器负载影响, 改为同一次运行内相对比较——
    # 被拒请求的响应必须快于任何一次真实服务 (服务至少耗时 0.05s, 拒绝不消耗服务时间)
    shed_lat = max(dt for k, dt in results if k == "SHED 503")
    served_lat = min(dt for k, dt in results if k == "200")
    assert shed_lat < served_lat, "被拒请求必须不等服务、立刻返回"


if __name__ == "__main__":
    main()
