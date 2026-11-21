---
title: [Q2420] 优雅降级的响应缓存:stale-while-revalidate
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2420 · 优雅降级的响应缓存:stale-while-revalidate

> 难度:★★★★ | 标签:降级, 缓存, SWR

**问**:上游挂了,配置中心的消费者怎么继续活着?

**答**:stale-while-revalidate 的分层服务:fresh 命中直接回;stale 命中先回旧值、后台异步刷新;miss 才同步回源。上游死亡时,缓存退化为"最后已知好值"的陈列柜,服务可用性由旧值顶住。

- 实测:首次 miss-fetch 拿到 value-1,立即再读 fresh,过期后读到旧值并触发后台刷新;

- 上游打死之后:刷新失败留痕 refresh-fail,但旧值不被冲掉,消费者持续拿到 config 值;

- 每个响应带 stale 标记,调用方自己决定"拿旧值继续"还是"报错终止",把选择权交回业务;

- 陈旧数据的容忍度要按业务定:配置类可以分钟级陈旧,库存类可能一秒都不能旧。

```python
# file: code/02_并发与网络工程/q2420_stale_while_revalidate.py
# -*- coding: utf-8 -*-
"""优雅降级的响应缓存: 上游死了, 昨天的答案也比没有答案强。

- fresh 命中直接回, stale 命中先回旧值再后台刷新, miss 才同步回源;
- 后台刷新失败不冲掉旧值, 缓存退化为"最后已知好值"的陈列柜;
- 每个响应都带 age 与 stale 标记, 调用方自己决定拿旧值还是报错。
"""
import threading
import time


class Upstream:
    """假上游: 前两次正常, 之后持续故障。"""

    def __init__(self):
        self.calls = 0
        self.dead = False

    def fetch(self, key):
        self.calls += 1
        if self.dead:
            raise ConnectionError("上游不可达")
        time.sleep(0.05)
        return "value-%d" % self.calls


class SWRCache:
    def __init__(self, upstream, ttl_s):
        self.upstream = upstream
        self.ttl = ttl_s
        self.lock = threading.Lock()
        self.entries = {}            # key -> (value, fetched_at, stale_flag)
        self.refresh_log = []

    def _fetch_and_store(self, key):
        try:
            value = self.upstream.fetch(key)
            with self.lock:
                self.entries[key] = (value, time.monotonic(), False)
            self.refresh_log.append("refresh-ok: " + value)
        except (ConnectionError, OSError) as e:
            self.refresh_log.append("refresh-fail: %s" % e)
            with self.lock:
                if key in self.entries:
                    value, at, _ = self.entries[key]
                    self.entries[key] = (value, at, True)   # 标旧不删除

    def get(self, key):
        with self.lock:
            entry = self.entries.get(key)
            now = time.monotonic()
            if entry and now - entry[1] < self.ttl:
                return entry[0], False, "fresh"
            if entry:                          # stale-while-revalidate
                value, _, _ = entry
                t = threading.Thread(target=self._fetch_and_store, args=(key,),
                                     daemon=True)
                t.start()
                return value, True, "stale-revalidated"
        value = self.upstream.fetch(key)       # miss: 同步回源
        with self.lock:
            self.entries[key] = (value, time.monotonic(), False)
        return value, False, "miss-fetch"


def main():
    upstream = Upstream()
    cache = SWRCache(upstream, ttl_s=0.3)

    v, stale, kind = cache.get("config")
    print("首次读取:", v, kind)
    assert kind == "miss-fetch" and v == "value-1"

    v, stale, kind = cache.get("config")
    print("立即再读:", v, kind)
    assert kind == "fresh"

    time.sleep(0.4)                  # TTL 过期, 同时把上游打死
    upstream.dead = True
    v, stale, kind = cache.get("config")
    print("过期后读取: %s stale=%s %s (旧值先行, 刷新在后台)" % (v, stale, kind))
    assert v == "value-1" and stale and kind == "stale-revalidated"

    time.sleep(0.2)                  # 给后台刷新失败留时间
    v2, stale2, kind2 = cache.get("config")
    print("上游已死仍读到:", v2, kind2, "刷新日志:", cache.refresh_log)
    assert v2 == "value-1", "最后已知好值必须顶住上游故障"
    assert any("refresh-fail" in x for x in cache.refresh_log), \
        "后台刷新失败要留痕, 但不能冲掉旧值"
    print("结论: 缓存的价值在故障时刻, 陈旧但可用胜过全新但不可达")


if __name__ == "__main__":
    main()
```

**追问**:1) 后台刷新失败的退避怎么做?——失败后按指数退避重试刷新,期间继续供旧值,恢复后自动回到 fresh。2) 冷启动就 miss 怎么办?——同步回源加超时,失败则返回显式空值而非崩溃,冷启动的降级路径也要设计。3) stale-while-revalidate 的三层与失败留痕?——fresh 直回;stale 先回旧值+后台刷新;miss 同步回源;刷新失败留痕不冲旧值(「最后已知好值」陈列柜)——旧值不被失败冲掉是分层的关键;响应带 age/stale 标记,选择权(继续用旧值 or 报错)交回业务。4) 后台刷新的退避与冷启动?——刷新失败指数退避重试,期间供旧值,恢复自动回 fresh;冷启动 miss 同步回源+超时,失败返回显式空值不崩溃(冷启动降级路径也要设计,Q2420 原问)。5) 生产陷阱?——刷新失败冲掉旧值(缓存变空,服务崩);stale 标记缺失(调用方不知道拿到旧值);刷新风暴(上游恢复瞬间全员刷新,要抖动);陈旧容忍度一刀切(配置可分钟级,库存不行);后台刷新任务泄漏(没注册表管理,Q1588)。

---
