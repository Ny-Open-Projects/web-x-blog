---
title: [Q1095] monorepo 与包拆分
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1095 · monorepo 与包拆分

> 难度:★★★★ | 标签:monorepo, 架构

**问**:仓库里 apps 和 libs 越长越乱,循环依赖频发,monorepo 怎么治理?

**答**:monorepo 的关键纪律:分层单向依赖(libs 不许依赖 apps,apps 之间不许互相 import)、每个包独立 pyproject 声明依赖、内部互引用 workspace/可编辑安装。落法:目录结构 `libs/`(领域逻辑、io 工具)+ `apps/`(api、worker)+ `packages/`(对外发布的 wheel),CI 按变更路径触发对应包的测试;依赖方向用脚本静态检查(扫描 import 语句),违反即红。相比多仓,monorepo 换来原子提交与统一重构,代价是必须补上工具化的边界检查。

```python
# file: code/05_数据分析与工程化/q1095_monorepo_check.py
import os
import tempfile
import textwrap

LAYOUT = textwrap.dedent("""
    repo/
      libs/          领域逻辑 零业务依赖
      apps/          api 与 worker 只依赖 libs
      packages/      对外发布的 wheel
      pyproject.toml + uv.lock
""")

def write_tree(root):
    files = {
        "libs/core/util.py": "def add(a, b):\n    return a + b\n",
        "apps/api/main.py": "import sys, pathlib\nsys.path.append(str(pathlib.Path(__file__).parents[2] / 'libs'))\nfrom core.util import add\nprint(add(1, 2))\n",
        "apps/api/bad.py": "import sys, pathlib\nsys.path.append(str(pathlib.Path(__file__).parents[2] / 'apps'))\n",
        "pyproject.toml": "[project]\nname = 'repo'\n",
    }
    for rel, content in files.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)

def check_no_cross_app_imports(root):
    """apps 之间禁止互相 import 的静态检查"""
    problems = []
    for dirpath, _, names in os.walk(root):
        for name in names:
            if not name.endswith(".py"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            with open(path) as f:
                text = f.read()
            if rel.startswith("apps/") and "parents[2] / 'apps'" in text:
                problems.append(rel)
    return problems

if __name__ == "__main__":
    print("推荐布局:", LAYOUT)
    with tempfile.TemporaryDirectory() as root:
        write_tree(root)
        bad = check_no_cross_app_imports(root)
        print("跨 app 依赖违规:", bad or "无")
```

**追问**:
- 追问 1:monorepo 里 CI 只跑变更包怎么做?—— 按 git diff 路径映射到受影响包及依赖闭包,拓扑序执行测试。
- 追问 2:libs 之间也允许依赖吗?—— 允许但要有层次(core 最底层),禁止成环,同样用脚本检查。
