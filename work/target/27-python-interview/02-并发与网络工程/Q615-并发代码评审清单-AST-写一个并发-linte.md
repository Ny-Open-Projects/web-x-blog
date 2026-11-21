---
title: [Q615] 并发代码评审清单:AST 写一个并发 linter
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q615 · 并发代码评审清单:AST 写一个并发 linter

> 难度:★★★★ | 标签:code review, AST, 静态检查

**问**:review 并发代码时你按什么清单看?能不能把部分检查自动化?

**答**:人工清单:锁的粒度与临界区是否完整(check-then-act 有没有被切开)、锁顺序是否全局一致、await/sleep 是否混入错误位置、异常路径上锁是否释放、共享可变状态的归属是否清晰。可自动化部分用 AST 检查:async 函数里出现 time.sleep、acquire 与 release 不配对、裸 except 吞掉 CancelledError 等,做成 CI linter 拦截在合并前。自动检查的价值不是替代审查,而是把"低级但高危"的模式挡在人工审查之前,让审查聚焦协议设计。

```python
# file: code/02_并发与网络工程/q615_concurrency_lint.py
import ast

SAMPLE = '''
import asyncio
import threading
import time

lock = threading.Lock()

async def bad_sleep():
    time.sleep(1)          # L1: async 内阻塞
    async with lock:       # L2: asyncio.Lock 与 threading.Lock 混用 (示例简化)
        pass

def unbalanced():
    lock.acquire()
    if True:
        return             # L3: acquire 后无 release
    lock.release()

def lock_pair():
    lock.acquire()
    try:
        pass
    finally:
        lock.release()
'''


def lint(source: str) -> list[str]:
    issues: list[str] = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call):
                    name = ast.unparse(sub.func)
                    if name == "time.sleep":
                        issues.append(
                            f"第 {sub.lineno} 行: async 函数 {node.name} 内调用 time.sleep 会阻塞事件循环, 应改用 await asyncio.sleep")
        if isinstance(node, ast.FunctionDef):
            acquires = sum(
                1 for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "acquire"
            )
            releases = sum(
                1 for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "release"
            )
            if acquires > releases and not any(
                isinstance(n, ast.Try) for n in ast.walk(node)
            ):
                issues.append(
                    f"第 {node.lineno} 行: 函数 {node.name} 中 acquire {acquires} 次但 release {releases} 次, 且无 try/finally 保护")
    return issues


if __name__ == "__main__":
    for msg in lint(SAMPLE):
        print("[lint]", msg)
    print("人工清单补充项: 锁顺序 / 临界区完整性 / CancelledError 不得吞掉")
```

**追问**:1) 为什么"裸 except 吞 CancelledError"值得进 linter?——async 任务里 `except Exception` 捕不到 CancelledError(它继承 BaseException)是对的,但 `except BaseException` 或裸 except 会吞取消,任务杀不死,这类模式静态可查,危害极大。2) 并发 linter 的检查面?——裸 except、time.sleep in async def、create_task 不持引用(启发式)、锁内 await、阻塞调用进循环;AST 检查的边界:跨文件调用链查不到,靠约定+评审(Q615 正文)。3) 规则的落地?——ruff 自定义规则或项目 lint(Q511);每条规则给修复建议;误报高的降为 warning。4) 生产陷阱?——linter 只查本文件漏 from-import 别名;规则太严被绕过;静态检查替代不了压测(Q608)。
