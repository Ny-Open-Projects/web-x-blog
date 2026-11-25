---
title: [MFW-821] 笔试：手写跨区会话黑名单的 gossip 合并器
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-821：笔试：手写跨区会话黑名单的 gossip 合并器

**答**：
- 结论：各区独立维护被登出的 session 黑名单（sid → logoutAt），定期 gossip 合并；合并必须幂等、单调（时间只增不减）， gossip 才能收敛。
- 关键：保留更大的 logoutAt 防时钟回拨/重复失效；按 TTL 清理过期项，避免无限增长。
- 追问钩子：为什么不用 Pub/Sub 推失效？——跨区推送不可靠且顺序无保证，时间戳比较 + gossip 更稳。

```javascript
function mergeBlacklist(local, remote, now = Date.now(), ttl = 86400e3) {
  const out = new Map(local);
  for (const [sid, ts] of remote) {
    if ((out.get(sid) ?? 0) < ts) out.set(sid, ts);   // 单调：取更大 logoutAt
  }
  for (const [sid, ts] of out) {
    if (now - ts > ttl) out.delete(sid);              // TTL 清理
  }
  return out;
}
function isLoggedOut(bl, sid, sessIat) {
  const t = bl.get(sid);
  return t !== undefined && sessIat < t;             // 签发早于登出 → 失效
}

// 自测：A、B 两区 gossip 合并
let zoneA = new Map([['s1', 100]]);
let zoneB = new Map([['s1', 90], ['s2', 110]]);
zoneA = mergeBlacklist(zoneA, zoneB, 120);
console.log(zoneA.get('s1') === 100 && zoneA.has('s2')); // true
console.log(isLoggedOut(zoneA, 's1', 95));              // true
console.log(isLoggedOut(zoneA, 's1', 105));             // false（重登后签发）
```

**评分点**：
- 合并单调：保留更大 logoutAt，满足幂等/交换（gossip 收敛基础）
- 用 iat < logoutAt 判定失效，正确处理重新登录后的 session
- TTL 过期清理避免黑名单无限增长
- 能点出 Pub/Sub 跨区不可靠 vs 时间戳比较的稳定性（加分）
