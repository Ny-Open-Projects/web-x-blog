---
title: [Q081] TaskGroup 与结构化并发
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q081 · TaskGroup 与结构化并发

> 难度:★★★★ | 标签:asyncio, TaskGroup, 结构化并发

**问**:什么是结构化并发?TaskGroup 相比 gather 好在哪?

**答**:结构化并发要求子任务的生命周期被限定在父作用域内:进入时创建、退出前全部结束,不遗留后台任务。Python 3.11 的 asyncio.TaskGroup 在一个子任务失败时会取消其余所有子任务,最后抛 ExceptionGroup 汇总错误,比 gather 的"部分失败即泄漏或需手动取消"更安全。异常分组用 `except*` 处理。注意 TaskGroup、ExceptionGroup、`except*` 都是 3.11 才引入的(且 `except*` 是语法级特性),demo 必须加版本守卫:低版本打印提示并跳过,用 gather 等价演示,3.11+ 专属代码放字符串按需编译,否则老解释器连语法检查都过不了。

```python
# file: code/02_并发与网络工程/q081_task_group.py
import asyncio
import sys


async def fetch(i: int) -> str:
    await asyncio.sleep(0.2)
    if i == 1:
        raise ValueError(f"任务 {i} 失败")
    return f"result-{i}"


# TaskGroup/except* 是 3.11+ 语法级特性, 放字符串按需编译
TASKGROUP_DEMO = '''
async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch(i), name=f"fetch-{i}") for i in range(4)]
            # 出 with 时: 要么全部成功, 要么取消全部并抛 ExceptionGroup
        print("全部成功:", [t.result() for t in tasks])
    except* ValueError as eg:
        print("捕获 ExceptionGroup 中的 ValueError:", [str(e) for e in eg.exceptions])
        # 失败时其余任务已被自动取消
    except* RuntimeError as eg:
        print("RuntimeError:", eg.exceptions)
'''


async def main_compat() -> None:
    # 3.11 以下等价演示: gather + return_exceptions 汇总全部异常
    tasks = [asyncio.create_task(fetch(i), name=f"fetch-{i}") for i in range(4)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    errors = [r for r in results if isinstance(r, Exception)]
    if errors:
        print("等价演示捕获异常:", [str(e) for e in errors], "(TaskGroup 会同时取消其余任务)")
    else:
        print("全部成功:", results)


if __name__ == "__main__":
    if sys.version_info >= (3, 11):
        exec(compile(TASKGROUP_DEMO, "<taskgroup_demo>", "exec"), globals())
        asyncio.run(main())  # noqa: F821  由 TASKGROUP_DEMO 动态定义
    else:
        print(
            f"TaskGroup/except*/ExceptionGroup 需要 Python 3.11+, "
            f"当前 {sys.version_info.major}.{sys.version_info.minor}, "
            f"演示跳过, 改用 gather 等价演示"
        )
        asyncio.run(main_compat())
```

**追问**:
- gather 一个失败时其他任务会怎样?——默认被取消但异常只报第一个(return_exceptions=False);return_exceptions=True 则互相不影响,谁都不会被取消,需要自己善后。
- except* 和 except 的区别?——except* 按 ExceptionGroup 内异常类型分组匹配,可同时命中多组;普通 except 只捕获第一个。
- 低版本怎么兼容 TaskGroup?——3.11 起才有;兼容层要么退回 gather+手动取消,要么引入 anyio 的任务组,入口处做版本守卫。
