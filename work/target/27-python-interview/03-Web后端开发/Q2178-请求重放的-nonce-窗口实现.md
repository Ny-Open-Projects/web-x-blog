---
title: [Q2178] 请求重放的 nonce 窗口实现
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2178 · 请求重放的 nonce 窗口实现

> 难度:★★★★ | 标签:安全, 防重放

**问**:签名请求的防重放,nonce 窗口的存储该怎么实现?有哪些坑?

**答**:nonce 窗口是一个带 TTL 的去重集合:请求携带一次性 nonce,服务端原子地做 check-and-put——窗口内出现过就拒绝,否则记下并设过期时间等于签名时间窗。三个坑:一是并发下的 check 与 put 必须原子,分两步会有竞态,两个并发重放都能通过;二是存储必须有界,攻击者用海量随机 nonce 撑爆内存,对策是容量上限加过期清理,满了宁可拒绝服务也不放重放进来(与安全团队约定的失败策略);三是清理策略要防 O(n) 扫描拖慢请求路径,定期批量清理加惰性检查组合。窗口长度与签名时间窗一致:窗口越长存储越大,越短对时钟偏移越敏感,典型 5 分钟。

```python
# file: code/03_Web后端开发/q2178_nonce_window.py
"""请求重放的 nonce 窗口: 有界存储加原子 check-and-put(纯标准库)。"""
import threading


class NonceStore:
    def __init__(self, window=300.0, capacity=100000):
        self.window = window
        self.capacity = capacity
        self.lock = threading.Lock()
        self.nonces = {}                            # nonce -> 过期时刻

    def check_and_put(self, nonce, now):
        """首次出现返回 True; 窗口内重复返回 False; 满时先清理, 仍满则拒绝服务。"""
        with self.lock:
            if len(self.nonces) >= self.capacity:
                expired = [n for n, exp in self.nonces.items() if exp <= now]
                for n in expired:
                    del self.nonces[n]
                if len(self.nonces) >= self.capacity:
                    raise RuntimeError("nonce 存储已满, 拒绝服务而非放行重放")
            exp = self.nonces.get(nonce)
            if exp and exp > now:
                return False
            self.nonces[nonce] = now + self.window
            return True

    def prune(self, now):
        with self.lock:
            stale = [n for n, exp in self.nonces.items() if exp <= now]
            for n in stale:
                del self.nonces[n]
            return len(stale)


store = NonceStore(window=300)
print("首次 nonce-a      :", store.check_and_put("nonce-a", now=1000))
print("重放 nonce-a      :", store.check_and_put("nonce-a", now=1100))
print("窗口滑过后再复用  :", store.check_and_put("nonce-a", now=1301))   # 已过期可复用
store.check_and_put("nonce-b", now=1301)
print("当前残留条目      :", len(store.nonces))
print("清理过期条目      :", store.prune(1301), "条被移除")
assert store.check_and_put("nonce-a", 1000) is False or True
try:
    tiny = NonceStore(capacity=1)
    tiny.check_and_put("x1", now=0)
    tiny.check_and_put("x2", now=0)
except RuntimeError as exc:
    print("容量打满          :", exc)
print("要点: check 与 put 必须原子; 存储有界, 满时拒绝服务; 窗口与签名时间窗等长")
```

**追问**:
- 多实例部署时 nonce 存哪?——共享存储(Redis SETNX 加 TTL),本地内存只适合单实例或按实例分片的场景。
- nonce 由谁生成?——客户端用随机数或随机加序列,服务端只要求窗口内唯一,不要规定生成方式以免弱实现。
