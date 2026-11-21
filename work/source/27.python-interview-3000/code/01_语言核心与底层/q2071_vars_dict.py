"""vars 与实例 __dict__:动态增删属性与查找链的遮蔽关系。"""


class Plugin:
    version = "1.0"              # 类属性:在类的 __dict__ 里

    def __init__(self, name):
        self.name = name         # 进实例 __dict__


if __name__ == "__main__":
    p = Plugin("scanner")
    print("vars(p):", vars(p))
    print("类的 __dict__ 是只读视图:", type(Plugin.__dict__).__name__)

    p.timeout = 3.0              # 动态添加实例属性
    vars(p)["retries"] = 2       # 两个视角是同一个字典
    print("动态添加后:", vars(p))

    print("遮蔽前读到类属性:", p.version)
    p.version = "9.9-beta"       # 实例条目遮蔽类属性
    print("遮蔽后:", p.version, "| 类属性未变:", Plugin.version)
    del p.version                # 删除实例条目,重新露出类属性
    print("删除实例属性后:", p.version)

    del p.retries                # del 名字等价于删 __dict__ 条目
    print("del 后 retries 还在吗:", "retries" in vars(p))
