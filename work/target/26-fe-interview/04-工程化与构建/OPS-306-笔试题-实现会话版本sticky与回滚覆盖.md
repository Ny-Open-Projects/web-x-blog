---
title: [OPS-306] 笔试题——实现会话版本 sticky（跨请求版本一致 + 回滚覆盖）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-306：手写会话 sticky

**需求与边界**：
- 需求：会话首次分配版本后 sticky 到会话结束（24h 过期）；紧急回滚覆盖 sticky（全量回旧版）；渗透率双口径（新会话渗透 vs 全量渗透，SCN-OPS-244）；sticky 版本与当前灰度组核对（用户换组时的处理）。
- 边界：① sticky 存储按会话（cookie 加密/服务端 session）；② 过期后会话重新分流；③ sticky 覆盖事件记录（多少用户被回滚覆盖——影响面评估）。

**答**：
```javascript
function resolveVersion(session, user, grayState, { ttl = 24 * 3600_000 } = {}) {
  // 紧急回滚覆盖 sticky
  if (grayState.emergencyRollback) {
    if (session.versionStamp && session.versionStamp !== grayState.stable)
      metrics.count('sticky-overridden');              // 覆盖影响面
    return grayState.stable;
  }
  // sticky 命中且未过期
  if (session.versionStamp && Date.now() - session.assignedAt < ttl)
    return session.versionStamp;
  // 新会话分流
  const v = grayState.split(user);
  session.versionStamp = v;
  session.assignedAt = Date.now();
  return v;
}
function penetration(sessionStats, grayState) {
  return {
    newSessionPct: sessionStats.newWithTarget / sessionStats.newTotal,   // 新会话渗透
    overallPct: sessionStats.withTarget / sessionStats.total,            // 全量渗透（含 sticky 滞后）
    note: overall < newSessionPct && 'sticky 滞后中，放量进度看 newSession 口径',
  };
}
```

**评分点**:
- 回滚覆盖 sticky + 覆盖计数（影响面评估）。
- TTL 过期重新分流（sticky 不永续）。
- 双口径渗透率（新会话 vs 全量——放量进度的正确读法）。
- 新会话分流仅在无 sticky 时执行（一致性优先）。
