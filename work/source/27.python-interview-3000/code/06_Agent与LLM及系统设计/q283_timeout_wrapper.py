import functools
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutTimeout

executor = ThreadPoolExecutor(max_workers=8)


def with_timeout(seconds: float) -> functools.partial:
    """装饰器:超时抛 TimeoutError,不阻塞主流程。"""
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            future = executor.submit(fn, *args, **kwargs)
            try:
                return future.result(timeout=seconds)
            except FutTimeout:
                raise TimeoutError(f"{fn.__name__} timed out after {seconds}s")
        return wrapper
    return deco


import time


@with_timeout(seconds=1.0)
def slow_call():
    time.sleep(3)
    return "done"


@with_timeout(seconds=1.0)
def fast_call():
    return "quick"


if __name__ == "__main__":
    print(fast_call())
    try:
        slow_call()
    except TimeoutError as e:
        print(e)
