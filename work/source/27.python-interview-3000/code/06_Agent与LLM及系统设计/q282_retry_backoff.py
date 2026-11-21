import functools
import random
import time
from typing import Callable


def retry(times: int = 3, base_delay: float = 0.1,
          exceptions: tuple = (TimeoutError,)) -> Callable:
    def deco(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except exceptions:
                    if attempt == times:
                        raise  # 用尽后抛出原始异常
                    # 指数退避 + 抖动
                    delay = base_delay * (2 ** (attempt - 1))
                    delay = random.uniform(0, delay * 2)
                    print(f"retry {attempt}, sleep {delay:.2f}s")
                    time.sleep(delay)
        return wrapper
    return deco


_call_count = 0


@retry(times=3, base_delay=0.05)
def flaky_api() -> str:
    global _call_count
    _call_count += 1
    if _call_count < 3:
        raise TimeoutError("simulated timeout")
    return "ok"


if __name__ == "__main__":
    print(flaky_api())
