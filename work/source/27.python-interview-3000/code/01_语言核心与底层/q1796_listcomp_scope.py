"""列表推导的独立作用域:2.x 泄漏史与外层求值规则。"""


def loop_leak():
    for n in [1, 2, 3]:
        pass
    return n  # for 循环变量留在函数作用域;Python2 的推导式也这样泄漏


def comp_scope():
    n = "outer"
    squares = [n * n for n in [1, 2, 3]]  # 推导式有独立作用域,不改写外层 n
    return squares, n


def outermost_immediate():
    calls = []

    def iterable():
        calls.append("evaluated")
        return [1, 2]

    gen = (x for x in iterable())  # 定义这一行 iterable() 就已执行
    return calls, list(gen)        # 内层消费才驱动生成


def early_type_error():
    try:
        return [x for x in 123]    # 最外层 iterable 立即求值,当场 TypeError
    except TypeError as e:
        return type(e).__name__


if __name__ == "__main__":
    print("for 循环泄漏的 n:", loop_leak())
    squares, n = comp_scope()
    print("推导式结果:", squares, "外层 n 未被污染:", n)
    calls, values = outermost_immediate()
    print("定义时 iterable 已执行:", calls, "消费时产出:", values)
    print("坏 iterable 的报错时机:", early_type_error())
