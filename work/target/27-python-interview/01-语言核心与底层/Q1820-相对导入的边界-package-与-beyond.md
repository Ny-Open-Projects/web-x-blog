---
title: [Q1820] 相对导入的边界:__package__ 与 beyond top-level 解剖
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1820 · 相对导入的边界:__package__ 与 beyond top-level 解剖

> 难度:★★★☆☆ | 标签:相对导入, __package__, 工程

**问**:Q484 讲了「no known parent package」,另一种报错 attempted relative import beyond top-level package 什么时候出现?两者怎么区分?

**答**:相对导入按当前模块的 __package__ 逐级上跳解析,两类报错对应两种病灶:① __package__ 为空(脚本直跑、顶层模块)——一级相对导入都解析不了,报 no known parent package;② __package__ 有值但层级不够(包内模块再往外跳一层,如包内写 from ...)——跳出了自己的顶层,报 beyond top-level package。demo 在临时目录搭包树、子进程实测三种情形,并打印 __package__ 对照:顶层模块是空串、包本身是自己的名字、子模块是父包点名——这张对照表就是排查相对导入问题的第一现场。规范不变:入口脚本只用绝对导入,包内用相对导入表达包内依赖,包外安装为正式包(Q485)。

```python
# file: code/01_语言核心与底层/q1820_relative_boundary.py
"""相对导入边界:__package__ 与 beyond top-level 解剖。"""
import os
import subprocess
import sys
import tempfile

TREE = {
    "pkg/__init__.py": "",
    "pkg/base.py": "TAG = 'base'\n",
    "pkg/inner.py": "from . import base\nprint('inner ok:', base.TAG)\n",
    "pkg/too_deep.py": "from ... import nothing\nprint('never here')\n",
    "top.py": "import pkg.inner\n",
    "bad_top.py": "from .. import nothing\n",
    "top2.py": "import pkg.too_deep\n",
}


def build_tree(root):
    for rel, content in TREE.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def run(script, root):
    env = dict(os.environ, PYTHONPATH=root, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, os.path.join(root, script)],
                       capture_output=True, text=True, env=env, cwd=root)
    lines = (p.stdout + p.stderr).strip().splitlines()
    return p.returncode, lines[-1] if lines else ""


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        build_tree(root)
        rc, last = run("top.py", root)
        print("脚本 import 包内相对模块:", rc == 0, "|", last)
        rc, last = run("bad_top.py", root)
        print("顶层模块用 ..:", rc != 0, "|", last)
        rc, last = run("top2.py", root)
        print("包内模块向外多跳一层:", rc != 0, "|", last)
        code = ("import pkg, pkg.base;"
                "print('pkg.__package__:', repr(pkg.__package__),"
                "'| pkg.base.__package__:', repr(pkg.base.__package__))")
        env = dict(os.environ, PYTHONPATH=root, PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run([sys.executable, "-c", code],
                           capture_output=True, text=True, env=env)
        print(p.stdout.strip() or p.stderr.strip().splitlines()[-1])
```

**追问**:1) 为什么 -m 方式跑包内模块就没这些问题?——-m 把包根放进 sys.path 并以完整点名加载,__package__ 正确,相对导入自然可用。2) beyond top-level 的机理?——相对导入按 __package__ 逐级上溯;脚本模式 __package__ 为空,一层也上不去;`-m pkg.mod` 由 runpy 设置完整包路径(Q484)。3) main 双入口的处理?——包提供 python -m pkg 入口(__main__.py 委托),模块内的 __main__ 块用绝对导入或临时 sys.path 修补;测试统一从包根跑。4) 生产陷阱?——cron/运维直接 `python pkg/mod.py`;IDE 运行配置用脚本路径跑包内模块;入口文件从「成员」变「脚本」后相对导入全断,排查看 __package__ 与 __file__。
