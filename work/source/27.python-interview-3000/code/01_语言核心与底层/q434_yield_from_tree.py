def leaf(name):
    total = 0
    for _ in range(2):
        got = yield f"{name}-value"
        total += got or 0
    return f"{name} total={total}"        # return 值经 StopIteration.value 上浮

def middle():
    result = yield from leaf("A")         # 委托:转发 next/send/throw
    print("middle got:", result)
    result = yield from leaf("B")
    return result

if __name__ == "__main__":
    g = middle()
    print(next(g))                        # A-value
    print(g.send(1))                      # A-value
    print(g.send(2))                      # A 结束返回,委托切到 B:B-value
    print(g.send(3))                      # B-value
    try:
        g.send(4)
    except StopIteration as stop:
        print("final result:", stop.value)    # B total=7
