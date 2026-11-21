"""裸 raise 与 raise e 的差异:traceback 是否被加长。"""
import sys
import traceback


def level1():
    raise ValueError("root")


def middle_bare():
    try:
        level1()
    except ValueError:
        raise                      # 原样上抛:traceback 不变


def middle_rexpr():
    try:
        level1()
    except ValueError as e:
        raise e                    # 同一对象,但重抛点被追加进栈


def count_frames(func, exc_type):
    try:
        func()
    except exc_type:
        return len(traceback.extract_tb(sys.exc_info()[2]))


if __name__ == "__main__":
    n_bare = count_frames(middle_bare, ValueError)
    n_rexpr = count_frames(middle_rexpr, ValueError)
    print("裸 raise 帧数:", n_bare, "| raise e 帧数:", n_rexpr)
    print("差值就是重抛点那一帧,指向的是同一个异常对象")

    try:
        middle_rexpr()
    except ValueError as e:
        print("异常消息保真:", str(e))
    print("纯透传用裸 raise;跨层包装语义才用 raise NewError from e")
