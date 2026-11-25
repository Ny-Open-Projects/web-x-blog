---
title: [TST-647] 笔试：实现 CSRF token 校验测试器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-647：笔试：实现 CSRF token 校验测试器

**题目**：实现 CsrfGuard：issue(userId,ttl) 签发一次性 token；verify(token,userId,now) 校验存在性、归属、过期、是否已使用，返回 {ok,why?}。校验通过后标记 used=true。

**答**：
- 校验三要素：token 存在、未过期、未被使用（一次性）。
- 服务端状态用 Map 模拟，记录 token 的过期时间与消费标记。
- 返回明确失败原因，便于生成测试报告。

```javascript
class CsrfGuard {
  constructor() { this.tokens = new Map(); }
  issue(userId, ttl = 60000) {
    const token = Math.random().toString(36).slice(2);
    this.tokens.set(token, { userId, expire: Date.now() + ttl, used: false });
    return token;
  }
  verify(token, userId, now = Date.now()) {
    const rec = this.tokens.get(token);
    if (!rec) return { ok: false, why: 'no-token' };
    if (rec.userId !== userId) return { ok: false, why: 'owner-mismatch' };
    if (rec.expire < now) return { ok: false, why: 'expired' };
    if (rec.used) return { ok: false, why: 'reused' };
    rec.used = true;
    return { ok: true };
  }
}
```

**评分点**：
- 四要素（存在/归属/过期/一次性）全覆盖
- 一次性消费防重放
- 失败原因枚举清晰
- 时间可注入便于测试
