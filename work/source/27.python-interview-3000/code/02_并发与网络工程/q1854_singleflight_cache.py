# -*- coding: utf-8 -*-
"""异步缓存击穿保护: 单飞 singleflight 让同一个 key 只加载一次。

- 击穿: 缓存失效瞬间, 成百请求同时回源, 数据库被同一份数据打 N 次;
- 单飞: 第一个到的请求当 leader 建 Future 挂进 in-flight 表, 其余当 follower;
- follower 直接 await 同一个 Future, leader 的结果与异常都会广播给全体;
- 完成后摘除 in-flight 条目, 异常不缓存, 下一次调用重新单飞。
"""
import asyncio


class SingleFlightCache:
    def __init__(self, loader):
        self._loader = loader
        self._cache = {}
        self._inflight = {}
        self._lock = asyncio.Lock()
        self.loads = 0

    async def get(self, key):
        if key in self._cache:                     # 命中缓存, 不回源
            return self._cache[key]
        async with self._lock:
            fut = self._inflight.get(key)
            if fut is None:
                fut = asyncio.get_running_loop().create_future()
                self._inflight[key] = fut
                leader = True
            else:
                leader = False
        if not leader:
            return await fut                       # 异常也会原样传播给 follower
        self.loads += 1
        try:
            value = await self._loader(key)
        except Exception as e:
            fut.set_exception(e)
            raise
        else:
            self._cache[key] = value
            fut.set_result(value)
            return value
        finally:
            async with self._lock:
                self._inflight.pop(key, None)


async def main():
    loader_state = {"calls": 0, "fail_once": True}

    async def loader(key):
        loader_state["calls"] += 1
        await asyncio.sleep(0.15)                  # 模拟慢回源
        if loader_state["fail_once"]:
            loader_state["fail_once"] = False
            raise ValueError("源站这次不灵")
        return "value-of-" + key

    cache = SingleFlightCache(loader)

    # 第一波: 8 个并发请求撞上源站故障, 全体收到同一个异常
    r1 = await asyncio.gather(*[cache.get("hot") for _ in range(8)],
                              return_exceptions=True)
    errs = [x for x in r1 if isinstance(x, ValueError)]
    print("第一波: 回源 %d 次, %d 个 follower 同样收到异常"
          % (loader_state["calls"], len(errs)))
    assert loader_state["calls"] == 1 and len(errs) == 8

    # 第二波: 源站恢复, 8 个并发只回源一次, 全体拿到同一结果
    r2 = await asyncio.gather(*[cache.get("hot") for _ in range(8)])
    print("第二波: 回源累计 %d 次, 全体结果一致=%s"
          % (loader_state["calls"], len(set(r2)) == 1))
    assert loader_state["calls"] == 2 and len(set(r2)) == 1 and r2[0] == "value-of-hot"

    # 第三波: 已进缓存, 零回源
    await asyncio.gather(*[cache.get("hot") for _ in range(8)])
    assert loader_state["calls"] == 2, "命中缓存后不应再回源"
    print("结论: leader 回源一次, follower 排队等同一个 Future, 异常也公平分发")


if __name__ == "__main__":
    asyncio.run(main())
