---
title: [Q604] ExceptionGroup 与 except*:并发异常的聚合表达
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q604 · ExceptionGroup 与 except*:并发异常的聚合表达

> 难度:★★★☆ | 标签:ExceptionGroup, except star, TaskGroup

**问**:Python 3.11 的 ExceptionGroup 解决什么问题?except* 和普通 except 有什么区别?

**答**:并发场景下一个操作可能产生多个异常(3 个子任务各自失败),传统异常模型一次只能抛一个,信息全丢。ExceptionGroup 把多个异常打包,except* 可以按类型拆分捕获:每个 except* 分支拿到匹配类型的子组,且一个 try 可以有多个 except* 各自匹配。与 except 的区别:except* 会遍历组内所有异常分别匹配(可能有多个分支都触发);匹配的是组内元素的类型;重新抛出未捕获的部分。TaskGroup、asyncio.gather(return_exceptions=True 后手工检查)、anyio 都用它承载"批量失败"。注意 ExceptionGroup/`except*` 是 3.11+ 语法级特性,3.9 连解析都过不了,demo 用 exec 按需编译,低版本打印提示并用 gather(return_exceptions=True) 等价演示。

```python
# file: code/02_并发与网络工程/q604_exception_group.py
import asyncio
import sys

# ExceptionGroup/except* 是 3.11+ 语法级特性, 放字符串按需编译
DEMO_311 = '''
async def worker(name: str, delay: float, exc: Exception | None) -> str:
    await asyncio.sleep(delay)
    if exc:
        raise exc
    return f"{name}-ok"


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(worker("db", 0.05, ValueError("db 连接失败")))
            tg.create_task(worker("cache", 0.06, TimeoutError("cache 超时")))
            tg.create_task(worker("api", 0.07, ValueError("api 500")))
    except* ValueError as eg:
        print(f"ValueError 子组 ({len(eg.exceptions)} 个):",
              [str(e) for e in eg.exceptions])
    except* TimeoutError as eg:
        print("TimeoutError 子组:", [str(e) for e in eg.exceptions])

    print("三个失败都被独立捕获, 没有信息丢失")
'''


async def main_compat() -> None:
    """3.11 以下等价演示: gather(return_exceptions=True) 收集全部异常。"""
    from typing import Optional

    async def worker(name: str, delay: float, exc: Optional[Exception]) -> str:
        await asyncio.sleep(delay)
        if exc:
            raise exc
        return f"{name}-ok"

    results = await asyncio.gather(
        worker("db", 0.05, ValueError("db 连接失败")),
        worker("cache", 0.06, TimeoutError("cache 超时")),
        worker("api", 0.07, ValueError("api 500")),
        return_exceptions=True,
    )
    errors = [r for r in results if isinstance(r, Exception)]
    print(f"等价演示收集到 {len(errors)} 个异常:", [str(e) for e in errors])
    print("按类型子组拆分捕获要等 3.11+ 的 except*")


if __name__ == "__main__":
    if sys.version_info >= (3, 11):
        exec(compile(DEMO_311, "<exception_group_311>", "exec"), globals())
        asyncio.run(main())  # noqa: F821  由 DEMO_311 动态定义
    else:
        print(
            f"ExceptionGroup/except* 需要 Python 3.11+, "
            f"当前 {sys.version_info.major}.{sys.version_info.minor}, "
            f"演示跳过, 改用 gather(return_exceptions=True) 等价演示"
        )
        asyncio.run(main_compat())
```

**追问**:1) raise ExceptionGroup 里嵌套子组合法吗?——合法,组可以嵌套(except* 匹配会递归下钻),这正是"扇出再扇出"的并发树表达失败时的自然结构。2) TaskGroup 与 gather 的选择?——TaskGroup:失败即取消兄弟、聚合抛出(结构化并发默认);gather(return_exceptions=True):全部跑完按序返回、不取消;按「失败传播语义」选(Q589)。3) except* 的工程要点?——多分支独立匹配、嵌套组递归下钻(Q469);分支内 break/continue/return 禁用;低版本 SyntaxError 要版本门控。4) 生产陷阱?——把 ExceptionGroup 当单异常记日志丢子异常;except Exception 兜不到 BaseExceptionGroup(含取消);gather 与 TaskGroup 混用语义混乱。

---
