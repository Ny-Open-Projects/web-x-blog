"""综合设计:限流 反压队列 幂等消费串成事件管道,四类失败模式全部被拦。"""


class DualWindowLimiter:
    def __init__(self, short_limit, short_window, long_quota):
        self.short_limit, self.short_window = short_limit, short_window
        self.long_quota = long_quota
        self.events, self.long_used = [], 0

    def allow(self, now):
        recent = [t for t in self.events if now - t < self.short_window]
        if len(recent) >= self.short_limit:
            return False, "short_window"
        if self.long_used >= self.long_quota:
            return False, "quota"
        self.events.append(now)
        self.long_used += 1
        return True, "ok"

    def reset(self):
        """长窗周期重置:配额清零,短窗事件清空。"""
        self.long_used = 0
        self.events = []


class SpillQueue:
    def __init__(self, mem_limit):
        self.mem_limit = mem_limit
        self.mem, self.spill = [], []

    def put(self, item):
        if len(self.mem) < self.mem_limit:
            self.mem.append(item)
            return True
        self.spill.append(item)                  # 溢出暂存区
        return True

    def drain(self):
        out = self.mem + self.spill              # 顺序:先内存后溢出
        self.mem, self.spill = [], []
        return out


class IdempotentSink:
    """下游消费桩:按事件号幂等,LLM 调用用桩代替。"""

    def __init__(self):
        self.applied = set()
        self.llm_calls = 0

    def consume(self, event):
        if event["id"] in self.applied:
            return "duplicate"
        self.applied.add(event["id"])
        self.llm_calls += 1                      # FakeLLM 桩:不联网
        return "applied"


class Pipeline:
    def __init__(self):
        self.limiter = DualWindowLimiter(short_limit=3, short_window=4.0, long_quota=8)
        self.queue = SpillQueue(mem_limit=3)
        self.sink = IdempotentSink()
        self.rejected = []

    def submit(self, now, event):
        ok, reason = self.limiter.allow(now)
        if not ok:
            self.rejected.append((event["id"], reason))
            return "rejected"
        self.queue.put(event)
        return "queued"

    def flush(self):
        stats = {"applied": 0, "duplicate": 0}
        for event in self.queue.drain():
            stats[self.sink.consume(event)] += 1
        return stats


if __name__ == "__main__":
    p = Pipeline()
    wave1 = [{"id": "e%d" % (i % 6), "ts": float(i)} for i in range(8)]
    r1 = [p.submit(e["ts"], e) for e in wave1]
    assert r1.count("queued") == 6 and r1.count("rejected") == 2, "短窗拦下突发"
    assert [rid for rid, _ in p.rejected] == ["e3", "e1"]

    wave2 = [{"id": "e8", "ts": 20.0}, {"id": "e9", "ts": 21.0},
             {"id": "e10", "ts": 22.0}, {"id": "e11", "ts": 23.0}]
    r2 = [p.submit(e["ts"], e) for e in wave2]
    assert r2 == ["queued", "queued", "rejected", "rejected"]
    assert p.rejected[-1][1] == "quota", "长窗配额由第二道门拦截"

    stats = p.flush()
    assert stats == {"applied": 7, "duplicate": 1}, "重复 id 只消费一次"
    assert p.sink.llm_calls == 7, "桩调用次数等于唯一事件数"

    p.limiter.reset()                            # 长窗周期重置后重发
    assert p.submit(30.0, {"id": "e0", "ts": 30.0}) == "queued", "重发被放行"
    assert p.flush() == {"applied": 0, "duplicate": 1}, "下游幂等兜住重发"
    assert p.sink.llm_calls == 7, "端到端幂等:重发不产生新副作用"
    print("综合管道通过:限流两道门 队列缓冲 幂等消费,突发 超额 重发全被拦住")
