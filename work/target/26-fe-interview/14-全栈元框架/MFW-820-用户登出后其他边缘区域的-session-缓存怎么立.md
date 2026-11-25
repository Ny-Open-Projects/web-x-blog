---
title: [MFW-820] 用户登出后其他边缘区域的 session 缓存怎么立即失效
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-820：用户登出后其他边缘区域的 session 缓存怎么立即失效

**答**：
- 结论：登出是「全局失效」事件：写一条短 TTL 的失效记录（userId → logoutAt）到全球复制的 KV；各区读 session 时比对 session.iat 与 logoutAt，早于登出时间即失效。
- 兜底：失效记录复制有窗口，靠「短 TTL session + 关键操作二次校验」把窗口压到可接受。
- 追问钩子：为什么不用 Pub/Sub 推失效？——跨区推送不可靠且顺序无保证，时间戳比较更稳。

```javascript
// 登出：在全球复制 KV 写失效时间戳
async function logout(userId) {
  const now = Date.now();
  await globalKV.set('logout:' + userId, now, { ttl: 86400 });
  await clearLocalSession();
}

// 各区读 session：比较签发时间与登出时间
async function readSession(req) {
  const s = await edgeKV.get('sess:' + req.sid);    // 本区缓存
  if (!s) return null;
  const logoutAt = await globalKV.get('logout:' + s.uid);
  if (logoutAt && s.iat < logoutAt) {               // 早于登出 → 失效
    await edgeKV.del('sess:' + req.sid);
    return null;
  }
  return s;
}
// 关键操作（支付/改密）再向主库二次校验，兜住复制窗口
```
