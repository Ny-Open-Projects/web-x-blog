"""PEP 562:模块级 __getattr__ 与懒加载"""
import sys

def __getattr__(name):
    """常规模块属性查找失败时才会被调用"""
    if name == "HEAVY":
        print("computing HEAVY lazily")
        value = sum(range(10 ** 6))
        globals()["HEAVY"] = value        # 写回模块字典:下次常规查找直接命中
        return value
    raise AttributeError(f"module has no attribute {name!r}")

def __dir__():
    return sorted(set(globals()) | {"HEAVY"})

if __name__ == "__main__":
    me = sys.modules[__name__]
    print("HEAVY in dir:", "HEAVY" in dir(me))
    print(me.HEAVY)                       # 属性访问触发模块级 __getattr__
    print(me.HEAVY)                       # 已写回:不再进钩子
    try:
        me.nope
    except AttributeError as e:
        print(e)
