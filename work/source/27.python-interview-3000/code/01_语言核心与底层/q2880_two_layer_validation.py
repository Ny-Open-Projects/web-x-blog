"""类型注解与运行时校验的双层设计:静态层管全程,运行层只守边界。"""
import timeit
from typing import get_type_hints


def create_user(name: str, age: int) -> dict:
    """内部函数:只靠注解给静态检查,不做任何运行时检查。"""
    return {"name": name.title(), "age": age, "adult": age >= 18}


def validate_call(func, *args):
    """边界校验器:入口处按注解做一次运行时检查,再放行。"""
    hints = get_type_hints(func)
    param_names = func.__code__.co_varnames[:func.__code__.co_argcount]
    for value, pname in zip(args, param_names):
        expected = hints.get(pname)
        if expected is not None and not isinstance(value, expected):
            raise TypeError(f"参数 {pname} 期望 {expected.__name__},实际 {type(value).__name__}")
    return func(*args)


if __name__ == "__main__":
    print("合法调用:", validate_call(create_user, "alice", 30))

    try:
        validate_call(create_user, "bob", "30")
    except TypeError as e:
        print("边界拦截:", e)

    # 内部调用路径不做校验:正确性交给静态检查,性能留给运行时
    cost_checked = timeit.timeit(lambda: validate_call(create_user, "alice", 30), number=20000)
    cost_plain = timeit.timeit(lambda: create_user("alice", 30), number=20000)
    print(f"2 万次:带校验 {cost_checked:.3f}s vs 纯调用 {cost_plain:.3f}s")
    print("结论:校验只放在边界,内部调用保持零开销")
