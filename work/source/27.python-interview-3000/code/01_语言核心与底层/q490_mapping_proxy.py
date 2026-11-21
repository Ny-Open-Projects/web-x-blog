import types

class Registry:
    _data = {"a": 1}
    PUBLIC = types.MappingProxyType(_data)   # 活的只读视图

if __name__ == "__main__":
    view = Registry.PUBLIC
    print(view["a"])
    try:
        view["b"] = 2
    except TypeError as e:
        print("read-only:", e)
    Registry._data["b"] = 2                  # 内部仍可写
    print("view follows updates:", view["b"])
    print("underlying type:", type(view).__name__)
    print("still shallow: values can be mutable containers")
