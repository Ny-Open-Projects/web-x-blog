---
title: [Q201] ruff 与 black:为什么代码规范工具换代了
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q201 · ruff 与 black:为什么代码规范工具换代了

> 难度:★★☆ | 标签:ruff, black, lint

**问**:flake8、black、isort 都能用,为什么要换成 ruff?

**答**:**ruff** 用 Rust 实现,比 flake8/pylint 快一到两个数量级,能秒级 lint 整个大仓库,因此才能放进 pre-commit 和 CI 的"红灯规则"里;它一个工具覆盖了 flake8 + isort + 部分 pylint 的规则集(可启用规则组如 E/F/W/I/UP/B)。**black** 的哲学是"不可协商的格式化":团队不再争论风格,review 里不再有格式噪音;ruff format 也兼容 black 风格,可以二选一。最佳组合通常是 ruff(lint + import 排序)+ black 或 ruff format(格式化),规则集中写在 pyproject.toml 里统一管理。

```toml
# pyproject.toml 片段:非 python 文件,展示统一配置
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B", "SIM"]

[tool.black]
line-length = 100
```

```python
# file: code/05_数据分析与工程化/q201_lint_demo.py
import os  # noqa: F401  未使用导入,ruff F401 会提醒
import sys


def old_style(items):
    # ruff UP 规则会建议用 list comprehension 或内置函数
    result = []
    for i in items:
        if i % 2 == 0:
            result.append(i * 2)
    return result


def test_even_doubled():
    assert old_style([1, 2, 3, 4]) == [4, 8]
```

**追问**:
- ruff 怎么替代 isort?——启用 `I` 规则组 + `ruff check --fix` 自动排序导入;单独跑 isort 的步骤可以删了。
- 格式化冲突怎么处理?——black 与 linter 规则冲突时,以格式化工具为准,linter 关掉对应条目(E501 交给 formatter);不要两个工具互改。
- 规则应该全开吗?——按团队成熟度渐进:先 E/F/I(错误+导入),稳定后加 B(bugbear)、UP(现代化);全开告警淹没等于没开。
