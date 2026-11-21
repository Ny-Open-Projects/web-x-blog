import functools
import random
import time

def retry(times=3, base_delay=0.01, exceptions=(Exception,), jitter=True):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == times:
                        raise                       # 耗尽:保留原始异常
                    delay = base_delay * (2 ** (attempt - 1))
                    if jitter:
                        delay *= random.uniform(0.5, 1.5)
                    print(f"attempt {attempt} failed: {exc}, retry in {delay:.3f}s")
                    time.sleep(delay)
        return wrapper
    return deco

CALLS = {"n": 0}

@retry(times=4, base_delay=0.01, exceptions=(ConnectionError,))
def flaky_fetch(url):
    CALLS["n"] += 1
    if CALLS["n"] < 3:
        raise ConnectionError(f"timeout on {url}")
    return f"data from {url}"

if __name__ == "__main__":
    print(flaky_fetch("https://example.com/api"))
    print("total calls:", CALLS["n"])
