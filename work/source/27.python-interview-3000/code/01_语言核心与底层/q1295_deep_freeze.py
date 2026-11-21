from types import MappingProxyType


def deep_freeze(obj):
    if isinstance(obj, dict):
        return MappingProxyType({k: deep_freeze(v) for k, v in obj.items()})
    if isinstance(obj, (list, tuple)):
        return tuple(deep_freeze(x) for x in obj)
    if isinstance(obj, set):
        return frozenset(obj)
    return obj


if __name__ == "__main__":
    raw = {"name": "svc", "tags": ["a", "b"],
           "limits": {"cpu": 2, "hosts": ["h1", "h2"]}}
    frozen = deep_freeze(raw)
    raw["limits"]["cpu"] = 99            # 冻结发生在拷贝后,原始可变不影响结果
    print("frozen untouched:", frozen["limits"]["cpu"])
    try:
        frozen["name"] = "x"
    except TypeError as e:
        print("top level ->", type(e).__name__)
    try:
        frozen["limits"]["cpu"] = 1
    except TypeError as e:
        print("nested level ->", type(e).__name__)
