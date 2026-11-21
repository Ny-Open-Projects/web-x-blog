

def make_scaler(factor):
    """默认参数固化:定义时把 factor 快照进默认值。"""
    def scale(x, _factor=factor):
        return x * _factor
    return scale


def make_handlers_bad():
    """反例:闭包引用循环变量,所有 handler 共享最终值。"""
    handlers = []
    for name in ("read", "write", "admin"):
        handlers.append(lambda: "allowed:" + name)    # late binding
    return handlers


def make_handlers_good():
    """正解:默认参数固化每轮迭代的 name。"""
    handlers = []
    for name in ("read", "write", "admin"):
        handlers.append(lambda n=name: "allowed:" + n)
    return handlers


def make_counter(start=0):
    """闭包状态工厂:nonlocal 让内层函数持有可变状态。"""
    count = start
    def bump(step=1):
        nonlocal count
        count += step
        return count
    return bump


if __name__ == "__main__":
    double = make_scaler(2)
    triple = make_scaler(3)
    print("scale:", double(10), triple(10))
    print("same code, distinct defaults:",
          double.__defaults__, triple.__defaults__)

    for h in make_handlers_bad():
        print("bad :", h())
    for h in make_handlers_good():
        print("good:", h())

    tick = make_counter()
    print("counter:", tick(), tick(5), tick())
