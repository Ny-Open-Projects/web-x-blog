"""sys.intern 驻留控制与 __new__ 规范化对象池。"""
import sys

TOKEN_BYTES = [b"GET", b"POST", b"PUT", b"DELETE"]


def make_tokens(n):
    """bytes.decode 每次都产生值相等但身份不同的新字符串。"""
    return [TOKEN_BYTES[i % 4].decode("ascii") for i in range(n)]


class Color:
    """规范化对象池:同参数永远返回同一实例。"""
    _pool = {}

    def __new__(cls, name):
        obj = cls._pool.get(name)
        if obj is None:
            obj = super().__new__(cls)
            obj.name = name
            cls._pool[name] = obj
        return obj


if __name__ == "__main__":
    tokens = make_tokens(20000)
    unique_ids = len({id(t) for t in tokens})
    interned = [sys.intern(t) for t in tokens]
    unique_after = len({id(t) for t in interned})
    print("驻留前不同对象数:", unique_ids, "| 驻留后:", unique_after)
    print("intern 不改值只改身份:", tokens[0] == interned[0], tokens[0] is not interned[0])

    a, b = Color("red"), Color("red")
    print("对象池同参同实例:", a is b, "| 不同参数不同实例:", Color("blue") is not a)
    print("池的代价:状态被共享,且池持强引用,要有上限与淘汰策略")
