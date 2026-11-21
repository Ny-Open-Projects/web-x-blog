import sys


def inner():
    return sys._getframe(1)          # 拿到调用者的帧


def outer():
    caller = inner()
    n, f = 0, sys._getframe()
    while f is not None:             # 沿 f_back 数这条 Python 栈
        n += 1
        f = f.f_back
    return caller.f_code.co_name, caller.f_lineno, sorted(caller.f_locals), n


def raise_deep():
    raise ValueError("boom")


def catch_and_clear():
    try:
        raise_deep()
    except ValueError:
        tb = sys.exc_info()[2]
        current = sys._getframe()
        cleared = 0
        while tb is not None:
            if tb.tb_frame is not current:   # 正在执行的帧不能 clear
                tb.tb_frame.clear()          # 释放 traceback 钉住的局部变量
                cleared += 1
            tb = tb.tb_next
        return cleared


if __name__ == "__main__":
    name, line, locals_, depth = outer()
    print("caller:", name, "at line", line)
    print("caller locals:", locals_)
    print("python stack depth:", depth)
    print("cleared non-current frames:", catch_and_clear())
