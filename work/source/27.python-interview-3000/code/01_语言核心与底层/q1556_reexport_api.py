import importlib
import sys
import types
import warnings


def build_package():
    """在 sys.modules 里搭一个迷你包:impl 模块 + 门面模块。"""
    impl = types.ModuleType("demopkg.impl")

    def public_tool(n):
        return n * 2

    def _hidden_helper(n):
        return n + 1

    impl.public_tool = public_tool
    impl._hidden_helper = _hidden_helper
    sys.modules["demopkg.impl"] = impl

    facade = types.ModuleType("demopkg")
    from demopkg.impl import public_tool as public_tool   # as 同名 = 公共 API
    facade.public_tool = public_tool
    facade.__all__ = ["public_tool"]

    def __getattr__(name):
        """弃用转接:旧名字打警告后转发。"""
        if name == "old_tool":
            warnings.warn("old_tool 已弃用, 请用 public_tool",
                          DeprecationWarning, stacklevel=2)
            return public_tool
        raise AttributeError(name)

    facade.__getattr__ = __getattr__
    sys.modules["demopkg"] = facade
    return facade


if __name__ == "__main__":
    pkg = build_package()

    star = {}
    exec("from demopkg import *", star)      # __all__ 收敛 star-import 面
    print("star import sees:",
          sorted(k for k in star if not k.startswith("__")))

    tool = importlib.import_module("demopkg").public_tool
    print("public_tool:", tool(21))

    print("impl 私有名不在门面:", not hasattr(pkg, "_hidden_helper"))

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        legacy = pkg.old_tool
    print("legacy shim:", legacy(5), "| warned:",
          any(issubclass(w.category, DeprecationWarning) for w in caught))

    try:
        pkg.nope
    except AttributeError as err:
        print("unknown attr:", err)
