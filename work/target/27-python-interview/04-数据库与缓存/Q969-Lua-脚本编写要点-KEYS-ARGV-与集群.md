---
title: [Q969] Lua 脚本编写要点: KEYS/ARGV 与集群约束
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q969 · Lua 脚本编写要点: KEYS/ARGV 与集群约束

> 难度:★★★★ | 标签:Redis, Lua

**问**:写一个"扣库存"的 Lua 脚本要注意什么?KEYS 和 ARGV 为什么必须分清?

**答**:模板:`EVAL "script" numkeys key1 key2 arg1 arg2`。要点:一、所有键走 KEYS 传参,数值与业务参数走 ARGV——Redis Cluster 按脚本声明的 KEYS 计算槽位,把键写死在脚本字符串里会在集群下报错(交叉槽);二、脚本返回单值(整数/字符串/表),客户端解析注意 null 与整数截断(Lua number 到 RESP);三、保持脚本短小、幂等,失败重试安全;四、复杂度控制在常数时间,禁止循环大量数据。扣库存经典脚本:GET 校验足够则 DECR 返回 1,否则返回 0,全程原子,替代"先 GET 再 DECR"的竞态。

```python
# file: code/04_数据库与缓存/q969_lua_stock.py
"""用 Python 函数模拟 EVAL 扣库存脚本, 展示 KEYS/ARGV 分离与原子性"""
import threading

STOCK_LUA = """
local stock = tonumber(redis.call('GET', KEYS[1]) or '-1')
local want  = tonumber(ARGV[1])
if stock >= want then
  return redis.call('DECRBY', KEYS[1], want)
else
  return -1
end
"""

class FakeRedis:
    def __init__(self):
        self.store = {"stock:1": 10}
        self.lock = threading.Lock()

    def eval(self, script, keys, args):
        """逐行解释脚本语义的等价实现(教学用)"""
        with self.lock:                          # redis 单线程: 脚本天然原子
            key, want = keys[0], int(args[0])
            stock = int(self.store.get(key, -1))
            if stock >= want:
                self.store[key] = stock - want
                return self.store[key]
            return -1

if __name__ == "__main__":
    r = FakeRedis()
    print("脚本:\n" + STOCK_LUA.strip())
    print("扣 5 件 ->", r.eval(STOCK_LUA, ["stock:1"], [5]))
    print("再扣 6 件 ->", r.eval(STOCK_LUA, ["stock:1"], [6]), "<- 不足返回 -1")
    print("剩余:", r.store["stock:1"])
```

**追问**:
- 集群下两个键不在同一槽会怎样?——脚本报 CROSSSLOT 错误,解法是 hash tag(如 {order1}:stock 与 {order1}:pay 强制同槽)或拆脚本。
- 脚本缓存怎么做?——生产用 SCRIPT LOAD + EVALSHA 避免每次传脚本体,注意主从切换后 NOSCRIPT 需重载。

---
