---
title: [Q2131] athrow 注入异常:管道的恢复与毒丸终止
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2131 · athrow 注入异常:管道的恢复与毒丸终止

> 难度:★★★ | 标签:athrow, 异步生成器, 错误注入

**问**:不通过 return,能不能从外部"扔个异常进"异步生成器,让它走降级路径?

**答**:athrow(exc) 把异常精确投到生成器当前挂起的 yield 处;内部用 try/except 包住 yield 即可就地恢复,不接住的异常向上传播并终止生成器。

- 实测注入 ValueError 后管道输出 degraded 条目并继续工作;

- 未接住的 ZeroDivisionError 象征毒丸:生成器终止,调用方收到异常;

- 终止后再 next 一律 StopAsyncIteration,状态不可逆;

- 这是流式管道里受控降级与受控停机的标准机制。

```python
# file: code/02_并发与网络工程/q2131_athrow_pipeline.py
# -*- coding: utf-8 -*-
"""athrow 注入异常: 流式管道内部的恢复与终止。

- athrow(exc) 把异常精确投到生成器当前挂起的 yield 处;
- 生成器内部 try/except 包住 yield 即可就地恢复, 继续产出;
- 内部不接住的异常向上传播并终止生成器, 是受控的"毒丸"。
"""
import asyncio


async def resilient_pipeline(source):
    """数值翻倍输出; 注入的 ValueError 走降级路径而不是崩溃。"""
    for item in source:
        try:
            yield "ok:%d" % (item * 2)
        except ValueError:
            yield "degraded:%d" % item


async def main():
    gen = resilient_pipeline([1, 2, 3, 4, 5])
    print(await gen.__anext__())          # ok:2

    recovered = await gen.athrow(ValueError("注入一次故障"))
    print("athrow 后生成器恢复, 产出:", recovered)

    print(await gen.__anext__())          # 管道继续: ok:4
    print(await gen.__anext__())          # ok:6

    # 毒丸: 内部没接 ZeroDivisionError, 生成器终止, 异常传到调用方
    try:
        await gen.athrow(ZeroDivisionError("毒丸"))
        print("意外: 毒丸被吞")
    except ZeroDivisionError as e:
        print("未接住的注入异常向上传播:", e)
    try:
        await gen.__anext__()
        print("意外: 终止后还有产出")
    except StopAsyncIteration:
        print("生成器已终止, 再 next -> StopAsyncIteration")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) athrow(GeneratorExit) 会怎样?——那是 aclose 的底层动作,手动注入容易踩"yield 后又 GeneratorExit"的坑,关闭请交给 aclose。2) 恢复后 item 是重复处理了吗?——异常落在 yield 点,当前 item 已产出,注入影响的是"下一次迭代"的走向,不会重复消费。3) athrow 与 aclose 的边界?——aclose 底层注入 GeneratorExit(关闭语义,内部不能再 yield,否则 RuntimeError);athrow 注入业务异常(恢复/终止语义);手动 athrow(GeneratorExit) 踩双重坑——「关闭交 aclose,降级交 athrow」分工明确。4) 受控降级的管道模式怎么搭?——生成器 try/except 包住 yield:注入异常→except 产出 degraded 占位→继续;调用方 athrow(V) 即可让管道「这一轮降级,下一轮正常」——流式管道的优雅降级原语,与熔断降级(Q1336)组合。5) 生产陷阱?——athrow 后还 next(终止态不可逆);except 里再 yield GeneratorExit 相关歧义;恢复逻辑吞掉所有异常(真 bug 被降级掩盖,要分类);athrow 注入的异常类型与内部 except 不匹配(直接终止);生成器已 aclose 再 athrow(StopAsyncIteration)。

---
