import concurrent.futures
import threading
import time


class SingleFlight:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._inflight = {}   # key -> Future

    def run(self, key: str, fn):
        with self._lock:
            fut = self._inflight.get(key)
            if fut is not None:
                leader = False
            else:
                fut = concurrent.futures.Future()
                self._inflight[key] = fut
                leader = True
        if not leader:
            return fut.result()   # 跟随者: 等同一个结果或异常
        try:
            result = fn()
            fut.set_result(result)
            return result
        except BaseException as exc:
            fut.set_exception(exc)
            raise
        finally:
            with self._lock:
                self._inflight.pop(key, None)


def main() -> None:
    sf = SingleFlight()
    calls = {"n": 0}
    lock = threading.Lock()

    def slow_load() -> str:
        with lock:
            calls["n"] += 1
        time.sleep(0.2)               # 模拟昂贵的后端调用
        return f"payload-{calls['n']}"

    results = []
    errors = []

    def requester() -> None:
        try:
            results.append(sf.run("hot-key", slow_load))
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=requester) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len(results) == 10 and len(set(results)) == 1
    assert calls["n"] == 1, f"底层应只执行一次, 实际 {calls['n']}"
    print(f"10 个并发请求合并为 {calls['n']} 次执行, 结果一致: {results[0]}")

    # 异常也会传播给全部跟随者, 不会有人挂起
    def broken() -> None:
        raise RuntimeError("boom")
    errs = []
    threads = [threading.Thread(target=lambda: errs.append(capture(sf, "k", broken)))
               for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert all(isinstance(e, RuntimeError) for e in errs) and len(errs) == 3
    print(f"异常路径: {len(errs)} 个请求全部快速拿到异常, 无人挂起")


def capture(sf, key, fn):
    try:
        return sf.run(key, fn)
    except Exception as exc:
        return exc


if __name__ == "__main__":
    main()
