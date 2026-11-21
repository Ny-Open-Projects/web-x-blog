import functools
import inspect

def deco_no_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def deco_with_wraps(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@deco_no_wraps
def f1():
    """doc of f1"""

@deco_with_wraps
def f2():
    """doc of f2"""

if __name__ == "__main__":
    print(f1.__name__, "|", f1.__doc__)  # wrapper | None
    print(f2.__name__, "|", f2.__doc__)  # f2 | doc of f2
    print(inspect.signature(f2))         # 还原真实签名
