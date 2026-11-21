import concurrent.futures
import threading
import time


class AllStagesFailed(Exception):
    pass


class FallbackChain:
    def __init__(self, stages) -> None:
        self._stages = stages          # (名字, 取数函数, 超时秒)
        self.served_by = {}

    def fetch(self, key: str):
        errors = []
        for name, fn, timeout in self._stages:
            start = time.monotonic()
            try:
                value = self._call_with_timeout(fn, key, timeout)
                self.served_by[name] = self.served_by.get(name, 0) + 1
                return value, name
            except Exception as exc:
                errors.append(f"{name}[{type(exc).__name__}@"
                              f"{(time.monotonic()-start)*1000:.0f}ms]")
        raise AllStagesFailed(" -> ".join(errors))

    @staticmethod
    def _call_with_timeout(fn, key: str, timeout: float):
        if timeout is None:
            return fn(key)
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
            return ex.submit(fn, key).result(timeout=timeout)


def main() -> None:
    cache = {"item-9": '{"name":"stale-item","price":99}'}
    default_value = '{"items":[],"hint":"degraded"}'

    def primary(key: str) -> str:
        time.sleep(0.5)                # 主服务卡死
        return "live"

    def replica(key: str) -> str:
        raise ConnectionError("副本也挂了")

    def cache_get(key: str) -> str:
        if key in cache:
            return cache[key]
        raise KeyError(key)

    def default(key: str) -> str:
        return default_value

    chain = FallbackChain([
        ("primary", primary, 0.1),
        ("replica", replica, 0.1),
        ("cache", cache_get, None),
        ("default", default, None),
    ])

    v, src = chain.fetch("item-9")
    print(f"场景一 主卡死+副本挂: {src} 返回 {v[:28]}...")
    assert src == "cache"

    v, src = chain.fetch("no-such-key")
    print(f"场景二 缓存也没有:   {src} 返回 {v[:24]}...")
    assert src == "default"

    try:
        chain.fetch("item-9") if False else None
        chain2 = FallbackChain([("a", lambda k: (_ for _ in ()).throw(OSError("x")), 0.05),
                                ("b", lambda k: (_ for _ in ()).throw(OSError("x")), 0.05)])
        chain2.fetch("k")
    except AllStagesFailed as exc:
        print(f"场景三 全链失败:     {exc}")
    print(f"各级命中统计: {chain.served_by}")


if __name__ == "__main__":
    main()
