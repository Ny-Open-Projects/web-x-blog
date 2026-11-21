"""命名规范的自查清单:用程序检查模块内名字的几条红线。"""
import inspect
import re

SNAKE = re.compile(r"^[a-z_][a-z0-9_]*$")
PASCAL = re.compile(r"^_?[A-Z][a-zA-Z0-9]*$")
CAMEL = re.compile(r"^[a-z]+[A-Z]")


def check_names(namespace):
    """对给定命名空间跑一遍清单,返回违规列表。"""
    problems = []
    for name, obj in sorted(namespace.items()):
        if name.startswith("__"):
            continue
        if inspect.isclass(obj):
            if not PASCAL.match(name):
                problems.append(f"类 {name}:应为 PascalCase")
        elif inspect.isfunction(obj):
            if not SNAKE.match(name):
                problems.append(f"函数 {name}:应为 snake_case")
        elif CAMEL.match(name):
            problems.append(f"变量 {name}:驼峰混用,应为 snake_case 或 UPPER")
        elif name in {"l", "O", "I"}:
            problems.append(f"变量 {name}:易与数字 1 和 0 混淆,PEP 8 禁用")
    return problems


GOOD_CONSTANT = 10
badPrivate = 1             # 变量用了驼峰:演示违规


def good_function():
    return 1


def BadFunction():
    """函数用了 PascalCase:演示违规。"""
    return 2


class GoodClass:
    pass


class badClass:
    """类名用了小写开头:演示违规。"""
    pass


if __name__ == "__main__":
    current = dict(globals())
    for problem in check_names(current):
        print("违规:", problem)
    print("清单检查完成,违规数:", len(check_names(current)))
