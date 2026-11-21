"""保存异常对象会钉住整条帧链的局部变量。"""
import gc
import weakref


class Payload:
    pass


def failing():
    payload = Payload()                 # 大对象,本函数结束后应可回收
    marker = weakref.ref(payload)
    try:
        raise ValueError("boom")
    except ValueError as exc:
        return exc, marker


if __name__ == "__main__":
    exc, marker = failing()
    gc.collect()
    print("异常对象活着时,帧内 payload 仍被钉住:", marker() is not None)

    exc.__traceback__ = None            # 掐断帧链
    gc.collect()
    print("掐断 __traceback__ 后回收:", marker() is None)

    # 对照:保存提炼信息才是长存姿势
    exc2, marker2 = failing()
    brief = f"{type(exc2).__name__}: {exc2}"
    del exc2
    gc.collect()
    print("只存摘要后可回收:", marker2() is None, "| 摘要:", brief)
