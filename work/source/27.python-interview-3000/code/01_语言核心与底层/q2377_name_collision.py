"""变量名冲突的常见来源:builtins、循环变量、import 与模块名。"""


def demo_builtin():
    """模块级 sum 遮蔽了内置 sum。"""
    print("  此时 sum =", sum)
    return None


sum = 100        # 冲突一:遮蔽 builtins.sum


def demo_loop_leak():
    for i in range(3):
        pass
    return i      # 循环变量泄漏


if __name__ == "__main__":
    demo_builtin()
    del sum
    print("del 后 sum 恢复内置:", sum([1, 2], 10))

    print("循环变量泄漏到函数级:", demo_loop_leak())

    import math

    def shadowed():
        math = 42           # 冲突二:局部遮蔽模块
        return math

    print("函数内 math 被遮蔽:", shadowed())
    print("模块级 math 正常:", math.sqrt(16))

    string = "我是字符串,不是 string 模块"   # 冲突三:与模块名撞车
    print(string)

    import builtins
    risky = [n for n in ("sum", "min", "max", "list", "id", "type")
             if hasattr(builtins, n)]
    print("高危内置名:", risky)
