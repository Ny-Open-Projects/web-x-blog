---
title: [Q7024] nox 与 uv 的多版本矩阵测试
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7024 · 多版本矩阵测试：库要支持 3.9-3.13 五个版本，CI 怎么组织才不失控？

> 难度:★★★ | 标签:nox, uv, CI

**问**：一个三方库声明支持 Python 3.9-3.13，还混了 asyncio、sqlite3 行为差异。测试矩阵怎么设计？5 个版本全跑太慢，怎么裁剪？nox 和 tox、uv 怎么分工？

**答**：结论：矩阵测试 = "会话矩阵 + 分层裁剪"。nox 用 Python 代码声明会话（`@nox.session(python=["3.9", "3.13"])`），比 tox 的 ini 更适合做条件逻辑；uv 负责"秒级装环境"，`uv venv -p 3.11` + `uv pip install` 把矩阵一轮时间从 10 分钟压到 1 分钟，两者组合是 2025+ 的新默认。裁剪策略：**全量跑边界版本（最低 + 最高），PR 只跑边界 + 1 个中间版，夜跑/发版前全量**——语义变更风险几乎都出现在"最老支持的写法"和"最新解释器的新语义"两端。

机理与实战：
- 会话声明要点：`python=[...]` 展开笛卡尔积，配合 `@nox.parametrize` 加依赖矩阵（如 SQLAlchemy 1.4/2.0 两代）时用 `reuse_venv=False` 防串味；环境隔离原则是"每个 (python, dep) 组合一个独立 venv"。
- 版本差异测试不是"再跑一遍"：3.12+ 的异常组/f-string 语法差异用 `sys.version_info` 分支 + `skipif`；真正值钱的是**最低版本守卫**——CI 里加一条"禁止使用超过 3.9 语法"的 lint（ruff `target-version`），让不兼容代码在写的时候就报错，而不是在 3.9 环境的深夜 CI 里报错。
- uv 的角色：它是环境层加速器（并行安装、全局缓存、uv run 直接管理解释器下载），不替代 nox 的"会话编排"语义；也可用 nox 内置 `uv` backend（nox 2024.07+ 支持 session 安装走 uv）。

```python
# 基线:Python 3.9+ 标准库 ;演示矩阵裁剪决策与版本分支守卫
import sys
from dataclasses import dataclass

SUPPORTED = ["3.9", "3.10", "3.11", "3.12", "3.13"]


@dataclass
class Session:
    python: str
    deps: tuple[str, ...]


def build_matrix(pythons: list[str], dep_sets: list[tuple[str, ...]]) -> list[Session]:
    """笛卡尔积展开会话矩阵。"""
    return [Session(p, d) for p in pythons for d in dep_sets]


def prune_for_pr(matrix: list[Session]) -> list[Session]:
    """PR 级裁剪:只跑最低/最高/一个中间版本,夜跑恢复全量。"""
    keep = {matrix[0].python, matrix[-1].python}
    mid = matrix[len(matrix) // 2].python
    keep.add(mid)
    return [s for s in matrix if s.python in keep]


def version_guard() -> None:
    """最低版本守卫:按 sys.version_info 分支,不兼容语法写时报警。"""
    if sys.version_info >= (3, 12):
        # 3.12+ 才有的写法放这里,配合 ruff target-version 保证 3.9 可解析
        print("新版本分支:支持 ExceptionGroup 语义")
    else:
        print("旧版本分支:降级实现")


if __name__ == "__main__":
    dep_sets = [("sqlalchemy==2.0.*",), ("sqlalchemy==1.4.*",)]
    matrix = build_matrix(SUPPORTED, dep_sets)
    print(f"全量矩阵 {len(matrix)} 会话:")
    for s in matrix:
        print("  ", s.python, s.deps[0])
    pr = prune_for_pr(matrix)
    print("PR 裁剪后:", [(s.python, s.deps[0]) for s in pr])
    version_guard()
```

**追问一**：矩阵里为什么先跑"最低版本"？
答：最低版本暴露语法/依赖兼容问题（新语法、新 stdlib 行为），是矩阵里最"脆"的一环；CI 排序把最脆的放前面，失败快速退出省时。高版本排后，主要暴露 deprecation 与语义变化。

**追问二**：uv 秒级装环境后，还需要缓存策略吗？
答：需要——uv 的快来自全局缓存（wheel 硬链接），缓存目录本身要 CI 缓存持久化；另外解释器下载（uv python install 3.9-3.13）也要缓存。没有缓存层，uv 的"秒级"只在第二次生效。

**背诵要点**：
- 矩阵 = 笛卡尔积(python × 依赖)，每个组合独立 venv 防串味。
- 裁剪策略：PR 跑最低/最高/中间三档，夜跑与发版前全量。
- nox 管编排、uv 管环境加速；最低版本守卫靠 ruff target-version 前置到编码期。

**复盘追问**：
- 依赖矩阵出现 2×5=10 会话时如何用 fail-fast 与分片并行控制总时长？
- stdlib 行为差异（如 3.12 的 distutils 移除）在矩阵测试里怎么系统性发现？

## 背诵要点
- 边界版本（最低+最高）承载绝大多数兼容性风险，PR 级只测三档。
- 会话矩阵隔离原则：一个组合一个 venv，绝不复用。
- 版本兼容在编码期用 ruff target-version 守卫，不在 CI 深夜报错。

## 复盘追问
- nox 会话中如何注入 uv 作为安装后端并验证缓存命中？
- 支持窗口结束（drop 3.9）的矩阵收敛流程怎么设计？
