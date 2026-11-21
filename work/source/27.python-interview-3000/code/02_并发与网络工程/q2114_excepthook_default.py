# -*- coding: utf-8 -*-
"""threading.excepthook: 线程异常的默认行为与自定义钩子。

- 3.8 起线程异常不再杀进程, 默认由 threading.excepthook 打印到 stderr 后继续跑;
- ExceptHookArgs 携带 exc_type / exc_value / exc_traceback / thread;
- 自定义钩子把默认打印替换掉, 是崩溃埋点的唯一正门。
"""
import io
import threading
import contextlib


def boom(name):
    raise ValueError("worker %s 崩了" % name)


def default_behavior():
    buf = io.StringIO()
    t = threading.Thread(target=boom, args=("A",), name="t-A")
    with contextlib.redirect_stderr(buf):   # 捕获默认钩子的打印
        t.start()                            # 必须在捕获内启动, 否则竞态漏拍
        t.join()
    out = buf.getvalue()
    print("默认钩子打印包含异常类型:", "ValueError" in out)
    print("默认钩子打印包含线程名:", "t-A" in out)
    print("进程此刻仍然存活, 这行就是证明")


caught = []


def custom_hook(args):
    caught.append({
        "thread": args.thread.name,
        "type": args.exc_type.__name__,
        "msg": str(args.exc_value),
    })


def main():
    default_behavior()

    old = threading.excepthook
    threading.excepthook = custom_hook
    try:
        t = threading.Thread(target=boom, args=("B",), name="t-B")
        t.start()
        t.join()
    finally:
        threading.excepthook = old   # 用完恢复, 避免污染其他库
    print("自定义钩子捕获:", caught)
    print("自定义钩子生效期间默认 stderr 打印消失, 改为结构化上报")


if __name__ == "__main__":
    main()
