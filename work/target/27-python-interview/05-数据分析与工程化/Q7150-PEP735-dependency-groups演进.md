---
title: [Q7150] PEP 735 dependency-groups 演进
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7150 · PEP 735 dependency-groups：dev 依赖的标准化演进

难度：P6 | 标签：PEP 735、pyproject、版本演进

**问**：以前 dev 依赖（pytest、ruff）要么写进 `[project.optional-dependencies]` 要么靠 requirements-dev.txt，为什么 PEP 735（`[dependency-groups]`）要另立标准？它和 optional-dependencies 的本质区别是什么？

**答**：结论：本质区别是**语义归属**——optional-dependencies 是"发布给用户的可选功能"（如 `pip install pkg[doc]`），dev/test/lint 组是"开发者的本地工具链"，不该出现在发布元数据里、也不该被用户装走。PEP 735 把 dev 依赖标准化进 `pyproject.toml` 的 `[dependency-groups]`，工具无关（uv/pip 8.x+/pdm 等均可读），且有标准化的 `dev` 默认组与组间引用（`{include-group = "test"}`）。它终结的是"每个项目一个 requirements-dev.txt、每套工具一个安装入口"的碎片化。

实战要点：
1. 迁移映射：requirements-dev.txt → `[dependency-groups] test/lint`；`dev` 组用 include-group 聚合所有组，`uv sync --group dev` 或 `pip install --group dev`（pip 需较新版本）。
2. 与 optional-dependencies 的边界判据：会被发布到 PyPI 且用户可装 → extras；仅开发者用 → dependency-groups。
3. 降级基线：PEP 735 于 2024 定稿，旧工具链不识别该表时回退 requirements-dev.txt（可由 `uv export` 生成），CI 双读检查一致性。

```python
"""dependency-groups 的解析与 dev 聚合语义（标准库模拟，可运行）"""
import tomllib
from pathlib import Path

PYPROJECT = b"""
[dependency-groups]
test = ["pytest>=8", "hypothesis>=6"]
lint = ["ruff>=0.8"]
docs = ["mkdocs-material>=9"]
dev = [
    {include-group = "test"},
    {include-group = "lint"},
    {include-group = "docs"},
]
"""


def resolve_groups(raw: dict[str, list], name: str,
                   _seen: set[str] | None = None) -> list[str]:
    """展开 include-group 引用，防环"""
    _seen = _seen or set()
    if name in _seen:
        raise ValueError(f"cycle in group {name}")
    _seen.add(name)
    out: list[str] = []
    for item in raw.get(name, []):
        if isinstance(item, dict) and "include-group" in item:
            out += resolve_groups(raw, item["include-group"], _seen)
        else:
            out.append(item)
    return out


data = tomllib.loads(PYPROJECT.decode())
groups = data["dependency-groups"]
print("dev 组展开:", resolve_groups(groups, "dev"))

# 边界判据：extras 属发布元数据，groups 属开发链
assert "doc" not in [g for g in groups if g == "dev"]
print("语义归属: test/lint/docs -> 开发链, 不进发布元数据")
```

**追问 1**：既然 extras 也能装 dev 依赖，为什么"误用 extras 装 dev 工具"是坏味道？
**提示**：extras 进发布元数据后，用户 `pip install pkg[dev]` 会装上 pytest/ruff 整条工具链，拉大安装体积并暴露内部工具版本约束。

**追问 2**：dependency-groups 与 lock 文件（PEP 751，见 Q7151）如何配合？
**提示**：groups 声明"要什么"，lock 记录"锁到哪个版本"；CI 用 `--group dev` + lock 安装，保证可复现。

## 背诵要点
- PEP 735 语义归属：dev 工具链进 `[dependency-groups]`，发布可选功能才进 extras。
- 标准含 `dev` 默认组与 `{include-group}` 引用，工具无关，uv/pip 均支持。
- 判据一句话：用户会装的是 extras，只有开发者用的是 groups。

## 复盘追问
- 你们的 requirements-dev.txt 与 pyproject 有没有漂移过？迁移后如何 CI 断言一致性？
- 为什么 dev 组引用环在解析期就该报错而不是安装期？
