import sys
from collections import Counter


def inner_a():
    return 1


def inner_b():
    return inner_a() + inner_a()


def outer():
    return inner_b() + inner_a()


if __name__ == "__main__":
    calls = Counter()

    def profiler(frame, event, arg):
        if event == "call":
            calls[frame.f_code.co_name] += 1

    sys.setprofile(profiler)
    try:
        outer()
    finally:
        sys.setprofile(None)               # 探针必须拆除,否则全局减速
    print("call counts:", dict(calls))
    print("c_call 事件同样存在,cProfile 因此能统计内置函数")
