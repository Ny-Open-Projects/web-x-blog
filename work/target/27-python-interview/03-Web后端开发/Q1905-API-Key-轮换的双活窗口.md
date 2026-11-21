---
title: [Q1905] API Key 轮换的双活窗口
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1905 · API Key 轮换的双活窗口

> 难度:★★☆☆ | 标签:API 安全, 密钥管理

**问**:调用方有几百个,让所有人在同一时刻换 API Key 不现实,怎么平滑轮换?

**答**:双活窗口:签发新钥后新旧两把并行有效,旧钥标记 retiring 并带宽限期(如 7 天),宽限期内两者都能通过认证;调用方按自己的节奏切换,宽限期一到旧钥自动失效,全程无停机。流程四步:签发新钥、进入双活、监控旧钥流量归零、到期吊销或提前回收。工程细节:存储只存密钥哈希不存明文,数据库泄露不丢钥匙;认证响应可带弃用提示头,提醒仍在用旧钥的调用方;按 key_id 维度统计调用,宽限期结束前对未迁移的大户主动通知;疑似泄露走独立路径,立即吊销不等宽限。同一调用方最多两把活跃钥匙,防止钥匙蔓延失控,轮换审计记录谁签发、谁吊销、旧钥最后使用时间。

```python
# file: code/03_Web后端开发/q1905_apikey_rotation.py
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
```

**追问**:
- 宽限期定多长?——按最慢集成方的发版周期,一般 7 到 30 天,期间看流量监控决定是否延长一次。
- 轮换期间能监控到迁移进度吗?——能,按新旧 key 分别计数,旧钥流量占比就是未迁移清单。
