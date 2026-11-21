"""namedtuple 的工程用法:defaults、_replace、_asdict 与字段演进。"""
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"], defaults=[0, 0])
Host = namedtuple("Host", "host port timeout", defaults=[None, 3.0])

if __name__ == "__main__":
    print("defaults 补齐:", Point())
    print("按位与关键字混合:", Host("db2", port=5432))

    h = Host("db1")
    h2 = h._replace(timeout=10.0)
    print("原对象:", h, "| 替换后:", h2, "| 是新对象:", h2 is not h)

    print("字段名:", Host._fields)
    print("转字典:", h._asdict())

    HostV2 = namedtuple("Host", Host._fields + ("weight",), defaults=(None, 3.0, 1.0))
    print("V2 兼容旧构造:", HostV2("db3", 6379))
