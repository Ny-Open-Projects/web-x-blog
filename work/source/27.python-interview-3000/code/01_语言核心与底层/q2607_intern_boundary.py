"""运行时字符串驻留的边界:编译期收编,运行期不收编。"""
import sys


def f1():
    return "hello world!"


def f2():
    return "hello" + " " + "world" + "!"   # 编译期折叠成同一个常量


def make_runtime(prefix):
    return prefix + "thon"                 # 运行时拼接,不驻留


if __name__ == "__main__":
    literal = "python"
    folded = "py" + "thon"                 # 编译期折叠
    print("字面量与折叠拼接同对象:", literal is folded)          # True

    runtime = make_runtime("py")
    print("运行时拼接同对象:  ", runtime is literal)              # False
    print("sys.intern 收编后:  ", sys.intern(runtime) is literal)  # True

    joined = "".join(["py", "thon"])
    print("join 结果同对象:    ", joined is literal)              # False

    print("跨函数相同字面量同对象:", f1() is f2())                # True
    print("函数名是 intern 的:  ", sys.intern("f1") is f1.__name__)  # True
