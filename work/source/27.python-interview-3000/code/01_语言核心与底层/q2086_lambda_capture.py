"""lambda 捕获循环变量:late binding 的三种解法。"""
import functools


def naive():
    return [lambda: i for i in range(3)]           # 全部看到最终的 i


def fix_default():
    return [lambda i=i: i for i in range(3)]       # 解法一:默认参数定义时绑定


def fix_partial():
    return [functools.partial(lambda v: v, i) for i in range(3)]   # 解法二:固化实参


def fix_factory():
    def make(v):
        return lambda: v
    return [make(i) for i in range(3)]             # 解法三:工厂制造独立作用域


if __name__ == "__main__":
    for name, builder in [("天真写法", naive), ("默认参数", fix_default),
                          ("partial", fix_partial), ("工厂闭包", fix_factory)]:
        print(f"{name}: {[cb() for cb in builder()]}")
