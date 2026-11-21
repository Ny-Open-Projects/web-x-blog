"""get_origin 与 get_args:把泛型别名拆回裸类型与参数。"""
import typing
from typing import Dict, List, Union, get_args, get_origin


def check_str_list(obj):
    """运行时校验 obj 是 list 且元素都是 str,不使用参数化泛型 isinstance。"""
    origin = get_origin(List[str])            # list
    if not isinstance(obj, origin):
        return False
    return all(isinstance(item, str) for item in obj)


if __name__ == "__main__":
    print("origin List[int]:", get_origin(List[int]))          # list
    print("args   List[int]:", get_args(List[int]))            # (int,)
    print("origin Dict[str, int]:", get_origin(Dict[str, int]))
    print("args   Dict[str, int]:", get_args(Dict[str, int]))
    print("origin Union[str, int]:", get_origin(Union[str, int]))
    print("args   Union[str, int]:", get_args(Union[str, int]))

    print("内置泛型 list[int]:", list[int], get_args(list[int]))

    try:
        isinstance([], List[int])
    except TypeError as exc:
        print("参数化泛型 isinstance 被拒:", exc)

    print("check_str_list(['a', 1]):", check_str_list(["a", 1]))
    print("check_str_list(['a', 'b']):", check_str_list(["a", "b"]))
