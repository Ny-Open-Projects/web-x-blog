---
title: [Q989] 分布式 Session 与登录态
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q989 · 分布式 Session 与登录态

> 难度:★★★☆ | 标签:session, 认证

**问**:多实例部署下 session 怎么存?Redis session 与 JWT 各适合什么场景?

**答**:传统本地 session 在多实例下因负载均衡路由不稳而失效,标准解法是集中存储:session-id 随机生成放 Cookie,会话数据存 Redis(TTL 即过期),所有实例读同一 Redis——无状态应用 + 有状态存储。JWT 是无状态替代:签名令牌自带用户信息,服务端不存,优点零存储、跨服务易传递,缺点无法主动失效(要拉黑名单又回到存储)、payload 泄露可见、续期复杂。选型:需要"强制下线/单点登录互踢/即时吊销"用 Redis session;纯 API、可接受令牌生命周期内不可撤的用 JWT(配短 TTL + refresh token)。安全底线:session-id 高熵随机、Cookie HttpOnly+Secure+SameSite、敏感操作二次校验。

```python
# file: code/04_数据库与缓存/q989_distributed_session.py
"""Redis session: 登录写入 多实例共享 主动踢下线"""
import secrets
import time

class SessionStore:
    def __init__(self, ttl=60):
        self.data, self.ttl = {}, ttl

    def login(self, user) -> str:
        sid = secrets.token_urlsafe(16)
        self.data[sid] = {"user": user, "expire": time.monotonic() + self.ttl}
        return sid

    def get(self, sid):
        rec = self.data.get(sid)
        if rec is None:
            return None
        if time.monotonic() > rec["expire"]:
            del self.data[sid]
            return None
        rec["expire"] = time.monotonic() + self.ttl      # 滑动续期
        return rec["user"]

    def kick(self, user):                               # 强制下线: 全端失效
        kicked = [sid for sid, r in self.data.items() if r["user"] == user]
        for sid in kicked:
            del self.data[sid]
        return kicked

if __name__ == "__main__":
    store = SessionStore()
    s1, s2 = store.login("alice"), store.login("alice")
    print("实例A 验证:", store.get(s1), "| 实例B 验证另一会话:",
          store.get(s2), "<- 共享 Redis, 双实例可用")
    print("踢下线:", store.kick("alice"), "随后验证:", store.get(s1))
```

**追问**:
- 为什么 session-id 要服务端生成而不是用用户名?——可预测的会话标识等于开放会话固定攻击,必须高熵随机且登录后轮换。
- Redis 挂了登录态全丢怎么办?——多副本+哨兵;更稳的是 session 双写或退化为短 TTL JWT + 黑名单,平衡可用性与可控性。

---
