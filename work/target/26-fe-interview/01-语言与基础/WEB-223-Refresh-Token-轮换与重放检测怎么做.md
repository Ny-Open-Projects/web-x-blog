---
title: [WEB-223] Refresh Token 轮换与重放检测怎么做？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-223：Refresh Token 轮换与重放检测怎么做？

**答**：
- 轮换（Rotation）：每次用 refresh 换新 access 时，旧 refresh 作废、发新的。目的：refresh 泄漏后攻击者只能用一次。
- 重放检测：refresh 存 Redis，带「是否已用」标记。正常流程：旧 refresh 换新 → 标记已用。若已用的 refresh 再次出现，说明泄漏——吊销该用户全部 token 强制重新登录（OAuth2 规范推荐做法）。
- 实现要点：已用判断必须原子（Redis SETNX / Lua），防止并发换新竞态都成功；token 携带 family ID，重放时可精准吊销整条链。
- 前端配合：refresh 请求失败立即登出跳转，不要无限重试；多标签页用 BroadcastChannel/Storage 事件共享新 token。

```javascript
// 服务端轮换 + 重放检测（Redis）
async function rotateRefresh(userId, oldToken) {
  const key = `refresh:${userId}:${oldToken}`;
  const isNew = await redis.set(key, 'used', 'NX', 'EX', 60);
  if (!isNew) {
    await redis.del(...await redis.keys(`refresh:${userId}:*`)); // 重放→全吊销
    throw new Error('token 重放，已强制下线');
  }
  const newRefresh = crypto.randomUUID();
  await redis.setex(`refresh:${userId}:${newRefresh}`, 7 * 86400, 'active');
  return { newRefresh, access: signAccess(userId) };
}
```
