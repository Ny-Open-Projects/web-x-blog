"""API Key 轮换的双活窗口: 新旧并行期与到期回收(纯标准库)。"""
import hashlib
import time


def key_id(raw):
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


class KeyRegistry:
    """每个调用方最多两把可用钥匙: active(新) 与 retiring(旧, 带宽限期)。

    轮换四步: 签发新钥 -> 新旧双活 -> 旧钥到期 -> 显式吊销。
    """

    def __init__(self, clock=time.time):
        self.keys = {}          # key_id -> {"owner", "state", "expires_at"}
        self.clock = clock

    def issue(self, owner, raw, state="active", ttl=7 * 86400):
        self.keys[key_id(raw)] = {"owner": owner, "state": state,
                                  "expires_at": self.clock() + ttl}

    def authenticate(self, raw):
        kid = key_id(raw)
        rec = self.keys.get(kid)
        if rec is None:
            return None
        if rec["state"] == "revoked" or self.clock() >= rec["expires_at"]:
            return None
        return rec["owner"]

    def rotate(self, owner, old_raw, new_raw, grace=7 * 86400):
        """旧钥降级为 retiring 并只保留 grace 宽限期, 新钥全量生效。"""
        self.keys[key_id(old_raw)]["state"] = "retiring"
        self.keys[key_id(old_raw)]["expires_at"] = self.clock() + grace
        self.issue(owner, new_raw)

    def revoke(self, raw):
        rec = self.keys.get(key_id(raw))
        if rec:
            rec["state"] = "revoked"


now = 1000000.0
registry = KeyRegistry(clock=lambda: now)
registry.issue("partner-a", "old-secret")
print("轮换前旧钥认证:", registry.authenticate("old-secret"))

registry.rotate("partner-a", "old-secret", "new-secret", grace=7 * 86400)
print("轮换后双活: 旧钥 ->", registry.authenticate("old-secret"),
      " 新钥 ->", registry.authenticate("new-secret"))
assert registry.authenticate("old-secret") == "partner-a"
assert registry.authenticate("new-secret") == "partner-a"

now += 7 * 86400 + 1                 # 宽限期过后
print("宽限期后: 旧钥 ->", registry.authenticate("old-secret"),
      " 新钥 ->", registry.authenticate("new-secret"))
assert registry.authenticate("old-secret") is None
registry.revoke("new-secret")        # 疑似泄露, 立即吊销
print("显式吊销后新钥 ->", registry.authenticate("new-secret"))
assert registry.authenticate("new-secret") is None
print("要点: 双活窗口把轮换从停机事件变成后台任务, 存储只存哈希不存明文, 宽限期按对方改造进度定")
