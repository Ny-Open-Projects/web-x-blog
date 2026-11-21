import threading
import uuid


class PaymentService:
    """幂等支付: 相同 key 重放首次结果, 不同 key 正常执行。"""

    def __init__(self) -> None:
        self._store: dict = {}          # idem_key -> 响应
        self._inflight: set = set()     # 占位防并发双写
        self._lock = threading.Lock()
        self.executed: list = []

    def pay(self, idem_key: str, amount: int) -> dict:
        with self._lock:
            if idem_key in self._store:
                resp = dict(self._store[idem_key])
                resp["replayed"] = True
                return resp
            if idem_key in self._inflight:
                # 生产中这里应等待首请求结果; 简化为拒绝
                return {"error": "in-progress", "replayed": False}
            self._inflight.add(idem_key)
        try:
            # 真实执行 (这里只记录)
            resp = {"order_id": f"pay-{uuid.uuid4().hex[:8]}",
                    "amount": amount, "status": "paid"}
            self.executed.append(idem_key)
            with self._lock:
                self._store[idem_key] = resp  # TTL 存储, 生产用 Redis SETNX+TTL
            resp = dict(resp)
            resp["replayed"] = False
            return resp
        finally:
            with self._lock:
                self._inflight.discard(idem_key)


if __name__ == "__main__":
    svc = PaymentService()
    key = str(uuid.uuid4())

    r1 = svc.pay(key, 100)
    print("首次支付:", r1)
    r2 = svc.pay(key, 100)  # 网络超时后客户端重试: 同 key
    print("同 key 重试:", r2)
    r3 = svc.pay(key, 100)
    print("同 key 再试:", r3)
    assert r1["order_id"] == r2["order_id"] == r3["order_id"]
    assert r2["replayed"] and r3["replayed"]
    assert len(svc.executed) == 1, "业务只执行了一次"

    r4 = svc.pay(str(uuid.uuid4()), 100)  # 新业务: 新 key
    print("新 key 支付:", r4)
    assert r4["order_id"] != r1["order_id"]
    print(f"\n执行次数 {len(svc.executed)}, 请求次数 4 → 重试安全")
    print("要点: 执行前占位 + 结果存储 + 响应可重放")
