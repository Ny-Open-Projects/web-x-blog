import functools
import time

def ttl_cache(ttl=1.0, maxsize=128):
    def deco(func):
        store = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()
            hit = store.get(key)
            if hit and now - hit[0] < ttl:
                return hit[1]                 # 命中未过期
            value = func(*args, **kwargs)
            if len(store) >= maxsize:
                oldest = min(store, key=lambda k: store[k][0])
                store.pop(oldest)             # 淘汰最旧
            store[key] = (now, value)
            return value

        wrapper.cache_clear = store.clear     # 主动失效入口
        return wrapper
    return deco

CALLS = {"n": 0}

@ttl_cache(ttl=0.05)
def slow_square(x):
    CALLS["n"] += 1
    time.sleep(0.01)
    return x * x

if __name__ == "__main__":
    print(slow_square(4), slow_square(4))     # 第二次命中
    print("calls:", CALLS["n"])
    time.sleep(0.08)                          # 超过 TTL
    print(slow_square(4))
    print("calls after ttl:", CALLS["n"])
