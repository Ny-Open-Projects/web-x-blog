---
title: "[Q7221] yield fixture 的 teardown 抛错：真实失败被吞掉了"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7221 · yield fixture 的 teardown 抛错：真实失败被吞掉了

难度：P6 ｜ 标签：pytest、fixture、teardown、异常掩盖

基线：Python 3.12；pytest 7/8 yield fixture；纯 Python 模拟 setup/body/teardown 生命周期。

**问**：一个 `yield` fixture 负责建临时库、yield 连接、最后 `drop database`。某次测试 body 断言失败，同时 teardown 的 `drop` 也报错（连接已断）。CI 日志里只看到 `ERROR at teardown`，原始的断言失败信息不见了，排查花了半天。teardown 异常为什么会盖住真正的失败？fixture 里该怎么写清理才安全？

**答**：
- **结论**：pytest 的 fixture 生命周期是 setup → yield → teardown。如果 body 已经失败、teardown 又抛异常，pytest 会把 teardown 错误作为**独立的 ERROR** 报告，原始 FAIL 信息仍在但常被日志尾部覆盖；更糟的是 teardown 异常会**中断后续 fixture 的清理**，造成资源泄漏与连锁失败。清理代码里的异常不应该改变测试结论。
- **取舍**：teardown 必须"尽力而为 + 不抛"：能忽略的清理错误记日志，关键资源用 `contextlib.ExitStack` 统一关闭并收集异常；确实需要让清理失败可见时，用 `pytest.fail`/`warnings` 显式上报，而不是让原始异常穿透。另一种做法是把清理做成独立的 session fixture，失败只影响一次收尾。
- **实战**：① teardown 用 `try/except Exception: log.exception(...)` 包住，确保不打断后续清理；② 多个资源按 **LIFO** 顺序关闭（ExitStack 自动保证）；③ 清理操作要幂等（`IF EXISTS`、忽略已关闭连接），避免"已经断了还 drop"；④ CI 里把 `ERROR` 与 `FAILED` 分开统计，别只看最后一行。

```python
"""模拟 pytest fixture 生命周期：body 失败 + teardown 失败时的报告覆盖。"""
from dataclasses import dataclass, field


@dataclass
class Report:
    body_error: str | None = None
    teardown_errors: list[str] = field(default_factory=list)

    def summary(self) -> str:
        if self.teardown_errors:
            return f"ERROR at teardown: {self.teardown_errors[-1]}"
        if self.body_error:
            return f"FAILED: {self.body_error}"
        return "PASSED"


def run_case(fixture, body) -> Report:
    rep = Report()
    gen = fixture()
    next(gen)                       # setup
    try:
        body()
    except AssertionError as e:
        rep.body_error = str(e)
    finally:
        try:
            next(gen)               # teardown
        except StopIteration:
            pass
        except Exception as e:
            rep.teardown_errors.append(str(e))
    return rep


def unsafe_fixture():
    yield "conn"
    raise RuntimeError("drop failed: connection closed")


def safe_fixture():
    yield "conn"
    try:
        raise RuntimeError("drop failed: connection closed")
    except Exception as e:
        print("  [cleanup] 记录并忽略:", e)


def body() -> None:
    assert False, "amount mismatch: 100 != 90"


if __name__ == "__main__":
    print("不安全 fixture:", run_case(unsafe_fixture, body).summary())
    print("安全 fixture  :", run_case(safe_fixture, body).summary())
    print("结论：teardown 不应抛；清理失败要记录，别覆盖 body 的真实失败")
```

**追问一**：为什么 pytest 把 teardown 失败叫 ERROR 而不是 FAILED？
→ 解析：`FAILED` 表示"测试断言不成立"，是业务逻辑问题；`ERROR` 表示"测试无法正常执行/收尾"，是环境或 fixture 问题。两者语义不同，CI 门禁通常对 ERROR 更敏感（说明基础设施不可信）。teardown 抛错被归为 ERROR，正是提醒你"这次结果可能不可信"。

**追问二**：多个 yield fixture 的 teardown 顺序是什么？某个 teardown 抛错会影响其他吗？
→ 解析：按**依赖的反序**（LIFO）执行：后 setup 的先 teardown。某个 teardown 抛异常，pytest 仍会继续执行其余 fixture 的 teardown（尽量收尾），但该异常会被记录为 ERROR，且可能让依赖它的资源处于半关闭状态。所以每个 teardown 都要独立 try/except，不能假设前一个成功。
