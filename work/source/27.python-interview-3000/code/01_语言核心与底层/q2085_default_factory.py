"""默认参数的工厂惯用法:None 哨兵 + 调用时创建。"""
from dataclasses import dataclass, field
from datetime import datetime


def append_to(item, bucket=None):
    """未传入容器时每次新建,而不是共享同一个。"""
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


def tag_now(timestamp=None):
    """None 表示用当前时刻:调用时求值,而非 def 时。"""
    return timestamp if timestamp is not None else datetime.now()


@dataclass
class Cart:
    items: list = field(default_factory=list)   # dataclass 的声明式同款


if __name__ == "__main__":
    print(append_to("a"), "|", append_to("b"))          # 两个独立列表
    shared = [1]
    print("显式传入则复用:", append_to(2, shared))

    print("可注入固定时间:", tag_now(datetime(2026, 1, 1)))
    print("缺省取当前:", tag_now().year)

    c1, c2 = Cart(), Cart()
    c1.items.append("book")
    print("default_factory 隔离:", c1.items, c2.items)
