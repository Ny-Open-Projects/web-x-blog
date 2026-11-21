---
title: [Q6022] GraphQL 的 N+1 与 DataLoader 批量拉取
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6022 · GraphQL 的 N+1 与 DataLoader 批量拉取

> 难度:★★★★ | 标签:GraphQL, DataLoader, N+1

**问**：GraphQL 的 resolver 模型为什么天然产生 N+1（而 REST 不会）？DataLoader 的两板斧——批合并与请求级缓存——是怎么在事件循环里实现的？"每请求新建 DataLoader"为什么是铁律？

**答**：GraphQL 让客户端声明数据形状，服务端按 resolver 逐字段解析：查 20 本书再逐本取作者，就是 20 次独立调用——**resolver 是"按需逐个"的执行模型**，而 REST 的 handler 一次请求一个函数，N+1 在 ORM 层解决（Q761）。DataLoader 的两板斧：1) **批合并（batching）**：所有 `load(key)` 不立即执行，把 key 攒进队列，用一个 `call_soon` 在**当前事件循环这一轮**结束时统一 flush，一次 `batch_load_fn(keys)` 取回全部，再按 key 分发结果——20 次 load 合并成 1 次 SQL `WHERE id IN (...)`；2) **请求级缓存（memoization）**：同一 key 在同一请求内第二次 load 直接命中缓存的 Future，同请求重复引用（一篇文章的作者被多个字段引用）不重复拉。铁律：**DataLoader 实例必须每请求新建**——它是"请求内一致性缓存"，跨请求复用会把用户 A 的授权数据缓存给用户 B（越权泄漏），且缓存失效语义会错乱。注意 batching 边界：flush 时机是"微任务级"，跨 await 的多轮 resolver 各自成批，批数=await 深度。

```python
# file: code/03_Web后端开发/q6022_dataloader.py
import asyncio

DB_AUTHORS = {i: {"id": i, "name": f"作者{i}"} for i in range(1, 11)}
stats = {"queries": 0}

async def db_get_authors(ids):                 # 模拟一次 SELECT ... WHERE id IN (...)
    stats["queries"] += 1
    await asyncio.sleep(0.001)
    return [DB_AUTHORS.get(i) for i in ids]

class DataLoader:
    def __init__(self, batch_fn):
        self.batch_fn = batch_fn
        self._cache = {}                       # 请求级缓存: key -> Future
        self._keys, self._futs = [], []
        self._scheduled = False

    def load(self, key):
        if key in self._cache:                 # 板斧 2: 同请求重复 key 直接命中
            return self._cache[key]
        fut = asyncio.get_running_loop().create_future()
        self._cache[key] = fut
        self._keys.append(key)
        self._futs.append(fut)
        if not self._scheduled:                # 板斧 1: 本轮循环末统一 flush
            self._scheduled = True
            asyncio.get_running_loop().call_soon(self._dispatch)
        return fut

    def _dispatch(self):
        self._scheduled = False
        keys, futs = self._keys, self._futs
        self._keys, self._futs = [], []
        asyncio.ensure_future(self._run(keys, futs))

    async def _run(self, keys, futs):
        rows = await self.batch_fn(keys)
        for k, f, r in zip(keys, futs, rows):
            f.set_result(r)

async def main():
    loader = DataLoader(db_get_authors)        # 铁律: 每请求新建实例

    async def book_resolver(book_id):          # 模拟 20 个 book resolver 各自取作者
        author = await loader.load(book_id % 10 + 1)
        return {"book": book_id, "author": author["name"]}

    result = await asyncio.gather(*(book_resolver(i) for i in range(1, 21)))
    print("前 2 条:", result[:2])
    print("DB 往返次数:", stats["queries"], "(无 DataLoader 时为 20)")
    print("重复作者命中缓存 -> 往返次数恒为批数,与 resolver 数无关")

asyncio.run(main())
```

**追问**：1) 批合并和 ORM 的 `select_related`/`prefetch_related` 什么关系？——DataLoader 在 resolver 层做批，ORM 预取在查询构造层做；GraphQL 深层嵌套时 resolver 层批是通用解，ORM 预取要每个字段手写、易漏。2) 批内部分 key 失败怎么回传？——`batch_load_fn` 返回与 keys 等长的结果列表，失败位放异常对象由 DataLoader `set_exception` 到对应 Future（部分成功语义，参考 Q1350/Q2159）。3) 缓存与批合并可以关一个吗？——可以（`cache=False` 的 primitive 场景/`prime()` 预热），但关缓存后同请求重复 key 会重复入批，重复引用多的 schema 不建议关。

## 背诵要点
1. N+1 根因：resolver 按字段逐个执行，客户端形状任意 → 深层逐个取数。
2. DataLoader 两板斧：call_soon 攒批（一轮循环一次 batch）+ 请求级 Future 缓存去重。
3. 实例必须每请求新建：跨请求复用 = 授权数据泄漏 + 缓存语义错乱。

## 复盘追问
1. 上线 DataLoader 后某些接口反而更慢（批太大拖垮 DB），怎么治理？（提示：batch 上限 + 分片批（每 200 id 一批）、慢查询监控对准 IN 长度、必要时转预取/materialized 视图）
2. 订阅（subscription）长连接场景下 DataLoader 的"每请求"边界是什么？（提示：每事件算一次"请求"，或在 resolver 上下文绑定实例生命周期，防长连接缓存陈旧与越权）
