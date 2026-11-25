---
title: [NODE-816] 笔试题——实现网关请求去重（相同请求合并转发）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-816：手写请求去重

**需求与边界**：
- 需求：网关请求去重（SCN-NODE-691 网关版）——① 相同请求合并（URL+方法+用户 hash——幂等 GET 的并发合并）；② 响应分发（首个响应分发给所有等待者）；③ 范围控制（只合并幂等 GET——非幂等不合并）；④ 命中率监控（合并收益可见）。
- 边界：① 请求 fingerprint 的键完整性（headers 影响响应的——Vary 联动，SCN-NODE-718）；② 响应缓存的隐私（用户级——不跨用户合并，SCN-NODE-692 授权红线）；③ 等待者超时（首响应慢——全部超时，退避重试）。

**答**：
```javascript
const inflight = new Map();
function dedupeMiddleware({ maxWait = 3000 } = {}) {
  return (req, res, next) => {
    if (req.method !== 'GET') return next();           // 只合并幂等 GET（SCN-NODE-691）
    const key = sha256([req.url, req.grayBucket, req.user?.id ?? 'anon'].join('|'));   // 用户级（不跨用户——SCN-NODE-692）
    const pending = inflight.get(key);
    if (pending) {                                     // 等待者：共享响应
      pending.waiters.push(res);
      telemetry.count('dedupe-hit');
      pending.timeout.refresh?.();
      return;
    }
    const entry = { waiters: [res] };                  // 首请求
    inflight.set(key, entry);
    const timer = setTimeout(() => finishAll(entry, 504), maxWait);   // 等待者超时（SCN-NODE-691）
    res.on('finish', () => {                           // 首响应分发
      clearTimeout(timer);
      entry.waiters.forEach(w => w !== res && pipeResponse(w, res));   // 响应克隆分发
      inflight.delete(key);
    });
    next();
  };
}
```

**评分点**:
- 只合并幂等 GET（非幂等不合并——SCN-NODE-691 边界）。
- 用户级键不跨用户（隐私——SCN-NODE-692 红线）。
- 首响应克隆分发 + 等待者超时。
- 命中率监控（收益可见）。
