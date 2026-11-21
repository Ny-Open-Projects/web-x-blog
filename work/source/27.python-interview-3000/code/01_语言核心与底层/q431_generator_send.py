def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average          # send 进来的值成为这个表达式的值
        total += term
        count += 1
        average = total / count

if __name__ == "__main__":
    avg = averager()
    first = next(avg)                 # 预激:推进到第一个 yield,得到 None
    print("first yield:", first)
    print(avg.send(10))               # 10.0
    print(avg.send(20))               # 15.0
    print(avg.send(30))               # 20.0

    fresh = averager()
    try:
        fresh.send(1)                 # 未预激就 send 非空值
    except TypeError as e:
        print("must prime first:", e)
