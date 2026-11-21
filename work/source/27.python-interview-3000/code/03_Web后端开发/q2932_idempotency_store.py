"""接口幂等性的存储实现: 指纹冲突、在途互斥与结果重放(纯标准库)。"""
import hashlib
import json
import threading


class FakeClock:
    def __init__(self, start=1000.0):
        self.now = start

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


class IdempotencyStore:
    """以幂等键为单位的存储: go 可执行 / replay 重放 / busy 在途 / conflict 指纹不符。"""

    def __init__(self, ttl=600, clock=None):
        self.ttl = ttl
        self.clock = clock or FakeClock()
        self._lock = threading.Lock()
        self._entries = {}

    @staticmethod
    def fingerprint(method, path, body):
        """同键不同体的检测依据: 方法+路径+体的规范化哈希。"""
        raw = json.dumps([method, path, body], sort_keys=True, ensure_ascii=False).encode()
        return hashlib.sha256(raw).hexdigest()

    def begin(self, key, fingerprint):
        now = self.clock()
        with self._lock:
            entry = self._entries.get(key)
            if entry and entry["expires"] > now:
                if entry["state"] == "done":
                    if entry["fingerprint"] != fingerprint:
                        return "conflict", None      # 同键异体: 客户端 bug, 直接拒绝
                    return "replay", entry["response"]
                return "busy", None                  # 在途: 让客户端稍后重试
            self._entries[key] = {"state": "inflight", "fingerprint": fingerprint,
                                  "response": None, "expires": now + self.ttl}
            return "go", None

    def finish(self, key, response):
        with self._lock:
            entry = self._entries.get(key)
            if entry and entry["state"] == "inflight":
                entry["state"] = "done"
                entry["response"] = response

    def fail(self, key):
        """失败要摘除记录, 否则失败结果会被永久重放。"""
        with self._lock:
            return self._entries.pop(key, None) is not None


clock = FakeClock()
store = IdempotencyStore(ttl=600, clock=clock)
fp = store.fingerprint("POST", "/api/orders", {"sku": "A1", "qty": 1})


def execute():
    """模拟扣库存下单, 返回响应体。"""
    return {"order_id": "o-1001", "total": 99.0}


# 1. 首次请求: go -> 执行 -> 落结果
verdict, _ = store.begin("key-1", fp)
assert verdict == "go"
resp = execute()
store.finish("key-1", resp)
print("首次请求执行并落缓存:", resp)

# 2. 网络抖动重发同键同体 -> 重放, 不再执行
verdict, cached = store.begin("key-1", fp)
assert verdict == "replay" and cached == resp
print("重发同键同体 -> 重放缓存响应, 加 Idempotency-Replayed: true 头")

# 3. 同键异体 -> 指纹冲突, 拒绝并告警
verdict, _ = store.begin("key-1", store.fingerprint("POST", "/api/orders", {"sku": "B2", "qty": 9}))
assert verdict == "conflict"
print("同键异体 -> 422 指纹冲突, 说明客户端复用错了键")

# 4. 在途互斥: 未 finish 前并发同键 -> busy
store.begin("key-2", fp)                       # 只 begin 不 finish, 模拟在途
verdict, _ = store.begin("key-2", fp)
assert verdict == "busy"
print("同键并发第二请求 -> 409/425 请稍后重试, 而不是重复扣库存")

# 5. 失败摘除: 执行失败后记录消失, 下一次可以重新执行
verdict, _ = store.begin("key-3", fp)
assert verdict == "go"
store.fail("key-3")
verdict, _ = store.begin("key-3", fp)
assert verdict == "go", "失败后允许重试"
store.finish("key-3", execute())
print("失败摘除后可重试, 成功结果才可重放")

# 6. TTL 过期: 过期记录视同不存在, 但指纹仍在途的窗口由客户端重试承担
clock.advance(601)
verdict, _ = store.begin("key-1", fp)
assert verdict == "go", "过期后同键视为新请求"
print("TTL 过期后同键重新放行, 超长间隔的重复由业务对账兜底")

# 7. 并发压力: 多线程争抢同一键, go 恰好一次
store2 = IdempotencyStore(ttl=600, clock=FakeClock())
fp2 = store2.fingerprint("POST", "/api/orders", {"sku": "A1"})
go_count, busy_count = [], []
barrier = threading.Barrier(8)

def racer():
    barrier.wait()
    verdict, _ = store2.begin("race", fp2)
    (go_count if verdict == "go" else busy_count).append(1)

threads = [threading.Thread(target=racer) for _ in range(8)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("8 线程争抢: go=%s busy=%s" % (len(go_count), len(busy_count)))
assert len(go_count) == 1 and len(busy_count) == 7
print("幂等存储实现演示通过")
