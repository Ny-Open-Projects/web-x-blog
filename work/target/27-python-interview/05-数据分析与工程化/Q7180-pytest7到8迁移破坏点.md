---
title: [Q7180] pytest 7 到 8 迁移破坏点
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7180 · pytest 7 → 8 迁移：弃用清单、收集行为变化与升级剧本

难度：P6 ｜ 标签：版本演进、pytest、测试工程
基线：pytest 8.x（Python 3.8+）；pytest 插件生态（pytest-asyncio 0.23+ 等）。

**问**：仓库几千个测试用例钉在 pytest 7.4，升级 8.x 后 collection 阶段就报错、部分用例莫名 skipped。pytest 8 的主要破坏点有哪些？几千用例的仓库怎么安全升级？

**答**：**结论**：pytest 8 的四类主要破坏点：① **收集行为收紧**——8.0 起对非类容器里的 `__init__`、重复模块名（不同目录同名 test 文件无 `__init__.py`）的报错更严格，经典报错 `import file mismatch`；② **fixture 语义**——未声明的 fixture 参数、scope 不匹配（session fixture 被更小 scope 依赖时）从弃用警告变错误；③ **断言与警告**——`pytest.warns`/`pytest.deprecated_call` 对无警告场景直接失败，`filterwarnings` 的默认 error 策略让存量 DeprecationWarning 显形；④ **插件兼容矩阵**——pytest-asyncio 8.0 前后模式变化（`asyncio_mode`）、老插件在 8.x 直接不加载。升级剧本：pytest 7.4 上先跑 `-W error::pytest.PytestDeprecationWarning` 清零 → 修"同名测试文件无 `__init__.py`"的历史包袱 → 插件矩阵逐个升 → 全量跑 + 抽样比对失败集与 7.x 的差异。

**取舍**：两个常见捷径的正确性：改 hash 文件名冲突用 `rootdir` 内加 `__init__.py` 或 `--import-mode=importlib`——后者是官方推荐但会改变模块导入语义（conftest 依赖、相对导入行为），要全量回归而不是只看收集通过。另一捷径是 `filterwarnings ignore` 一刀切——把 8.x 变严的警告静默等于埋下一批"行为已变但没人知道"的用例，正确姿势是分类修复。

**实战**：升级预检与收集冲突检测（标准库演示 pytest 的收集语义）：

```python
# pytest 8 升级预检：同名测试文件冲突与弃用信号扫描
import pathlib, re

def find_name_conflicts(root: str) -> list[str]:
    """不同目录下同名 test 文件且缺 __init__.py -> import file mismatch。"""
    seen: dict[str, list[pathlib.Path]] = {}
    for p in pathlib.Path(root).rglob("test_*.py"):
        seen.setdefault(p.name, []).append(p)
    conflicts = []
    for name, paths in seen.items():
        if len(paths) > 1:
            lacks = [p for p in paths if not p.with_name("__init__.py").exists()]
            if len(lacks) > 1 or (lacks and len(paths) > 1):
                conflicts.append(f"{name}: {len(paths)} 处，其中 {len(lacks)} 处缺 __init__.py")
    return conflicts

def scan_deprecated_patterns(root: str) -> list[str]:
    hits = []
    pat = re.compile(r"pytest\.warns\(|pytest\.deprecated_call\(|yield_fixture")
    for p in pathlib.Path(root).rglob("test_*.py"):
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if pat.search(line):
                hits.append(f"{p.name}:{i}: {line.strip()[:60]}")
    return hits

# 演示：构造一棵假仓库树
import tempfile
root = pathlib.Path(tempfile.mkdtemp())
(root / "a").mkdir(); (root / "b").mkdir()
(root / "a" / "test_api.py").write_text("def test_x(): pass\n")
(root / "b" / "test_api.py").write_text("def test_x(): pass\n")
(root / "b" / "test_warn.py").write_text(
    "import pytest\ndef test_w():\n    with pytest.warns(UserWarning):\n        pass\n")

print("收集冲突:", find_name_conflicts(str(root)))
print("弃用信号:", scan_deprecated_patterns(str(root)))

# pytest.warns 语义收紧说明（标准库等价演示）
import warnings
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    # 块内没有发出任何 UserWarning
print(f"8.x 语义：pytest.warns 块内无对应警告 -> FAIL（捕获到 {len(caught)} 条，"
      f"7.x 部分场景仅静默通过）")
```

**追问 1**：`--import-mode=importlib` 改变了什么语义？为什么不能无脑开？
提示：不再把测试文件插入 `sys.modules` 顶层，同名文件可共存，但 `sys.modules` 断言、conftest 可见性、`__file__` 相对路径等依赖旧语义的测试会碎；开启后必须全量回归。

**追问 2**：pytest-asyncio 从 0.21 到 0.23 的 fixture-loop 变化踩过什么坑？
提示：0.23 引入 per-test loop 作用域变化，session 级 async fixture 的 loop 绑定改变，表现为"单跑过、全量挂"；对策是显式 `loop_scope` 并固定插件版本。

**追问 3**：几千用例怎么比对升级前后的失败集？
提示：两版本各跑一遍，导出 JUnit XML，diff 失败用例集合；新增失败逐个归因为"8.x 更严（该修）"还是"环境差异（该修环境）"，禁止直接 skip 消音。

## 背诵要点
1. pytest 8 四破坏面：收集收紧（同名文件/import mismatch）、fixture scope 语义变错误、warns 无警告即失败、插件兼容矩阵。
2. 升级剧本：7.4 上 `-W error::PytestDeprecationWarning` 清零 → 修 __init__.py 包结构 → 插件逐个升 → JUnit XML diff 失败集。
3. `--import-mode=importlib` 解同名冲突但改导入语义，必须全量回归；禁止用 filterwarnings 一刀切静默行为变化。

## 复盘追问
1. 你们仓库里有多少"不同目录同名 test 文件"的存量？当年是怎么积累下来的（复制粘贴式建测试？）
2. 插件矩阵升级时哪个插件最痛？锁插件版本的策略现在写在哪个文件里，谁负责跟进上游？
