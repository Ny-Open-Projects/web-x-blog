import functools
import inspect

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"log: calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"log: {func.__name__} returned {result}")
        return result
    return wrapper

def double_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@log_calls
@double_result
def add(a, b=1):
    """add two numbers"""
    return a + b

if __name__ == "__main__":
    print(add(1, 2))                      # log 先执行,double 先算
    print(add.__name__, add.__doc__)      # wraps 保留的元信息
    print(inspect.signature(add))         # (a, b=1):沿 __wrapped__ 链还原
    f = add
    while hasattr(f, "__wrapped__"):
        f = f.__wrapped__
    print("unwrapped to original:", f is not None)
    print(inspect.unwrap(add) is not None)
