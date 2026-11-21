---
title: [Q1582] 异步重试装饰器:可重试分类与不吞 CancelledError
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1582 · 异步重试装饰器:可重试分类与不吞 CancelledError

> 难度:★★★☆ | 标签:重试, 装饰器, CancelledError

**问**:写一个通用异步重试装饰器,最容易被忽略的正确性细节是什么?

**答**:三个细节。第一,可重试异常显式声明:只重试声明的瞬时异常(超时、连接重置、5xx),业务异常直接抛,把"该不该重"的判断固化在异常类型里。第二,CancelledError 必须穿透:取消是协程世界的硬中断,装饰器一旦被通用 except 吞掉,"取消一个卡死的重试"就变成"再等一轮退避",任务永远停不下来——所以 except CancelledError: raise 要写在最前面。第三,退避指数增长带抖动且封顶,用 await asyncio.sleep 让出控制权,协程里绝不能同步 sleep。最后把最后一次尝试的异常原样 re-raise,保留完整 traceback。

```python
# file: code/02_并发与网络工程/q1582_async_retry.py
"""异步重试装饰器: 可重试分类 + 绝不吞 CancelledError。

- 只对声明的瞬时异常(网络抖动、5xx)重试, 业务异常直接抛;
- 指数退避 + 抖动, 上限 cap;
- 取消(CancelledError)是协程世界的硬中断: 重试装饰器必须让它穿透,
  否则"取消一个卡死的重试"会变成"再等一轮退避"。
"""
import asyncio
import random


class TransientError(Exception):
    pass


def async_retry(attempts=4, base=0.05, cap=0.15, retry_on=(TransientError,)):
    def deco(fn):
        async def wrapper(*args, **kwargs):
            delay = base
            for attempt in range(1, attempts + 1):
                try:
                    return await fn(*args, **kwargs)
                except asyncio.CancelledError:
                    raise                    # 取消永远不重试
                except retry_on:
                    if attempt == attempts:
                        raise
                    pause = min(cap, delay * random.uniform(0.5, 1.5))
                    print("第 %d 次失败, %.0fms 后重试" % (attempt, pause * 1000))
                    await asyncio.sleep(pause)
                    delay *= 2
        return wrapper
    return deco


calls = {"n": 0}


@async_retry()
async def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise TransientError("网络抖动")
    return "ok"


@async_retry()
async def always_fail():
    raise TransientError("一直失败")


async def main():
    r = await flaky()
    print("flaky 最终返回:", r, "| 尝试次数:", calls["n"])
    assert r == "ok" and calls["n"] == 3, "前两次失败第三次应成功"

    # 重试中的任务被取消: CancelledError 必须穿透, 而不是再等一轮退避
    task = asyncio.create_task(always_fail())
    await asyncio.sleep(0.08)            # 让它先失败一两次进入退避
    task.cancel()
    try:
        await task
        raise AssertionError("不应正常返回")
    except asyncio.CancelledError:
        print("取消正确穿透重试装饰器, 任务被取消")
    assert task.cancelled(), "任务应以取消收场"

    print("结论: 重试清单解决'该不该重', CancelledError 通道解决'停得下来'")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 重试时要不要透传原始 traceback?——要,直接 re-raise 即可;自造新异常会切断 traceback,排障时看不到第一现场。2) CancelledError 为什么必须写在 except 最前?——3.8+ 它继承 BaseException,通用 except Exception 抓不到它(这是个隐式保护),但「except Exception 再 except BaseException 的裸吞」或「except:」仍会吞掉取消;纪律是任何重试/兜底逻辑的第一行就是「让取消穿透」(Q075 的完整链)。3) 可重试异常怎么分类才不误伤?——网络瞬时类(timeout/reset/503)可重;协议错误、4xx(除 429)不重;429 按 Retry-After 重;分类固化在异常类型上而不是布尔参数——与 Q1311 分诊、Q1601 分层共用同一张表。4) 生产陷阱?——用 time.sleep 退避(阻塞事件循环,全连接陪葬);重试里再 create_task 自我嵌套(取消传播断裂);退避无 cap,指数爆炸;装饰器吞掉异常返回 None,调用方拿空值当成功。

---
