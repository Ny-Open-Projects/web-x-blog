"""幂等框架:幂等表状态机 PROCESSING/COMPLETED + 并发唯一键 + 孤儿回收。"""
import time, threading


class IdempotencyStore:
    def __init__(self, processing_ttl=0.2):
        self.rows, self.ttl, self.mu = {}, processing_ttl, threading.Lock()

    def begin(self, key):
        with self.mu:
            row = self.rows.get(key)
            now = time.monotonic()
            if row and row["state"] == "COMPLETED":
                return "completed", row["result"]
            if row and row["state"] == "PROCESSING":
                if now - row["ts"] > self.ttl:
                    row["state"] = "ORPHAN"        # 崩溃遗留,待回收
                else:
                    return "processing", None
            if row and row["state"] == "ORPHAN":
                pass                                # 孤儿可被新请求接管
            self.rows[key] = {"state": "PROCESSING", "ts": now, "result": None}
            return "started", None

    def finish(self, key, result):
        with self.mu:
            self.rows[key].update(state="COMPLETED", result=result)


class PaymentService:
    def __init__(self, store):
        self.store, self.executed = store, []

    def pay(self, idem_key, order_id, amount):
        status, prev = self.store.begin(idem_key)
        if status == "completed":
            return {"status": "deduped", "result": prev}
        if status == "processing":
            return {"status": "retry_later"}
        # 唯一键抢占成功才执行业务
        self.executed.append((idem_key, order_id, amount))
        result = {"order": order_id, "paid": amount}
        self.store.finish(idem_key, result)
        return {"status": "ok", "result": result}


if __name__ == "__main__":
    store = IdempotencyStore()
    svc = PaymentService(store)
    r1 = svc.pay("idem-1", "o1", 100)
    r2 = svc.pay("idem-1", "o1", 100)          # 网络重发同一 key
    print("首次:", r1["status"], "重发:", r2["status"])
    assert r1["status"] == "ok" and r2["status"] == "deduped"
    assert len(svc.executed) == 1, "业务只执行一次"

    # 并发双发:两个线程同时 begin
    store2 = IdempotencyStore()
    svc2 = PaymentService(store2)
    outs = []
    t1 = threading.Thread(target=lambda: outs.append(svc2.pay("idem-2", "o2", 5)))
    t2 = threading.Thread(target=lambda: outs.append(svc2.pay("idem-2", "o2", 5)))
    t1.start(); t2.start(); t1.join(); t2.join()
    statuses = sorted(o["status"] for o in outs)
    # 竞争结果二选一:后到者拿到 PROCESSING,或先到者已完成拿到去重结果
    assert statuses in (["ok", "retry_later"], ["deduped", "ok"]), "并发下最多一个执行"
    print("并发双发:", statuses)

    # 孤儿回收:进程崩溃遗留 PROCESSING,TTL 后可接管
    store3 = IdempotencyStore(processing_ttl=0.05)
    store3.begin("idem-3")
    time.sleep(0.08)
    status, _ = store3.begin("idem-3")
    assert status == "started", "孤儿被接管可重试"
    print("孤儿 PROCESSING 记录按 TTL 回收,重试可接管")
