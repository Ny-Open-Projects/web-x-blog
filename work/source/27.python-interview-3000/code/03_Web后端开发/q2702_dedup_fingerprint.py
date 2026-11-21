"""重复提交的指纹去重缓存: 短窗口内同指纹直接拒绝(纯标准库)。"""
import hashlib
import json
import threading


def fingerprint(method, path, body, user_id):
    """指纹 = 方法 + 路径 + 规范化请求体 + 用户, 顺序无关地覆盖提交内容。

    json.dumps 加 sort_keys 保证同一份数据两次构造出同一串;
    缺 user 维度会把不同用户互相误伤, 缺 body 维度会漏掉内容不同但路径相同的请求。
    """
    canonical = json.dumps(
        {"m": method, "p": path, "b": body, "u": user_id},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


class DedupCache:
    """短 TTL 去重: 命中说明窗口内有完全相同的提交在途或刚落库。

    与 Idempotency-Key 的分工: 那是客户端声明的重试语义, 重放旧结果;
    这是服务端自保的防抖, 同指纹第二次直接拒绝, 不代客重放。
    """

    def __init__(self, window=5.0, now=lambda: 0.0):
        self.window = window
        self._now = now
        self._seen = {}
        self._lock = threading.Lock()

    def check(self, fp):
        """返回 (accepted, first_seen)。窗口外或未见过的指纹登记并放行。"""
        t = self._now()
        with self._lock:
            self._seen = {k: v for k, v in self._seen.items() if t - v <= self.window}
            if fp in self._seen:
                return False, self._seen[fp]
            self._seen[fp] = t
            return True, t


clock = {"t": 100.0}
cache = DedupCache(window=5.0, now=lambda: clock["t"])
fp = fingerprint("POST", "/api/orders", {"sku": "A1", "qty": 2}, "u1")

ok1, t1 = cache.check(fp)
assert ok1, "首次提交应放行"
ok2, _ = cache.check(fp)
assert not ok2, "窗口内重复提交应被拒"
clock["t"] = 106.0  # 推进时钟越过窗口
ok3, _ = cache.check(fp)
assert ok3, "窗口外同一内容是新的合法提交"

other = fingerprint("POST", "/api/orders", {"qty": 2, "sku": "A1"}, "u1")
assert other == fp, "键序不同的同内容请求必须产生同一指纹"
diff_user = fingerprint("POST", "/api/orders", {"sku": "A1", "qty": 2}, "u2")
assert diff_user != fp, "不同用户互不影响"
print("首次放行 t=%s, 窗口内重复拒绝, 窗口外重新放行" % t1)
print("指纹与键序无关; 用户维度隔离; 窗口=%s" % cache.window)
