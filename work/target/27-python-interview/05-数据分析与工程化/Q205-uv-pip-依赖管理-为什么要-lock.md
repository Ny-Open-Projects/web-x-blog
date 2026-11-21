---
title: [Q205] uv/pip 依赖管理:为什么要 lock
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q205 · uv/pip 依赖管理:为什么要 lock

> 难度:★★★ | 标签:uv, pip, lock

**问**:requirements.txt 直接 pip freeze 不就行了,uv 解决了什么问题?

**答**:核心问题是**可复现性分层**:pyproject.toml 声明直接依赖(语义化版本),lock 文件(uv.lock / pip-tools 生成的冻结文件)记录**完整依赖闭包的精确版本与哈希**,保证任何机器、任何时间安装结果一致。`pip freeze` 的问题是把传递依赖和直接依赖混在一起,升级时无从判断来源。**uv** 的优势:Rust 实现,解析与安装比 pip 快 10-100 倍;内置 `uv lock/uv sync` 工作流、统一管理 venv 与 Python 版本、原生支持 workspace;`uv pip` 接口可直接替换 pip。传统方案的等价物是 pip-tools 的 compile + sync,思路相同。

```bash
# uv 工作流:非 python 文件
uv init myproj && cd myproj
uv add httpx            # 写入 pyproject 并更新 uv.lock
uv add --dev pytest     # dev 依赖分组
uv sync                 # 按 lock 精确同步环境,多余包会被移除
uv run pytest           # 在项目环境内运行命令
```

```python
# file: code/05_数据分析与工程化/q205_deps_demo.py
def resolve(specs: list[str]) -> dict[str, str]:
    # 极简示意:lock 的本质是给每个包固定一个精确版本
    return {name.split("==")[0]: name.split("==")[1] for name in specs}

def test_lock_is_exact():
    locked = resolve(["httpx==0.27.2", "anyio==4.4.0"])
    assert locked["httpx"] == "0.27.2"
    assert set(locked) == {"httpx", "anyio"}
```

**追问**:
- uv sync 和 pip install 的差异?——uv sync 按 lock 精确同步环境(多余包会删),pip install 只增不减;环境漂移靠 sync 治理。
- lock 文件要提交吗?——应用必须提交(可复现构建);发布给第三方的库不提交,用宽松依赖声明。
- 怎么处理传递依赖的 CVE?——`uv lock --upgrade` 或 pip-audit 报告后升级 lock;只锁不升的 lock 是安全债。
