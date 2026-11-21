import importlib.abc
import sys

BANNED = {"this"}          # 以 this 模块为例:策略禁止导入

class Blocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        root = fullname.split(".")[0]
        if root in BANNED:
            raise ImportError(f"{root} is banned by policy")
        return None                      # 放行:交给后续 finder

if __name__ == "__main__":
    sys.meta_path.insert(0, Blocker())
    import json                          # 正常模块不受影响
    print("json ok")
    try:
        import this                      # 被 finder 拦截
    except ImportError as e:
        print("blocked:", e)
    sys.meta_path.pop(0)
    print("finder removed")
