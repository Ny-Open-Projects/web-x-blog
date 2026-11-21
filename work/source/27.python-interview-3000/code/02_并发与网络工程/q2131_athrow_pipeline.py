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
