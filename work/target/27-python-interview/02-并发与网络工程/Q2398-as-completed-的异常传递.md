---
title: [Q2398] as_completed 的异常传递
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2398 · as_completed 的异常传递

> 难度:★★☆ | 标签:as_completed, 异常传递, 任务批

**问**:一批任务里有两个会抛异常,as_completed 怎么把异常交给调用方?

**答**:as_completed 把异常也当作"完成"来递送:await 每个 Future 时,异常在循环体内原样抛出,调用方逐个 try/except 区分成败。

- 实测四个任务两好两坏,按完成顺序产出 ok、err 交错的结果,一个失败不打断整批消费;

- 这与 gather(return_exceptions=False) 的"一坏全坏"截然不同,as_completed 天然适合逐个隔离失败;

- 异常对象就是任务里抛的原异常,带完整 traceback,分类处理靠 except 的异常类型;

- 如果循环体内不 catch,第一个异常会冲断循环,剩余已完成任务的结果就漏收了。

```python
# file: code/02_并发与网络工程/q2398_as_completed_exc.py
# -*- coding: utf-8 -*-
"""as_completed 的异常传递: 谁先完成谁先出队, 异常也不例外。

- as_completed 把异常当结果递送: fut.result() 在循环体内抛出原异常;
- 单个任务失败不中断整批, catch 之后循环继续消费剩余 Future;
- 调用方负责逐个区分成败, 这正是 as_completed 与 gather 的分工差异。
"""
import asyncio


async def ok_task(name, s):
    await asyncio.sleep(s)
    return name + "-ok"


async def bad_task(msg, s):
    await asyncio.sleep(s)
    raise ValueError(msg)


async def main():
    fs = [asyncio.ensure_future(ok_task("A", 0.05)),
          asyncio.ensure_future(bad_task("B 爆了", 0.10)),
          asyncio.ensure_future(ok_task("C", 0.15)),
          asyncio.ensure_future(bad_task("D 爆了", 0.20))]
    outcomes = []
    for fut in asyncio.as_completed(fs):
        try:
            outcomes.append(("ok", await fut))
        except ValueError as e:
            outcomes.append(("err", str(e)))
    print("按完成顺序的结局:")
    for kind, payload in outcomes:
        print("  ", kind, payload)
    kinds = [k for k, _ in outcomes]
    assert kinds == ["ok", "err", "ok", "err"], "顺序与成败都应如实递送"
    assert len(outcomes) == 4, "一个任务失败不能打断整批消费"


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 异步函数里抛的 ValueError 到 result() 时 traceback 还在吗?——在,Task 会保留异常的 __traceback__,re-raise 或记录都完整。2) 想“一个失败就全停”该用什么?——gather 默认行为或 TaskGroup 的结构化取消,失败自动传染。3) as_completed 与 gather 的失败语义分工?——as_completed:逐个隔离失败,一个失败不打断整批消费(适合「能收多少收多少」);gather(return_exceptions=False) 一坏全坏、True 全收但要自行分类;TaskGroup 结构化取消(失败自动传染)——「隔离 vs 传染」是三种 API 的分界线。4) 循环体内不 catch 的后果?——第一个异常冲断 for 循环,剩余已完成任务的 Future 没人消费(结果漏收+异常 never retrieved);正确姿势:try/except 包住 await f,except 里分类记录后继续——「消费循环的健壮性」由调用方负责。5) 生产陷阱?——循环体不 catch(漏收);异常对象被丢弃(traceback 丢失);把 as_completed 当 gather 用(语义混);超时后不收尸(Q2399);按提交顺序处理结果(它按完成顺序,业务假定错了)。

---
