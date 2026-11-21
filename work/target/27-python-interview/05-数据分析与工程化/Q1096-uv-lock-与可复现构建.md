---
title: [Q1096] uv lock 与可复现构建
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1096 · uv lock 与可复现构建

> 难度:★★★☆ | 标签:uv, 依赖锁定

**问**:为什么 pip install -r requirements.txt 还不够,必须要有 lock 文件?

**答**:requirements.txt 只钉顶层依赖,传递依赖在每台机器上按当时最新解析,CI 与生产可能装出不同版本,"在我机器上是好的"由此而来。lock 文件(uv.lock/poetry.lock)锁定整棵依赖树的精确版本与哈希,任何机器 `uv sync` 都装出位对位相同的环境;升级是显式动作(`uv lock --upgrade-package x`)走评审。工程纪律:lock 提交入库、CI 用 lock 安装、基础镜像或 venv 缓存以 lock 哈希为 key,让"可复现"从口号变成机制。

```python
# file: code/05_数据分析与工程化/q1096_uv_lock.py
import json

AVAILABLE = {
    "requests": {"2.31.0": [], "2.32.0": ["urllib3>=1.21.1"]},
    "urllib3": {"2.0.7": [], "2.2.1": []},
}

def resolve(requirements, locked=None):
    """简化解析器:返回确定性的 pinned 版本,模拟 lock 的思想"""
    locked = dict(locked or {})
    for name in requirements:
        versions = sorted(AVAILABLE[name], reverse=True)
        locked[name] = versions[0]
        for dep in AVAILABLE[name][locked[name]]:
            dep_name = dep.split(">=")[0].strip()
            if dep_name not in locked:
                locked.update(resolve([dep_name]))
    return locked

if __name__ == "__main__":
    # uv 命令:uv lock 生成锁文件 / uv sync 按 lock 安装 / uv lock --upgrade-package requests
    lock = resolve(["requests"])
    print(json.dumps(lock, indent=2))
    assert resolve(["requests"]) == lock, "解析必须确定性,这就是 lock 的意义"
```

**追问**:
- 追问 1:lock 和 constraints 文件的区别?—— lock 是全量精确解,constraints 只约束上限,前者用于可复现安装,后者用于兼容性护栏。
- 追问 2:锁文件冲突怎么解?—— 谁升级谁负责重新 resolve,lock 的 diff 必须与版本变更 PR 一一对应。
