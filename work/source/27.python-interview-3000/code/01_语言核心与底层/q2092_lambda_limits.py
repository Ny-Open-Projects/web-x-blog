"""lambda 的边界:语句、递归、注解与调试名的缺失。"""
import traceback


def fib_def(n):
    """def 有名字:可递归、可写 docstring 与注解。"""
    return n if n < 2 else fib_def(n - 1) + fib_def(n - 2)


def boom():
    raise ValueError("deep error")


if __name__ == "__main__":
    square = lambda x: x * x
    print("单表达式可用:", square(6))
    print("调试名缺失:", square.__name__, "| def 有名:", fib_def.__name__)
    print("def 递归:", fib_def(10))

    caller = lambda: boom()
    try:
        caller()
    except ValueError:
        tb = traceback.format_exc()
        print("栈帧里只显示 <lambda>:", "<lambda>" in tb)

    print("结论:要语句、递归、注解、docstring 或清晰栈帧时,用 def")
