---
title: [Q979] 滑动窗口限流: zset 时间戳实现
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q979 · 滑动窗口限流: zset 时间戳实现

> 难度:★★★★ | 标签:限流, zset

**问**:用 zset 实现"最近 60 秒最多 100 次"的滑动窗口,四条命令的顺序有讲究吗?

**答**:流程:ZREMRANGEBYSCORE 删除窗口外旧记录 -> ZCARD 统计窗口内次数 -> 未超限则 ZADD 当前时间戳 -> EXPIRE 兜底键生命周期,四步放进一个 Lua 脚本原子执行,顺序必须"先清理再统计",否则垃圾数据让计数虚高。优点:任意窗口、精确无边界突刺;缺点:每次请求都写 zset,高 QPS 下内存与写入压力大(每请求一个 member),大数据量可用"滑动窗口分段计数"(把 60s 切成 6 个 10s 桶,模糊滑动)折衷。同属滑动思想的还有 GCRA/令牌桶,按精度与成本选型。

```python
# file: code/04_数据库与缓存/q979_sliding_window.py
"""zset 滑动窗口限流: 清理 -> 统计 -> 记录 -> 过期兜底"""
import time

class SlidingWindow:
    def __init__(self, limit, window_sec):
        self.limit, self.window = limit, window_sec
        self.zsets = {}                                # key -> [(ts, member)]

    def _zremrange(self, key, now):
        self.zsets[key] = [t for t in self.zsets.get(key, [])
                           if t[0] > now - self.window]

    def allow(self, key, now=None):
        now = now if now is not None else time.monotonic()
        self._zremrange(key, now)                      # 1 清理窗口外
        n = len(self.zsets.get(key, []))               # 2 统计
        if n >= self.limit:
            return False
        member = (now, time.monotonic_ns())            # 3 记录(member 保唯一)
        self.zsets.setdefault(key, []).append(member)
        return True

if __name__ == "__main__":
    sw = SlidingWindow(limit=3, window_sec=2)
    print("连续请求:", [sw.allow("api") for _ in range(4)], "<- 第4次被限")
    time.sleep(2.05)
    print("2 秒后窗口滑出:", sw.allow("api"), "<- 旧记录过期恢复")
```

**追问**:
- zset member 怎么保证唯一?——时间戳可能同秒冲突,拼上纳秒或自增序号;同一 member 重复 ZADD 只会覆盖,导致计数丢失。
- 高并发下 zset 太大怎么办?——限制窗口内元素数自然可控;更大规模改分段计数或令牌桶(状态只有两个数,内存 O(1))。

---
