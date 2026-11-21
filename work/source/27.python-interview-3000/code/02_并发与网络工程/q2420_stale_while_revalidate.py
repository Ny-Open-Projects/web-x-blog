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
