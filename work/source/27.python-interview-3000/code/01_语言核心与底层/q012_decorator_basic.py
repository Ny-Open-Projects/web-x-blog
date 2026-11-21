import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        cost = time.perf_counter() - start
        print(f"{func.__name__} cost {cost:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

if __name__ == "__main__":
    slow_sum(1_000_000)
    print(slow_sum.__name__)  # slow_sum,wraps 保住了元信息
