"""生成器 send 的启动契约:先 next 后 send,以及状态机观测。"""
import inspect


def echo():
    total = 0
    while True:
        got = yield total          # 首次推进到 yield 才会停在这里
        total += got


def primed(gen):
    """预激:推进到第一个 yield,调用方即可直接 send。"""
    next(gen)
    return gen


if __name__ == "__main__":
    g = echo()
    print("刚创建:", inspect.getgeneratorstate(g))
    try:
        g.send(10)                 # 未启动就 send 非 None
    except TypeError as e:
        print("启动前 send 报错:", e)

    print("send(None) 等价 next,启动并返回:", g.send(None))
    print("启动后:", inspect.getgeneratorstate(g))
    print("send(10):", g.send(10), "| send(32):", g.send(32))

    h = primed(echo())
    print("预激后直接 send(7):", h.send(7))
    h.close()
    print("close 后:", inspect.getgeneratorstate(h))
