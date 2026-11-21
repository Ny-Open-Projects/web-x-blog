class Root:
    def ping(self):
        print("Root.ping")

class Left(Root):
    def ping(self):
        print("Left.ping")
        super().ping()     # MRO 上的下一个,可能是兄弟类

class Right(Root):
    def ping(self):
        print("Right.ping")
        super().ping()

class Child(Left, Right):
    def ping(self):
        print("Child.ping")
        super().ping()

if __name__ == "__main__":
    Child().ping()
    # Child -> Left -> Right -> Root,Left 的 super 调到了兄弟 Right
    print(Child.__mro__)

    # 故意演示「直接写父类名」的重复初始化问题
    class Counter:
        instances = 0
        def __init__(self):
            Counter.instances += 1
    class L(Counter):
        def __init__(self):
            Counter.__init__(self)
    class R(Counter):
        def __init__(self):
            Counter.__init__(self)
    class Bad(L, R):
        def __init__(self):
            L.__init__(self)
            R.__init__(self)
    _ = Bad()
    print("Counter initialized:", Counter.instances, "times,应为 1")
