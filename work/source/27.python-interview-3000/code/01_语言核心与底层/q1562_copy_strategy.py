import copy
from types import MappingProxyType

INNER = {"env": "prod", "flags": ["a", "b"]}
STATE = {"inner": INNER, "id": 7}


if __name__ == "__main__":
    # 1. 浅拷贝:容器断开,嵌套的 list 仍共享
    shallow = dict(STATE)
    shallow["inner"]["flags"].append("SHALLOW")
    print("shallow leaks deep :", STATE["inner"]["flags"])

    # 2. 深拷贝:全断开
    deep = copy.deepcopy(STATE)
    deep["inner"]["flags"].append("DEEP")
    print("deep is isolated   :", STATE["inner"]["flags"])

    # 3. 只读视图:防写,但底层更新实时可见
    proxy = MappingProxyType(STATE["inner"])
    print("proxy read         :", proxy["env"])
    try:
        proxy["env"] = "dev"
    except TypeError:
        print("proxy write        : TypeError")
    STATE["inner"]["flags"].append("live")
    print("proxy sees updates :", list(proxy["flags"]))

    # 4. 不可变转换:tuple 化后可作缓存 key
    key = (STATE["id"], tuple(STATE["inner"]["flags"]))
    cache = {key: "v1"}
    print("immutable key works:", cache[(7, ("a", "b", "SHALLOW", "live"))])
