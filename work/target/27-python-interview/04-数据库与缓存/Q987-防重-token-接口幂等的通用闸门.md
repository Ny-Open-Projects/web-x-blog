---
title: [Q987] 防重 token: 接口幂等的通用闸门
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q987 · 防重 token: 接口幂等的通用闸门

> 难度:★★★★ | 标签:幂等, token

**问**:前端防抖挡不住重复提交,服务端怎么做提交防重?

**答**:防重 token 三步:一、进入表单页时服务端发一个一次性 token(SETNX token:xxx 1 EX 300),返回前端;二、提交时携带 token,服务端 Lua 校验存在则 DEL 并放行(原子),不存在则拒绝"重复提交";三、业务执行。它把"防重"从业务态挪到提交凭证上,对表单类、支付类都通用。与幂等表的区别:token 是"只防重复点击"(同 token 只能成功一次),幂等表是"同一业务操作任意次到达结果相同"(以业务键为准);支付场景两者都要——token 拦 UI 重复,唯一约束拦网络重试。token 失效策略:一次性删除 or 短 TTL 内可重复返回同一结果(配合缓存首次响应)。

```python
# file: code/04_数据库与缓存/q987_idempotency_token.py
"""防重 token: 发放 -> 原子校验并消费 -> 业务执行"""
import secrets

class TokenService:
    def __init__(self):
        self.tokens = set()

    def issue(self) -> str:
        token = secrets.token_hex(8)
        self.tokens.add(token)                  # SETNX token EX 300
        return token

    def consume(self, token) -> bool:
        """Lua: EXISTS 且 DEL 原子返回"""
        if token in self.tokens:
            self.tokens.remove(token)
            return True
        return False

def submit(svc, token, payload):
    if not svc.consume(token):
        return "重复提交, 拒绝"
    return f"业务已处理: {payload}"

if __name__ == "__main__":
    svc = TokenService()
    token = svc.issue()
    print("首次提交:", submit(svc, token, {"sku": "x", "qty": 1}))
    print("重放同一 token:", submit(svc, token, {"sku": "x", "qty": 1}))
    print("伪造 token:", submit(svc, "deadbeef", {"sku": "x"}))
```

**追问**:
- token 什么时候发放?——渲染表单/进入支付页时,与页面会话绑定;不要在提交时才发,否则等于没防。
- 高并发下同 token 双击同时到呢?——DEL 与 EXISTS 在 Lua 中原子,两个并发请求只有一个拿到 True,另一个必然拒绝。

---
