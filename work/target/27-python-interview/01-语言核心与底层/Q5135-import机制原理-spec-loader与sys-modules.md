---
title: [Q5135] import 机制原理：spec、loader 与 sys.modules
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5135 · import 机制原理：spec、loader 与 sys.modules

难度：P6-P7 | 标签：importlib、ModuleSpec、原理深挖、循环导入

**问**：`import foo` 这一行背后发生了什么？请完整描述从名字到模块对象的流水线（finders → spec → loaders → sys.modules），并解释循环导入为什么会拿到"半初始化模块"。

**答**：

**结论**：import 流水线是：先查 `sys.modules` 缓存（命中直接返回，这也是循环导入半初始化的根源）；未命中则按 `sys.meta_path` 顺序调用 meta path finder 的 `find_spec(name, path)`——内置模块 BuiltinImporter → 冻结模块 FrozenImporter → path based FileFinder；找到后返回 `ModuleSpec`（含 name、loader、origin、submodule_search_locations）；再由 `module_from_spec` 创建空模块对象并**先放入 sys.modules**，然后调 `loader.exec_module(module)` 执行模块体；执行完毕才把完整模块交给调用方。因为模块对象在 exec 前就进缓存，A import B、B import A 时 A 拿到的 B 或反向拿到的对象是"属性还没填完"的半成品——访问未定义属性抛 AttributeError。

**取舍**：理解流水线才能定制：`importlib.util.spec_from_file_location` 支持按路径加载非包文件；插入自定义 meta_path finder 可做加密模块、远端模块、测试替身；`sys.modules` 手动注入是 mock 的底层手段也是污染源。`from x import y` 并不比 `import x` 少执行——它同样执行整个模块体，只是多一步属性绑定，绑定失败（循环导入）时 Python 3.5+ 会尝试回退用 sys.modules 里的值。

**实战**：排查套路：`python -X importtime` 看导入耗时树；`importlib.metadata` 读发行元数据；"模块被 import 两次"（相对/绝对路径混用导致两个不同 key）是单例失效的经典根因——`sys.modules['foo'] is not sys.modules['pkg.foo']`。

```python
import sys, importlib.util, importlib.machinery, types

# 1) 观察流水线：手动走一遍 spec -> module -> exec
import os, tempfile
d = tempfile.mkdtemp()
src = os.path.join(d, "my_fake_mod.py")
open(src, "w").write("VALUE = 42\nprint('模块体被执行了一次')\n")

spec = importlib.util.spec_from_file_location("my_fake_mod", src)
mod = importlib.util.module_from_spec(spec)
print("exec 前：sys.modules 里有吗 ->", "my_fake_mod" in sys.modules)
sys.modules["my_fake_mod"] = mod          # 与真实 import 一致：先入缓存
spec.loader.exec_module(mod)              # 执行模块体
print("exec 后：VALUE =", mod.VALUE)

# 2) meta_path finder 顺序
print("meta_path ->", [f.__name__ for f in sys.meta_path])

# 3) 循环导入的半初始化复现：模块体中途查看自己
class Circular:
    pass
mod.circular_marker = "already executed"
print("自身属性可在 exec 中途被看到 ->", mod.circular_marker)
```

**追问 1**：为什么"模块在 exec 前就进 sys.modules"是必须的设计？
答：支持数据结构自引用（模块体内创建引用自身模块的类、装饰器注册表），并让递归 import 收敛为一个确定的半初始化对象而不是无限递归；代价就是半初始化窗口。

**追问 2**：`__init__.py` 里 import 子模块时 `sys.path` 和 `__path__` 各管什么？
答：`sys.path` 是顶层模块搜索路径（per-process 全局），包的 `__path__`（spec 的 submodule_search_locations）限定该包子模块的搜索范围；namespace package 没有 `__init__.py`，靠多个路径段合并成 `__path__`。

**追问 3**：如何安全地支持"可选依赖"？
答：`importlib.util.find_spec("name")` 只探测不执行（不进缓存），比 try-import 便宜且无副作用；确认存在后再真正 import。

## 背诵要点

- 流水线：sys.modules 缓存 → meta_path finders 找 spec → module_from_spec 建对象先入缓存 → exec_module 执行。
- 循环导入拿半初始化模块的根源是"先入缓存后执行"；AttributeError 多发在环上访问未完成属性。
- find_spec 只探测不执行；-X importtime 看耗时；同模块两个 key（foo vs pkg.foo）导致单例失效。

## 复盘追问

- 灰度发布时如何用 import 机制做"按版本加载两个同名包"？(提示：改名 + spec_from_file_location)
- 模块级单例在多入口（主程序 + 子模块相对引用）下为什么会失效？如何审计？(提示：打印所有 sys.modules key 指向)
