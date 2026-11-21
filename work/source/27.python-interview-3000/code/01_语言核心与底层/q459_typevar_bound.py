from typing import TypeVar, List

AnyStr2 = TypeVar("AnyStr2", str, bytes)     # constrained:只能是这几个
NumberT = TypeVar("NumberT", bound=float)    # bound:上界,可为子类

def concat(a: AnyStr2, b: AnyStr2) -> AnyStr2:
    """constrained:同一次调用中两个参数必须同类型"""
    return a + b

def scale_all(items: List[NumberT], factor: float) -> List[NumberT]:
    """bound:输入是什么类型,返回就保持什么类型"""
    return [x * factor for x in items]

if __name__ == "__main__":
    print(concat("a", "b"), concat(b"x", b"y"))
    print(scale_all([1.5, 2.5], 2.0))
    print(scale_all.__annotations__)
    # concat("a", b"b") 在 mypy 下报错:同一个 TypeVar 求解出两个冲突类型
