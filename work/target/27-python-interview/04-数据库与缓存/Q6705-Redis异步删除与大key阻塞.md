---
title: "[Q6705] Redis 异步删除（lazyfree）与大 key 阻塞复盘"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6705 · Redis 异步删除（lazyfree）与大 key 阻塞复盘

难度：P6 ｜ 标签：事故复盘、Redis、大 key、延迟

基线：Python 3.12；Redis 4.0+；threading 标准库演示同步/异步回收差异。

**问**：为清理一个百万元素的 Set，开发执行了 `DEL bigkey`，监控立刻出现几百毫秒的延迟毛刺，部分请求超时。删除一个 key 为什么会把整个 Redis 卡住？该怎么避免？

**答**：
- **结论**：Redis 主线程是单线程处理命令的，`DEL` 对大对象做同步内存释放，释放百万个元素的耗时全部算在主线程上，期间所有其他命令排队——这就是延迟毛刺的来源。Redis 4.0+ 的应对是 `UNLINK`（异步删除，主线程只摘链、后台线程回收内存）以及 `lazyfree-lazy-eviction`、`lazyfree-lazy-expire`、`lazyfree-lazy-server-del` 等配置，把回收挪到后台线程。
- **取舍**：异步删除让主线程立即响应，但内存不会立刻归还（后台线程慢慢释放），短时间内 RSS 仍高；极端大 key 即使异步，摘链也可能有成本。**治本是别制造超大 key**——按业务维度拆桶，让单 key 元素数可控。
- **实战**：把 `DEL` 换成 `UNLINK`；开启 lazyfree 相关配置；用 `redis-cli --bigkeys` 或 `MEMORY USAGE` 定期盘点大 key 并拆桶；监控 `lazyfree_pending_objects` 看后台积压；注意复制场景下异步删除传播的是 `UNLINK`，从节点也要支持。

```python
import threading
import time


class Store:
    def __init__(self) -> None:
        self.data: dict[str, list[int]] = {}
        self.pending: list[str] = []

    def del_async(self, key: str) -> threading.Thread:
        """模拟 UNLINK：主线程摘链后立即返回，后台线程释放内存。"""
        obj = self.data.pop(key)
        self.pending.append(key)

        def reclaim() -> None:
            time.sleep(0.02)  # 模拟后台线程慢慢释放大对象
            del obj

        th = threading.Thread(target=reclaim)
        th.start()
        return th


if __name__ == "__main__":
    store = Store()
    store.data["big"] = list(range(300_000))
    t0 = time.perf_counter()
    th = store.del_async("big")
    print(
        f"async delete 返回耗时 {time.perf_counter() - t0:.4f}s, "
        f"pending={len(store.pending)}"
    )
    th.join()
    print("后台回收完成")
```

**追问一**：异步删除后 `INFO memory` 的 used_memory 会不会立刻下降？
→ 解析：不会。主线程摘链后逻辑上已删除，但物理内存由后台线程异步释放，used_memory 滞后下降；可观察 `lazyfree_pending_objects` 判断后台是否积压。

**追问二**：除了删除，还有哪些操作会因大 key 阻塞主线程？
→ 解析：`SMEMBERS`/`HGETALL`/`LRANGE 0 -1` 等一次性取全量的命令、大 key 的过期清理、迁移（MIGRATE）。都应改成游标式（SSCAN/HSCAN）或分批，并避免构造超大 key。
