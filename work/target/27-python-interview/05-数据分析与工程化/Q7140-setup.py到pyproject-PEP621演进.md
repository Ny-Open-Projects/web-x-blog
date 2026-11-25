---
title: [Q7140] setup.py 到 pyproject.toml（PEP 621）的打包演进与迁移
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7140 · setup.py 到 pyproject.toml（PEP 621）的打包演进与迁移

难度：P6 ｜ 标签：版本演进 / 打包 / 工程化

**问**：老仓库还是 `setup.py` + `setup.cfg` + `requirements.txt` 三件套，新项目都上 `pyproject.toml`（PEP 621）。这条演进线的各层标准是什么（PEP 517/518/621/660）？迁移时的破坏点与降级兼容怎么处理？

**答**：
- **结论**：演进线四层：**PEP 518**（2016）定义 `pyproject.toml` 的 `[build-system]` 表——构建依赖（build-time deps）与构建后端声明，解决"build 时 import setup.py 需要的包从哪来"；**PEP 517** 定义构建后端 API（`build_wheel`/`build_sdist`），pip 不再执行 setup.py 而是调用后端；**PEP 621**（2021）把项目元数据（name/version/deps/entry-points）标准化进 `[project]` 表，setuptools 61+ 支持，元数据从此工具中立；**PEP 660**（Q7119）让可编辑安装也走构建后端。迁移破坏点：① `setup.py` 里的**动态逻辑**（读文件取版本、条件依赖 `install_requires=[... if py>=3.9]`）不能直接搬进静态 `[project]` 表——setuptools 提供 `[tool.setuptools.dynamic]` 读文件，复杂条件用 `dependencies` + `requires-python` 交叉表达或留 dynamic；② `requirements.txt` 的 `-e .`、`-r`、环境标记语义与 `[project.dependencies]` 不完全对等，生产锁定应交给 lock 文件（uv lock/pip-tools）；③ entry-points 写法变化：`[project.scripts]` 替代 `entry_points={'console_scripts':...}`。降级兼容：老 pip（<21）不认识 PEP 621 元数据时会退回 setuptools 传统路径——所以迁移期保留可构建的 `setup.py` 垫片（`setup(...)` 空壳或从 pyproject 读值）是常见过渡策略。
- **取舍**：静态 `[project]` 表换来工具中立（uv/pdm/hatch/pip 都能读）与未来兼容，代价是失去 setup.py 的编程自由度——官方态度是"动态性是 bug 来源"，能用静态就用静态，dynamic 只留给版本号单点。
- **实战**：① 迁移后用 `python -m build` + `twine check` 验证 sdist/wheel 元数据；② CI 里对比新旧两种方式构建出的 wheel `METADATA` diff，防搬家丢字段；③ `requires-python` 与依赖下限（Q7121）必须在 `[project]` 里显式声明，别留在 requirements.txt 里。

```python
# PEP 621 元数据迁移校验: 静态表 -> wheel METADATA 关键字段不丢失
# 基线: Python 3.11+ tomllib (3.9/3.10 用 tomli); 生产构建用 python -m build
import re
import tomllib  # type: ignore  # 3.11+; 3.9/3.10: import tomli as tomllib

PYPROJECT = """
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "mylib"
version = "1.4.0"
requires-python = ">=3.9"
dependencies = ["requests>=2.28,<3", "pydantic>=2.0"]

[project.scripts]
mylib-cli = "mylib.cli:main"
"""

LEGACY_SETUP = {
    "name": "mylib",
    "version": "1.4.0",
    "install_requires": ["requests>=2.28,<3", "pydantic>=2.0"],
    "entry_points": {"console_scripts": ["mylib-cli=mylib.cli:main"]},
}


def main() -> None:
    meta = tomllib.loads(PYPROJECT)["project"]
    # 校验 1: 三件套字段等价迁移
    assert meta["name"] == LEGACY_SETUP["name"]
    assert meta["version"] == LEGACY_SETUP["version"]
    assert meta["dependencies"] == LEGACY_SETUP["install_requires"]
    # 校验 2: entry-points 写法等价 (新表 "名=目标" 拆出目标)
    assert meta["scripts"]["mylib-cli"] == \
        LEGACY_SETUP["entry_points"]["console_scripts"][0].split("=", 1)[1]
    # 校验 3: requires-python 显式 (下限事故防线)
    assert meta["requires-python"].startswith(">=")
    # 校验 4: build-system 表存在 -> pip 走 PEP 517 后端而非执行 setup.py
    bs = tomllib.loads(PYPROJECT)["build-system"]
    assert bs["build-backend"] == "setuptools.build_meta"
    print("OK: PEP518/517(构建) -> PEP621(元数据) -> PEP660(可编辑); 迁移字段全等价")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 PEP 518 之前"构建依赖"是个隐性问题？
→ 一句话提示：pip 跑 setup.py 时若代码 import 了 setuptools 之外构建才需要的包（如 cython），只能在"装它之前"失败——鸡生蛋问题；[build-system] 让 pip 先建隔离构建环境装齐再构建。

**追问 2**：`requirements.txt` 与 `[project.dependencies]` 的语义差在哪？
→ 一句话提示：前者是"环境安装清单"（支持 -e/-r/哈希/注释，偏运维），后者是包元数据（发布声明，进 wheel）；锁定交给 lock 文件，声明交给 pyproject——两者角色不同不该混用。

## 背诵要点
- 演进链：PEP 518（build-system 构建依赖）→ PEP 517（后端 API，pip 不再执行 setup.py）→ PEP 621（[project] 元数据，setuptools 61+）→ PEP 660（可编辑安装走后端）。
- 迁移破坏点：动态逻辑（版本文件/条件依赖）、requirements 语义不对等、entry-points 新写法；过渡期留 setup.py 空壳垫片。
- CI 校验：新旧构建 METADATA diff 防丢字段；requires-python 与依赖下限必须显式进 [project]。

## 复盘追问
- 为什么官方反对在 pyproject 里保留大量 dynamic？提示：动态值工具不可静态分析（锁文件、发布平台无法预知），破坏"声明式可复现"目标，动态性历史上就是构建漂移来源。
- 迁移期"老 pip 用户"怎么兼容？提示：保留最小 setup.py 垫片 + pyproject 同时声明，老 pip 走传统路径新 pip 走 PEP 517；观察 pip 版本分布后再删垫片。
