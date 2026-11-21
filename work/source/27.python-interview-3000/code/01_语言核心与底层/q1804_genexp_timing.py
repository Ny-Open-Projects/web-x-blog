"""生成器表达式的求值时机:外层立即、内层惰性。"""


def outermost_eager():
    log = []

    def source():
        log.append("source evaluated")
        return iter([1, 2, 3])

    gen = (x * 10 for x in source())   # source() 在定义这一行就已执行
    return log, next(gen)


def body_lazy():
    log = []

    def double(v):
        log.append("double " + str(v))
        return v * 2

    gen = (double(x) for x in [1, 2])
    before = list(log)
    return before, list(gen), list(log)  # 消费前函数体未跑


def filter_late_binding():
    n = 10
    gen = (x for x in range(100) if x < n)  # if 里的 n 消费时才查外层
    n = 0                                   # 消费前改外层变量会生效
    return list(gen)


if __name__ == "__main__":
    log, first = outermost_eager()
    print("定义后 source 已执行:", log, "| 首个产出:", first)
    before, values, after = body_lazy()
    print("消费前:", before, "| 消费后:", after)
    print("if 引用的外层变量实时生效:", filter_late_binding())
