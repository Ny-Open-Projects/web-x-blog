def inner():
    total = 0
    while True:
        got = yield total        # 收到 send 的值,返回累计
        if got is None:
            return total         # return 值交给 yield from
        total += got

def outer():
    result = yield from inner()  # 委托给子生成器
    yield f"inner returned {result}"

if __name__ == "__main__":
    g = outer()
    print(next(g))       # 0,驱动到 inner 的 yield
    print(g.send(10))    # 10,直接写入 inner
    print(g.send(32))    # 42
    try:
        g.send(None)     # 结束 inner
    except StopIteration:
        pass
