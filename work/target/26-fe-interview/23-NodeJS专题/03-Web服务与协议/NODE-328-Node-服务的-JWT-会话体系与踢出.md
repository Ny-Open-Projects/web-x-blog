---
title: [NODE-328] Node 服务的 JWT 会话体系与踢出？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-328：Node 服务的 JWT 会话体系与踢出？
**答**:
- JWT 双 token：access（短，15min）+ refresh（长，7d，带旋转）——refresh 旋转检测重放（旧 refresh 被用 → 全会话失效）。
- 踢出机制：JWT 无状态难撤销——服务端维护"会话版本号"（uid → version），JWT 带版本；踢出 = version++，校验时比对（Redis O(1)）。
- 权限变更联动：权限快照版本（ARC-230）与 token 版本联动——权限变了 token 仍有效但快照刷新。
- 实现取舍：高频校验走 JWT 本地验签（无网络），版本比对走 Redis 一次 GET——安全与性能平衡。

```javascript
// JWT 校验 + 版本踢出
async function verify(token) {
  const payload = jwt.verify(token, PUB_KEY);       // 本地验签（无网络）
  const ver = await redis.get(`sessver:${payload.uid}`);
  if (ver && +ver !== payload.ver) throw new SessionRevokedError();   // 版本不符：踢出
  return payload;
}
// 踢出（管理员/改密触发）：
async function kick(uid) { await redis.incr(`sessver:${uid}`); }    // version++ → 全设备失效
// refresh 旋转：
async function rotate(refresh) {
  const rec = await db.refreshToken.findUnique({ where: { token: hash(refresh) } });
  if (rec.used) { await kick(rec.uid); throw new ReplayError(); }    // 重放 → 全会话失效
  await db.refreshToken.update({ where: { id: rec.id }, data: { used: true } });
  return issueTokens(rec.uid);                       // 新 access + 新 refresh
}
```
