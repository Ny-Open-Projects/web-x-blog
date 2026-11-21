from typing import overload

@overload
def parse(value: str) -> list:
    """字符串:按逗号拆分为列表"""

@overload
def parse(value: int) -> str:
    """整数:格式化为编号"""

def parse(value):
    """运行时唯一存在的实现"""
    if isinstance(value, str):
        return value.split(",")
    if isinstance(value, int):
        return f"code-{value}"
    raise TypeError(f"unsupported: {type(value).__name__}")

if __name__ == "__main__":
    print(parse("a,b,c"))
    print(parse(7))
    try:
        parse(1.5)
    except TypeError as e:
        print("runtime rejects:", e)
    print("overloads are invisible at runtime:", parse.__name__)
