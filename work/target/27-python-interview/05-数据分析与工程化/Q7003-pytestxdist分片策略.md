---
title: [Q7003] pytest-xdist 分片策略与用例独立性改造
date: 2026-11-18
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7003 · pytest-xdist 分片策略与用例独立性改造

> 难度:★★★ | 标签:pytest, CI, 并行

**问**：测试套件 40 分钟想压到 10 分钟以内，`pytest -n 8` 之后 flaky 率反而上升了。并行化为什么会放大 flaky？怎么设计分片策略，用例要满足什么前提才能安全并行？

**答**：结论：xdist 是多进程分发，用例之间共享的任何外部状态——数据库行、临时目录、固定端口、全局 mock、时间敏感的断言——都会成为进程间竞态。并行不是提速开关，前提是**用例独立性**：每个用例自带隔离的数据集与端口/目录，共享资源要么 per-worker 一份，要么加命名空间。提速的正确路径是先隔离再并行，最后才谈分片调优。

分片策略与实战：
- 分发模式选择：默认 `load` 模式按用例动态派发（负载均衡好但顺序不可控，`-p no:randomly` 类顺序依赖用例会炸）；`loadfile`/`loadgroup` 按文件/类保持整组同 worker（模块级 fixture 复用、避免同模块竞态）；`each` 是每 worker 全跑（冒烟冗余）。分层策略：单元测试 `load`，集成测试 `loadgroup`（DB schema 类共享 fixture 的整组绑定）。
- 隔离改造清单：session 级 DB fixture 改 per-worker（`worker_id` 做库名后缀建临时 schema）；文件用 `tmp_path_factory.mktemp(f"{worker_id}-...")`；端口用 0（内核分配）；时间敏感断言改相对时长或注入时钟。
- 事故复盘：并行后 flaky 率 1%→9%，归因是两个模块共用固定 8081 端口起 mock 服务。改造：端口 0 + 地址写进 per-worker fixture；顺带把 session 级 DB 换 per-worker schema，DB 用例从"排队等锁"变真并行。40 分钟 → 9 分钟，flaky 回落到 1%。

```python
# 基线:Python 3.10+ / pytest 7+ / pytest-xdist 3.x;标准库部分可直接运行
# conftest.py 关键片段(xdist 感知 fixture)
import os, socket, tempfile

def worker_id() -> str:
    # xdist 注入的环境变量;单进程跑时为 "master"
    return os.environ.get("PYTEST_XDIST_WORKER", "master")

def make_worker_db_name(base: str) -> str:
    """per-worker 独立 schema:worker_id 后缀保证进程间不互踩。"""
    return f"{base}_{worker_id()}"

def free_tcp_port() -> int:
    """向内核要一个空闲端口(端口 0 绑定后取回),避免固定端口竞态。"""
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port

if __name__ == "__main__":
    print(make_worker_db_name("testdb"), free_tcp_port())
```

**追问**：
- 一层追问：怎么判断 flaky 上升是并行引起的还是本来就有？——单进程重跑同批用例对比：单进程稳定、并行失败，就是竞态；两边都偶发，是既有 flaky。再配合 `pytest --lf` 与失败重跑统计做归因。
- 二层追问：分片数怎么定？——不是核数。公式化思路：测单进程下 CPU 型 vs IO 型用例占比，CPU 型 worker 数 ≈ 核数 × 0.8，IO 型可以超配；瓶颈若在共享资源（DB 连接、CI 容器 CPU quota），先解瓶颈再谈 worker 数。
- 三层追问：`-n` 与 `--dist` 之外，还有什么隐藏坑？——xdist 下 `capsys`、`monkeypatch` 在 session 级 fixture 的行为差异，以及覆盖率合并（需要 `coverage combine`）；另外插件若维护全局状态（如 HTTP mock 服务器）必须 per-worker 实例化。
