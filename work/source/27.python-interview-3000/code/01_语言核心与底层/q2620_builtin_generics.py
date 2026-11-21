"""3.9 的内置泛型:PEP 585 的运行时形态、拆解与边界。"""
import types
import typing


def mean(values: list[float]) -> float:      # 3.9 合法注解
    return sum(values) / len(values)


if __name__ == "__main__":
    alias = list[int]
    print("list[int] 类型:", type(alias), isinstance(alias, types.GenericAlias))
    print("拆解:", typing.get_origin(alias), typing.get_args(alias))
    print("dict[str, int]:", dict[str, int])
    print("tuple[int, ...]:", tuple[int, ...])

    print("mean([1, 2, 3]):", mean([1.0, 2.0, 3.0]))

    try:
        str[int]
    except TypeError as exc:
        print("str 不可参数化:", exc)

    try:
        isinstance([], list[int])
    except TypeError as exc:
        print("isinstance 拒绝参数化泛型:", exc)
