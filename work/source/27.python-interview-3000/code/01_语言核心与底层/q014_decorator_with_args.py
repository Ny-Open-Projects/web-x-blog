import functools
import random
import time

def retry(times, delay=0.1, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"attempt {attempt} failed: {e}")
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(times=3, exceptions=(ValueError,))
def flaky():
    if random.random() < 0.7:
        raise ValueError("boom")
    return "ok"

if __name__ == "__main__":
    random.seed(42)
    try:
        print("flaky() =", flaky())
    except ValueError:
        print("flaky() 重试 3 次后仍失败——装饰器把最后一次异常抛给调用方(演示预期)")
