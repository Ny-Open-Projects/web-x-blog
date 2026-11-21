from __future__ import annotations

import functools
import inspect

try:
    from typing import Callable, ParamSpec, TypeVar
    P = ParamSpec("P")
    R = TypeVar("R")
    HAS_PARAMSPEC = True
except ImportError:                      # 3.9:typing.ParamSpec 尚不存在
    from typing import Callable, TypeVar
    P = None
    R = TypeVar("R")
    HAS_PARAMSPEC = False


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logged
def add(a: int, b: int = 0) -> int:
    return a + b


if __name__ == "__main__":
    print("HAS_PARAMSPEC:", HAS_PARAMSPEC)
    print("runtime signature preserved:", inspect.signature(add))
    print("name preserved:", add.__name__, "| call:", add(2, b=3))
    if HAS_PARAMSPEC:
        print("静态层: func: Callable[P, R] -> Callable[P, R]")
    else:
        print("3.9 请用 TypeVar bound=Callable 的恒等式写法, 见 q1270")
