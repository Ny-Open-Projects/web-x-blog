---
title: [Q043] import 机制与循环导入
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q043 · import 机制与循环导入

> 难度:★★★ | 标签:import, 模块

**问**:import 一个模块时发生了什么?循环导入为什么报错,怎么破?

**答**:import 会查找 sys.modules 缓存,未命中则按 sys.path 查找定位器,加载后执行模块顶层代码并把模块对象放入 sys.modules,之后重复导入直接命中缓存。循环导入:A 导入 B 时 B 又导入 A,此时 A 在 sys.modules 中存在但尚未执行完毕,`from a import name` 可能拿到不完整的模块而报 ImportError。解法:重构抽出公共依赖、把 import 下沉到函数内(延迟导入)、或改用 `import a` 后属性访问。

```python
# file: code/01_语言核心与底层/q043_import_cycle.py
import sys
import types

# 用 sys.modules + exec 模拟循环导入:A 启动时导入 B,B 又回头导入 A
mod_a = types.ModuleType("demo_a")
mod_b = types.ModuleType("demo_b")
sys.modules["demo_a"] = mod_a   # A 已登记进 sys.modules 但尚未执行完
sys.modules["demo_b"] = mod_b

if __name__ == "__main__":
    # 现场 1:A 要 B 的 helper,此刻 B 还没定义它 -> ImportError
    try:
        exec("from demo_b import helper", mod_a.__dict__)
    except ImportError as e:
        print("cycle hit (A->B):", e)

    # 现场 2:B 补上 helper 后回头要 A 的类,而 A 早已中断 -> ImportError
    exec("def helper():\n    return 'helper'", mod_b.__dict__)
    try:
        exec("from demo_a import ServiceA", mod_b.__dict__)
    except ImportError as e:
        print("cycle hit (B->A):", e)

    # 解法 1:重构——把公共依赖收敛到先完成定义的一方
    exec("""
def helper():
    return "helper"
class ServiceA:
    def use(self):
        return helper() + "-a"
""", mod_a.__dict__)
    print(mod_a.ServiceA().use())

    # 解法 2:延迟导入——函数体内 import,调用时双方模块都已就绪
    src = "def late():\n    import json\n    return json.dumps([1, 2])"
    mod = types.ModuleType("late_mod")
    exec(src, mod.__dict__)
    print(mod.late())

    print("demo_a" in sys.modules, "demo_b" in sys.modules)
```

**追问**:1) importlib 有什么用?——`importlib.import_module` 支持运行时按字符串动态加载,插件系统的标配;`reload` 可在开发期热更新模块。2) 循环导入的三种解法怎么选?——重构抽公共模块最彻底;函数内延迟导入最快但掩盖设计问题;类型注解依赖放 `if TYPE_CHECKING:` 下既满足 mypy 又不在运行时导入。3) sys.modules 在测试里怎么用?——mock 库替换模块属性的底层就是它;往 `sys.modules` 预插 stub 模块可以让 import 语句直接命中假实现,插件沙箱也用它做隔离。
