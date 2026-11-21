---
title: [Q968] Pipeline 与 Lua: 批量与原子性的两种武器
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q968 · Pipeline 与 Lua: 批量与原子性的两种武器

> 难度:★★★★ | 标签:Redis, 原子性

**问**:Pipeline 和 Lua 脚本都能减少往返,它们的本质区别是什么?

**答**:Pipeline 解决网络往返:把 N 条命令打包一次发送、一次收齐,省 N-1 个 RTT,但服务端仍逐条执行,中间可能插入其他客户端命令——不保证原子性。Lua 脚本由 EVAL 执行,整个脚本在 Redis 单线程里一次跑完,天然原子,且能在命令间做逻辑判断(读-算-写),这是 pipeline 做不到的。选型:纯批量读写(INCR 一堆、MGET 一批)用 pipeline;需要"检查再写"的复合逻辑(限流、扣库存、锁)必须 Lua。注意 Lua 里别做重计算与阻塞调用,脚本超时会卡住整个实例(`lua-time-limit` 超时不会中断脚本,只会让实例进入 BUSY 并拒绝新命令;需 `SCRIPT KILL` 或 `SHUTDOWN NOSAVE`。Redis 7 起允许 KILL 已执行写命令的脚本,但脚本仍不会被自动中断)。

```python
# file: code/04_数据库与缓存/q968_pipeline_vs_lua.py
"""模拟: pipeline 批量但可被并发插入, Lua 脚本原子执行"""
import threading

class FakeServer:
    def __init__(self):
        self.kv = {}
        self.lock = threading.Lock()

    def exec_pipeline(self, cmds):
        """pipeline: 一次传输, 但逐条执行, 中间可能插队"""
        results = []
        for op, k, v in cmds:
            with self.lock:
                if op == "set":
                    self.kv[k] = v
                results.append(("ok", k))
            time_would_allow_interruption = None  # 真实 redis 此处可能执行他人命令
        return results

    def eval_atomic(self, script):
        """lua: 整段脚本作为单命令原子执行"""
        with self.lock:
            before = dict(self.kv)
            script(self.kv)                      # 脚本内部无需再加锁
            return before, dict(self.kv)

if __name__ == "__main__":
    srv = FakeServer()
    cmds = [("set", "k1", 1), ("set", "k2", 2), ("set", "k3", 3)]
    print("pipeline 结果:", srv.exec_pipeline(cmds))

    def transfer(store):                         # 等价 lua: 转账两步
        store["a"] = store.get("a", 100) - 30
        store["b"] = store.get("b", 0) + 30
    before, after = srv.eval_atomic(transfer)
    print("lua 原子: before a=%s b=%s -> after a=%s b=%s"
          % (before.get("a"), before.get("b"), after["a"], after["b"]))
```

**追问**:
- pipeline 会阻塞其他客户端吗?——服务端收包后逐条执行,单条极快所以无感;但一次灌入百万条会让响应缓冲膨胀,分批 1000 条左右为宜。
- Lua 里能用随机结果吗?——带随机写的脚本在主从与 AOF 重放时会产生差异,Redis 限制随机命令后必须返回确定性结果(细节见 redis 文档)。

---
