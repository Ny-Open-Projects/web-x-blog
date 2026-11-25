---
title: "[Q5181] __init__.py 循环导入：模块级 __getattr__ 延迟求值"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5181 · __init__.py 循环导入：模块级 __getattr__ 延迟求值

难度：P6 ｜ 标签：import、循环依赖、PEP 562、__getattr__、importlib

**问**：一个 SDK 包在 `__init__.py` 里 `from .a import A`，a.py 又 `from .b import B`，b.py 再 `from .a import A`，`import pkg` 直接 `ImportError: cannot import name 'A' from partially initialized module`。为什么偏偏是"包顶层 re-export"最容易炸？`from .a import A` 和 `import pkg.a` 的差别在哪？PEP 562 的模块级 `__getattr__` 为什么能把它变成惰性求值，又有什么代价？

**答**：
结论：import 的语义是"先建模块对象并放进 `sys.modules`，再逐行执行模块体"。执行到 `from .a import A` 时，a 的模块对象已经存在（所以报错里说 partially initialized），但 `A` 这个属性还没绑定——`from X import Y` 本质是 `getattr(模块, "Y")`，取不到就抛 ImportError。循环里必然有一侧在对方还没定义完时就去取属性。`import pkg.a` 只把子模块对象绑定到名字上、不访问属性，所以常常"看起来没问题"，真正炸在后续 `pkg.a.A` 的访问点。PEP 562 的模块级 `__getattr__(name)` 只在模块属性找不到时被调用，于是可以把 `importlib.import_module` 推迟到第一次访问，`import pkg` 阶段不再触发任何子模块加载。

取舍：延迟求值的收益是打断"包初始化即全量加载"的环、顺带把启动时间摊到使用点；代价有三条：a) 错误从 import 期推到运行期（首次访问才炸，监控上表现为"启动正常、某接口 500"）；b) 静态分析器和 IDE 看不到 re-export，需要 `if TYPE_CHECKING:` 里补一份 import 声明；c) `dir(pkg)` 不含惰性属性，要额外实现 `__dir__`，`from pkg import *` 还要 `__all__`。对小包来说直接拆分模块层次、把公共依赖下沉到第三层往往比魔法更划算。

实战：事故形态是"给 SDK 加了一个便捷 re-export，本地跑通（导入顺序恰好有利），CI 里另一个入口先导入了 b，就随机炸"。下面用临时目录造出两个包：坏包在 `__init__.py` 顶层 re-export，b.py 再回头拿 A，复现经典报错；好包改成模块级 `__getattr__`，可以看到 `import goodpkg` 之后 `sys.modules` 里一个子模块都没有，访问 `goodpkg.A` 时才加载 a 和 b。

```python
import importlib
import os
import sys
import tempfile

root = tempfile.mkdtemp()
sys.path.insert(0, root)


def write(rel, src):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)


# ---- 坏味道：__init__.py 顶层 re-export 子模块，子模块再回头拿 ----
write("badpkg/__init__.py", "from .a import A\n")
write("badpkg/a.py", "from .b import B\n\n\nclass A:\n    peer = B\n")
write("badpkg/b.py", "from .a import A\n\n\nclass B:\n    peer = A\n")

importlib.invalidate_caches()
try:
    import badpkg  # noqa: F401
except ImportError as e:
    print("坏味道导入失败:", type(e).__name__, "|", e)

# ---- 修复：模块级 __getattr__（PEP 562）延迟到真正访问时才导入 ----
write(
    "goodpkg/__init__.py",
    "import importlib\n\n\ndef __getattr__(name):\n"
    "    if name in {'A', 'B'}:\n"
    "        mod = importlib.import_module('.' + name.lower(), __name__)\n"
    "        return getattr(mod, name)\n"
    "    raise AttributeError(name)\n",
)
write("goodpkg/a.py", "from .b import B\n\n\nclass A:\n    peer = B\n")
write("goodpkg/b.py", "class B:\n    peer = None\n")

importlib.invalidate_caches()
for name in ("badpkg", "badpkg.a", "badpkg.b"):
    sys.modules.pop(name, None)

import goodpkg

print("import goodpkg 后已加载子模块:", [m for m in sys.modules if m.startswith("goodpkg.")])
print("首次访问 goodpkg.A:", goodpkg.A.__name__)
print("访问后已加载子模块:", sorted(m for m in sys.modules if m.startswith("goodpkg.")))
print("A.peer is B:", goodpkg.A.peer is goodpkg.B)
```

**追问一**：`__init__.py` 加了 `__getattr__`，a.py 顶层的 `from .b import B` 还会炸吗？—— 会。因为 a.py 在执行第一行时，b.py 顶层又去 `from .a import A`，此刻 a 的模块对象在 `sys.modules` 里但类 `A` 还没定义，属性取不到。`__getattr__` 只能解决"包对外暴露"的那一层，环里必须有一侧把导入下沉到函数体（或 `if TYPE_CHECKING:` 里只给类型检查用）。判断哪一侧下沉的标准：谁是被依赖的"底层"，就让上层保持顶层导入、底层改成延迟导入。

**追问二**：为什么把 `from .a import A` 改成 `from . import a` 然后 `a.A` 就"好了"？—— 因为它把"取属性"的时间点从 import 时推到了使用点，等价于手工延迟求值。这不是修复，只是把炸点搬走了：如果 `a.A` 在模块体里被当作类属性默认值使用，依旧会在 a 执行期间访问到未完成的对象。真正的判据是"这个符号是在模块体里就要用，还是只在函数/方法体里用"。

## 背诵要点
- `from X import Y` = 取模块属性；循环时模块对象已存在但属性未绑定 → `cannot import name ... partially initialized module`。
- `import pkg.a` 只绑定模块名不取属性，所以常"看起来没问题"，炸点在使用处。
- PEP 562 模块级 `__getattr__` 做惰性 re-export：`import pkg` 零子模块加载，代价是错误后移、IDE 与 `dir()` 看不到。

## 复盘追问
- 一个包 `import` 就报 partially initialized，如何用"注册早于执行、属性晚于执行"解释，并给出三种修法？（拆层/下沉导入/模块级 `__getattr__`）
- 为什么 `__getattr__` 不能修复环里的另一侧？判断哪一侧该延迟导入的依据是什么？（模块体即用 vs 函数体才用）
