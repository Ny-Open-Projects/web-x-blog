---
title: [Q7005] CI 中的 Python 缓存策略与 pre-commit 秒级化
date: 2026-11-18
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7005 · CI 中的 Python 缓存策略(wheel 缓存、pre-commit 秒级化)

> 难度:★★☆ | 标签:CI, 缓存, 工程效率

**问**：CI 一个 PR 要 18 分钟，其中装依赖 6 分钟、pre-commit 3 分钟。缓存不是配了吗，为什么还这么慢？说说 Python 项目 CI 缓存的分层设计与缓存 key 的失效策略。

**答**：结论：慢的根因通常是"缓存了下载、没缓存安装产物"和"缓存 key 太粗导致命中率为零"。Python CI 缓存要分三层设计：**下载层**（pip/uv 的 wheel 下载缓存）、**环境层**（预装好的 venv 或 uv 的硬链接仓库）、**产物层**（自建 wheel house / pre-commit 的仓库缓存），每层 key 的失效条件不同，混在一层就等于没缓存。

分层设计与 key 策略：
- 下载层：key=`OS+Python 版本+lock 文件哈希`。lock 文件不变即命中——前提是项目真有 lock（uv.lock / pip-tools 的 requirements.txt），"requirements.txt 写 `>=` 的项目"缓存 key 每次都变，等于裸奔。
- 环境层（收益最大）：uv 的 `uv sync` 用全局 cache 做硬链接安装，秒级；传统 pip 的进阶做法是把 venv 目录整体缓存，key 里必须含 Python 小版本（3.11 与 3.12 的 venv 不通用），且要接受"偶发损坏需回退重建"（key 加 fallback）。
- pre-commit 秒级化：它自己有 `~/.cache/pre-commit`（按 hook 仓库 rev 缓存环境），CI 里缓存这个目录，key 含 `.pre-commit-config.yaml` 的哈希；再配 `--hook-stage manual` 拆分重活，PR 上只跑快速 hook。
- 事故复盘：团队把整个 venv 缓存但 key 只到 Python 主版本，一次 3.11→3.11.9 补丁后 venv 里残留旧 ABI 扩展，CI 偶发段错误。修复：key 加 patch 版本 + 缓存命中后跑 `python -c "import 关键扩展"` 自检，失败自动重建。

```python
# 基线:Python 3.9+ 标准库;缓存 key 生成器(可运行,模拟 CI yaml 的 key 计算)
import hashlib, sys

def cache_key(lock_hash: str, scope: str = "wheel") -> str:
    """分层缓存 key:lock 哈希为主键,scope 隔离层,解释器 ABI 进环境层。"""
    if scope == "venv":
        abi = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        seed = f"venv|{abi}|{lock_hash}"
    elif scope == "precommit":
        seed = f"precommit|{lock_hash}"          # 配置文件哈希由调用方传入
    else:
        seed = f"wheel|{sys.platform}|{lock_hash}"
    return f"py-ci-{scope}-" + hashlib.sha256(seed.encode()).hexdigest()[:12]

if __name__ == "__main__":
    h = hashlib.sha256(open(__file__, "rb").read()).hexdigest()  # 演示:以本文件当 lock
    for scope in ("wheel", "venv", "precommit"):
        print(cache_key(h, scope))
```

**追问**：
- 一层追问：为什么优先推 uv 而不是继续调 pip 缓存？——uv 的全局 cache + 写时硬链接让"装依赖"从分钟级到秒级且天然增量，替代了大部分手工 venv 缓存的复杂度；pip 路线的缓存 key/ABI 损坏维护成本更高，是旧栈的妥协方案。
- 二层追问：私有 wheel house 什么时候值得建？——依赖含私有 fork 或 PyPI 慢/不稳时；构建产物（`pip wheel -w house`）按版本入缓存后，CI 装依赖退化成"从内网拷文件"，还顺带解决供应链审计。
- 三层追问：缓存命中率怎么监控？——CI 平台的 cache 统计（Actions 的 cache hit 输出）按 key 前缀聚合；命中率 < 80% 时排查 key 里混入时间戳/路径类易变分量。
