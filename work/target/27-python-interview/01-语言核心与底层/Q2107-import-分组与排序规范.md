---
title: [Q2107] import 分组与排序规范
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2107 · import 分组与排序规范

> 难度:★★☆☆☆ | 标签:import, 代码规范, isort

**问**:import 语句为什么要有固定分组与排序?怎么自动检查?

**答**:通行规范是三段式:标准库一组、第三方一组、本地一组,组间空一行,组内按模块名字典序。收益不只是好看:三段式让依赖来源一眼可辨,评审时「这个依赖该不该进」有明确落位;字典序减少合并冲突与重复导入;分组混乱经常是模块边界腐化的第一个信号——标准库组里混进业务包,说明抽象漏了。自动检查用 ast 就能写一个迷你检查器:按 Import/ImportFrom 节点收集,遇非导入语句断组,再对每组报告来源类别与组内是否有序,demo 检出第一组 sys、os 乱序。工程上直接用 isort 配 pre-commit,自己写检查器的价值在于面试里讲清规则背后的可判定性。

```python
# file: code/01_语言核心与底层/q2107_import_groups.py
"""import 分组与排序:stdlib、第三方、本地的三段式与自动检查。"""
import ast

STDLIB = {"os", "sys", "ast", "json", "logging", "math", "time"}

SAMPLE = """import sys
import os

import requests

from mypkg import util
import mypkg.other
"""


def root_of(node):
    if isinstance(node, ast.ImportFrom):
        return node.module.split(".")[0] if node.module else ""
    return node.names[0].name.split(".")[0]


def kind_of(root):
    if root in STDLIB:
        return "stdlib"
    if root == "mypkg":
        return "local"
    return "third-party"


def check_groups(source):
    """按连续导入块分组,报告来源与组内有序性。"""
    tree = ast.parse(source)
    groups, current = [], []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            current.append(node)
        elif current:
            groups.append(current)
            current = []
    if current:
        groups.append(current)

    report = []
    for group in groups:
        roots = [root_of(n) for n in group]
        report.append((kind_of(roots[0]), roots, roots == sorted(roots)))
    return report


if __name__ == "__main__":
    for kind, roots, ordered in check_groups(SAMPLE):
        print(f"{kind:11} {roots} {'组内有序' if ordered else '组内乱序'}")
    print("规范:三段式分组加组内字典序;工程上用 isort 挂 pre-commit 自动治理")
```

**追问**:1) 为什么组内要字典序?——减少合并冲突与重复项,diff 干净可预期;相对导入放哪组?——与本地同段,通常排在显式包导入之后。2) 分组的完整约定?——标准库 → 第三方 → 本地应用,组间空行;from X import 与 import X 混排按模块名字典序;工具(ruff isort)强制,人工只看语义。3) 与循环依赖的联动?——分组乱序往往掩盖环;分层「底→中→上」导入让环显形;TYPE_CHECKING 段单独放(Q2103)。4) 生产陷阱?——手动排序与工具配置漂移(统一交工具);try/except 包裹可选依赖混进主分组(Q1557);__init__ 导入顺序引发循环导入。
