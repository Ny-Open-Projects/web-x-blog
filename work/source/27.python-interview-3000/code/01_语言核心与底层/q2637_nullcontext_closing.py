"""nullcontext 占位与 closing 收尾:控制流归一。"""
import contextlib


class OldHandle:
    """有 close 但不是上下文管理器的老式对象。"""

    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True
        print("    OldHandle.close 被调用")


def work(lock):
    """lock 可为 None:nullcontext 统一分支。"""
    with contextlib.nullcontext() if lock is None else lock:
        return "done"


def use_handle():
    with contextlib.closing(OldHandle()) as h:
        return h


if __name__ == "__main__":
    print("带锁:", work(contextlib.nullcontext()))
    print("无锁:", work(None))

    h = use_handle()
    print("退出 with 后 closed =", h.closed)

    with contextlib.nullcontext(42) as v:
        print("nullcontext 带值:", v)
