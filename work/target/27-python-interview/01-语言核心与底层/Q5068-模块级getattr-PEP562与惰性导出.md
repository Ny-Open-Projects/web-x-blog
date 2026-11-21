---
title: [Q5068] 模块级 __getattr__（PEP 562）与惰性导出
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5068 · 模块级 __getattr__（PEP 562）与惰性导入

> 难度:★★★★★ | 标签:原理深挖, PEP 562, 惰性导入, import 机制

**问**：NumPy/Sklearn 的包能 `import numpy` 秒开、首次 `np.linalg` 才加载子模块，还能 `from pkg import X` 触发自定义逻辑。3.7 引入的模块级 `__getattr__`（PEP 562）原理是什么？`__dir__` 和弃用转发怎么配合？有哪些坑？

**答**：原理：属性查找失败链的最后一步。`import pkg.mod` 后模块对象就是普通对象的属性访问——先查模块 `__dict__`，再查类层级（module 的类是 `module`），**都失败时**调用模块级 `__getattr__(name)`（PEP 562，3.7+），返回值成为 `pkg.X` 的结果。这是"失败钩子"，与 `__all__`（控制 `import *`）、`__dir__`（定制 `dir()` 补全）三者配合实现惰性导出四件套：a) `__all__` 列出公开名（IDE/文档可见）；b) `__getattr__` 按需 `importlib.import_module` 子模块并转发属性，转发时可挂 `DeprecationWarning` 做老路径迁移；c) `__dir__` 返回补全列表；d) `__getattr__` 里对未知名抛 AttributeError（默认行为兜底）。坑：a) **循环导入风险转移而非消失**：getattr 内 import_module 时若模块又 import 本包顶层，会重入——转发目标尽量叶子模块；b) `from pkg import X` 与 `import pkg; pkg.X` 都走 getattr，但 **`pkg.X = y` 赋值后 setattr 优先于 getattr 钩子**（真实 dict 命中就不再回调），可用来做"真实值覆盖惰性值"；c) 拼写错误延迟到属性访问才炸，比直接 import 更隐蔽——错误信息要带上候选名；d) typing 层的惰性注解（PEP 649/749，见既有 Q5003）解决的是注解求值，本卡的 getattr 解决的是运行时属性，两者互补不冲突。实战：CLI 工具入口、重型子模块（torch backend、matplotlib backend）用惰性导出把冷启动从秒级压到百毫秒级。

```python
# file: code/01_语言核心与底层/q5068_module_getattr.py
import importlib, warnings, os, sys, tempfile

# 1) 搭一个惰性导出的包: pkg/__getattr__ 转发子模块属性
tmp = tempfile.mkdtemp()
pkg = os.path.join(tmp, "lazypkg")
os.makedirs(pkg)
with open(os.path.join(pkg, "__init__.py"), "w") as f:
    f.write('''
import importlib, warnings

__all__ = ["heavy", "greet"]

def __getattr__(name):
    if name == "heavy":
        mod = importlib.import_module("lazypkg.heavy")
        val = mod.heavy_func
        globals()["heavy"] = val   # 关键: import_module 后子模块会 setattr 遮蔽, 须缓存转发值
        return val
    if name == "greet":
        warnings.warn("greet 已弃用, 请用 hello", DeprecationWarning)
        return lambda: "hi (deprecated path)"
    raise AttributeError(f"module {__name__!r} 没有属性 {name!r}")

def __dir__():
    return sorted(list(globals()) + __all__)
''')
with open(os.path.join(pkg, "heavy.py"), "w") as f:
    f.write("print('heavy 模块真实加载!')\ndef heavy_func(): return 'computed'\n")

sys.path.insert(0, tmp)

# 2) 顶层 import 不触发 heavy: 惰性生效
import lazypkg
print("import 后还没加载 heavy")

# 3) 首次访问属性才加载 + 转发
print(lazypkg.heavy())          # 触发 import_module("lazypkg.heavy")
print("第二次访问走已加载模块:", lazypkg.heavy())

# 4) 弃用转发 + 警告
with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter("always")
    print(lazypkg.greet())
print("弃用警告:", ws[0].category.__name__)

# 5) 未知属性: 明确报错
try:
    lazypkg.nope
except AttributeError as e:
    print("未知属性:", e)

# 6) dir() 补全由 __dir__ 控制
print("dir 包含 heavy:", "heavy" in dir(lazypkg))

# 7) setattr 真实值优先于 getattr 钩子
lazypkg.heavy = lambda: "overridden"
print("赋值后优先:", lazypkg.heavy())
```

**追问**：1) getattr 钩子和 `__getattr__` 在类上的实例版本有何差异？——实例版走 MRO（见既有 Q28），模块版只挂在模块对象上、且只有**模块类层级查不到**才触发；`del pkg.X` 则由模块级 `__delattr__`（PEP 562 同时引入）支持。2) 惰性导入与 PEP 594/依赖治理怎么联动？——把重第三方依赖挪到惰性导出后，`importtime`（见既有 Q5059）能看到启动峰值消失，但首次调用延迟仍在，需要按"入口路径"决定哪些子模块值得惰性；配合延迟依赖声明让未用到的依赖可以延迟安装。3) `from lazypkg import heavy` 会发生什么？——import 系统在 pkg 的 dict 里找不到 heavy 时会**尝试把 heavy 当子模块导入**，失败才走 `__getattr__`——所以子模块名和属性名冲突时行为要专门测试。

## 背诵要点
- 模块级 `__getattr__`（PEP 562, 3.7+）是属性查找失败钩子：dict 未命中才调用，可做惰性导入、弃用转发；`__delattr__` 配套、`__dir__` 配合补全。
- `from pkg import X` 先尝试把 X 当子模块导入，失败才走 getattr；setattr 真实值覆盖钩子；未知名必须抛 AttributeError。
- 收益是把冷启动压下来（importtime 验证）；代价是错误延迟暴露，转发目标选叶子模块防重入循环导入。

## 复盘追问
- 你们的 SDK/CLI 冷启动多少秒？importtime 里最重的三个 import 有没有值得惰性化的？（提示：对照本卡四件套改造一个子模块，前后对比 importtime 与首调延迟）
- 有没有"getattr 里 import 大模块被反复触发"或重入循环导入的隐患？（提示：给 getattr 加 import 缓存检查 sys.modules；叶子模块原则进 code review 清单）
