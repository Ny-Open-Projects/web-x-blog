from __future__ import annotations

import functools
import inspect
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable[..., object])   # 流派一:恒等透传


def log_calls(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@log_calls
def greet(name: str, punct: str = "!") -> str:
    return "hi " + name + punct


if __name__ == "__main__":
    print("runtime signature:", inspect.signature(greet))
    print(greet("lily"))
    print("流派二 ParamSpec 见 q1267;流派三 @overload 适合返回类型随参数变化的注册器")
