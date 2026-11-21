---
title: [Q1556] re-export 收敛:__all__ 与公共 API 门面
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1556 · re-export 收敛:__all__ 与公共 API 门面

> 难度:★★★☆☆ | 标签:模块设计, __all__, API

**问**:包的公共 API 怎么「收口」?from .impl import func 与 from .impl import func as func 有什么区别?__all__ 管什么?

**答**:公共 API 收口三件套:① __all__ 声明公共面——star-import 与文档工具都看它,没列进的顶层名不会被 from pkg import * 带出;② 显式 re-export——`from .impl import func as func` 的「as 同名」是 PEP 484 约定的公共 API 标记,mypy --strict(--no-implicit-reexport)只认它,不带 as 的转发视为内部实现;③ 弃用转接——模块级 __getattr__(PEP 562)对旧名字发 DeprecationWarning 并转发新实现。收益:调用方只 import 包根,内部模块布局可自由重构;配合 lint 防 API 面无序扩张。反模式:门面模块里堆满无 as 的转发,重构时一半调用方直接 import 到深层模块,收敛名存实亡。

```python
# file: code/01_语言核心与底层/q1556_reexport_api.py
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
```

**追问**:1) __all__ 之外的私有名字会被 star-import 带出吗?——不会,star-import 只看 __all__(无 __all__ 时带出所有不带下划线的顶层名);所以 __all__ 同时是文档和访问闸门。2) 门面模式怎么落?——包 __init__ 里 from .impl import 公共名 + __all__ 收敛;子模块间内部引用走相对导入不受 __all__ 管;re-export 用 `from x import y as y` 显式声明(类型检查器要求)。3) 工具链配合?——IDE/文档生成读 __all__;ruff 检查「导出但未在 __all__」;公共 API 收敛让「可删哪些」一目了然。4) 生产陷阱?——改实现忘记更新 __all__(新旧 API 并存);私有名无下划线被误当公共 API;门面层循环导入(收敛顺序要注意)。
