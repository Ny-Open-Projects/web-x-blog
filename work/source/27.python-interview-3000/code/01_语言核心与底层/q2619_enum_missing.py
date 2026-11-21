"""Enum 的 _missing_ 钩子:大小写与空白容错的按值查找。"""
import enum


class Color(enum.Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    @classmethod
    def _missing_(cls, value):
        """按值查找失败时进入这里:归一化后重试,失败返回 None。"""
        if isinstance(value, str):
            normalized = value.strip().lower()
            for member in cls:
                if member.value == normalized:
                    return member
        return None


if __name__ == "__main__":
    print("标准查找:  ", Color("red"))
    print("容错查找:  ", Color("  RED "))
    print("按名字查找: ", Color["GREEN"])

    try:
        Color("purple")
    except ValueError as exc:
        print("value 查找失败:", exc)

    try:
        Color["PURPLE"]
    except KeyError as exc:
        print("name 查找失败:", exc)
