"""可变默认参数的替代方案:None 哨兵、不可变收编与有意共享。"""
import dataclasses


def add_tag(item, tags=None):
    """方案一:None 哨兵 + 体内新建;list(tags) 顺带防御外部共享引用。"""
    tags = [] if tags is None else list(tags)
    tags.append("new")
    return item, tags


def collect_point(x, y, seen=()):
    """方案二:不可变序列当默认值,天然无跨调用副作用。"""
    return x + y, seen


@dataclasses.dataclass
class Cart:
    """方案三:dataclass 的 default_factory,每实例新建。"""
    items: list = dataclasses.field(default_factory=list)
    meta: dict = dataclasses.field(default_factory=dict)


def registry_default(box, _registry={}):
    """反例转正用:刻意利用共享默认值做进程内登记,必须注释声明意图。"""
    _registry[box] = box
    return _registry


if __name__ == "__main__":
    _, ta = add_tag("apple")
    _, tb = add_tag("pear")
    print("两次调用互不影响:", ta, tb)

    shared = ["x"]
    _, t1 = add_tag("a", shared)
    print("外部列表未被污染:", shared, "| 返回的是副本:", t1)

    print("不可变默认值:", collect_point(1, 2, seen=("keep",)))

    cart = Cart()
    cart.items.append("book")
    other = Cart()
    print("default_factory 每实例新建:", cart.items, other.items)

    registry_default("first")
    print("有意共享的登记表:", list(registry_default("second").values()))
