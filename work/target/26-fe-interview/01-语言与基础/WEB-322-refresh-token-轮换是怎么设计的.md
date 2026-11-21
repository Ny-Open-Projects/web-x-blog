---
title: [WEB-322] refresh token 轮换是怎么设计的？为什么要轮换？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 笔试题
---

## WEB-322：refresh token 轮换是怎么设计的？为什么要轮换？
**答**：
- 轮换：每次用 refresh 换新 access 时，旧的 refresh 作废、发新的；refresh 只能用一次。
- 价值：refresh 若被盗，合法用户下次使用会"撞车"，服务端发现 refresh 已用过 → 判定泄露 → 吊销该用户全部会话。
- 实现要点：refresh 存库（或带 jti 的 JWT）+ 一次性标记；并发请求同时刷新要加锁/复用同一次刷新结果。

```javascript
const store = new Map(); // jti -> { userId, used }
function refresh(jti) {
  const rec = store.get(jti);
  if (!rec || rec.used) {
    revokeAllSessions(rec?.userId); // 疑似泄露，全员下线
    return { error: 'refresh 已使用，会话全部吊销' };
  }
  rec.used = true;
  const newJti = crypto.randomUUID();
  store.set(newJti, { userId: rec.userId, used: false });
  return { access: sign({ sub: rec.userId, exp: now() + 900 }), refresh: newJti };
}
console.log('用过即作废 + 撞车即吊销');
```

**评分点**：
- 结论先行，能一句话说清核心机制
- 要点覆盖主流程与关键分支（异常/并发/边界）
- 代码可运行且体现安全或性能意识
- 能主动说出"工程上怎么选"与常见坑
