def worker():
    try:
        while True:
            item = yield "ready"
            print("got", item)
    except ValueError as e:
        print("injected:", e)
        yield "recovered"             # 捕获后还能吐出新值继续用
    finally:
        print("cleanup in finally")

if __name__ == "__main__":
    g = worker()
    print(next(g))                          # 预激,得到 ready
    print(g.throw(ValueError("boom")))      # 在 yield 处注入,生成器捕获后返回 recovered
    try:
        g.send("hello")                     # recovered 之后的 yield 没有:except 块结束进 finally
    except StopIteration:
        print("finally ran, generator finished")

    g2 = worker()
    next(g2)
    g2.close()                              # 注入 GeneratorExit,只走 finally
    print("closed cleanly")
