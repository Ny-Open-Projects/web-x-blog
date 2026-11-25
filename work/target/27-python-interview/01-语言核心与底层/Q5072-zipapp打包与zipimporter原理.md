---
title: [Q5072] zipapp 打包与 zipimporter 的导入原理
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5072 · zipapp 打包与 zipimporter 的导入原理

> 难度:★★★☆ | 标签:原理深挖, 打包, zipimport, PEP441

**问**：`python -m zipapp` 把一个目录打成一个 `.pyz` 就能直接跑，背后的导入机制是什么？zipapp 与冻结导入（frozen modules）、PEX/shiv 这类自解压方案的区别？什么场景下 zipimport 会成为性能瓶颈？

**答**：结论：zipapp（PEP 441）只是"可执行 zip"封装——文件头加 shebang，运行时由内置的 `zipimporter` 直接从 zip 里的 `.pyc`/`.py` 导入模块，不需要解压到磁盘。原理上 `sys.path` 可以放一个 zip 路径，Python 的 import 体系在 FileFinder 之外内置了 zipimport 这个 path entry finder：它会优先读 zip 内预编译的 `.pyc`（跳过编译步骤），源码 `.py` 则现编现缓存到内存。取舍：a) **zipimport 只导入 Python 代码**，不能加载 zip 内的 C 扩展（`.so`/`.pyd` 必须先解压出来），所以 numpy 这类依赖打不进纯 `.pyz`，PEX/shiv 的做法是启动时把依赖解压到临时目录再改 `sys.path`，zipapp 与它们的差别是"零解压但纯 Python"vs"全依赖但要解压"；b) 3.11+ 的冻结模块（frozen stdlib）是另一回事：解释器把 `os`、`zipimport` 自身等编进二进制，启动时不读任何文件——注意 zipimport 本身是冻结的，这正是它能被"第一个 import"的原因；c) 性能瓶颈：zipimport 是**每次 import 都要读中央目录 + 顺序定位条目**，条目极多（几千个模块）且无 pyc 时每次现编译，冷启动明显劣于目录导入；zip 里没有压缩（stored）反而比 deflate 更快，因为省了解压。实战：内部 CLI 工具、纯 Python 微服务镜像单文件分发用 zipapp 很合适；带 C 扩展的用 shiv/PEX 或直接容器；打 `.pyz` 前先 `compileall` 进 zip 保证都是 pyc。

```python
# file: code/01_语言核心与底层/q5072_zipapp_import.py
import sys, os, zipfile, tempfile, subprocess, zipimport

# 1) 造一个小包: mypkg/__init__.py + __main__.py
d = tempfile.mkdtemp()
pkg = os.path.join(d, "mypkg")
os.makedirs(pkg)
with open(os.path.join(pkg, "__init__.py"), "w") as f:
    f.write("VALUE = 42\n")
with open(os.path.join(d, "__main__.py"), "w") as f:   # 顶层入口: zipapp 直接采用
    f.write("import mypkg, sys; print('hello from pyz', mypkg.VALUE)\n")

# 2) 先 compileall 保证包内是 .pyc(zipimport 走 pyc 免编译)
subprocess.run([sys.executable, "-m", "compileall", "-q", pkg], check=True)

# 3) zipapp 打包并执行
pyz = os.path.join(d, "tool.pyz")
subprocess.run([sys.executable, "-m", "zipapp", d, "-o", pyz], check=True)
r = subprocess.run([sys.executable, pyz], capture_output=True, text=True)
print("pyz 运行输出:", r.stdout.strip() or r.stderr.strip())

# 4) 原理: sys.path 直接挂 zip 也能导入
with zipfile.ZipFile(os.path.join(d, "lib.zip"), "w") as z:
    z.write(os.path.join(pkg, "__init__.py"), "mypkg/__init__.py")
sys.path.insert(0, os.path.join(d, "lib.zip"))
for k in [m for m in list(sys.modules) if m.startswith("mypkg")]:
    del sys.modules[k]
import mypkg
print("zip 路径导入:", mypkg.VALUE, "| importer:", type(mypkg.__spec__.loader).__name__)
zi = sys.path_importer_cache[os.path.join(d, "lib.zip")]
print("path entry finder 类型:", type(zi).__name__)   # zipimporter

# 5) 边界: zip 内不能加载 C 扩展
print("zipimport 能加载 .so 吗: 否(C 扩展需先落盘解压, PEX/shiv 就是这么做的)")
```

**追问**：1) `.pyz` 里的 `__main__.py` 和 `-m` 指定的入口区别？——目录里若有顶层 `__main__.py`，zipapp 直接用它；没有就要 `-m pkg.module:func` 在 zipapp 阶段生成一个 `__main__.py`，本质是写了个调用 `func()` 的引导文件。2) zipimport 为什么能 import 自己所在的 zip？——它是冻结进解释器的（3.11 起纯 Python 冻结优化），不依赖磁盘上的任何模块，这也是 bootstrap 顺序的一部分。3) 打包后 `__file__` 是什么？——是 zip 内部路径（`/path/tool.pyz/mypkg/__init__.py`），任何"按 `__file__` 目录找配置/资源"的代码都会炸，正确做法是 `importlib.resources`（见 Q5074），这是 zipapp 迁移最常见的回归点。

## 背诵要点
- zipapp=可执行 zip（PEP 441），导入靠内置 zipimporter 从 zip 直读 pyc，不解压；`sys.path` 可直接挂 zip。
- 硬边界：不能加载 zip 内 C 扩展（PEX/shiv 解压落盘解决）；打包含 C 扩展的项目别用裸 zipapp。
- 冷启动要点：zip 里全部预编译成 pyc、压缩用 stored、模块条目别太多；`__file__` 指向 zip 内路径，读资源必须用 importlib.resources。

## 复盘追问
- 如果让你把一个内部 CLI 从"git clone + pip install"迁到单文件分发，你会选 zipapp 还是 shiv？判断依据是什么？（提示：有没有 C 扩展依赖、启动延迟要求、是否需要原生升级）
- 团队有人反馈 .pyz 版本"第一个请求特别慢"，你的排查清单是什么？（提示：zip 内是否含 pyc、deflate 解压成本、条目数、是否被 __file__ 路径问题绊住重试）
