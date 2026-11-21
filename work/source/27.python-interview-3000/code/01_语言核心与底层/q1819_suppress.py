"""contextlib.suppress:精确吞异常的语义与边界。"""
import os
from contextlib import suppress


def remove_quiet(path):
    with suppress(FileNotFoundError):
        os.remove(path)
        return "已删除"
    return "文件本来就不存在"


def too_broad():
    # 反例:suppress(Exception) 连程序 bug 一起吞掉
    with suppress(Exception):
        1 / 0
        return "不会到这里"
    return "ZeroDivisionError 也被吞了"


def narrow_only():
    with suppress(KeyError):
        {}["missing"]
        return "不会到这里"
    return "只吞声明的类型"


if __name__ == "__main__":
    print(remove_quiet("/tmp/q1819_definitely_missing.bin"))
    print(too_broad())
    print(narrow_only())
