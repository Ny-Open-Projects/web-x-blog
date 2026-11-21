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
