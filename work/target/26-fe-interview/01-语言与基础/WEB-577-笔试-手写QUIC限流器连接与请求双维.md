---
title: [WEB-577] 笔试：手写 QUIC 双维限流器（连接 + 请求速率）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-577：笔试：手写 QUIC 双维限流器（连接 + 请求速率）

**答**：实现 `QuicLimiter`：① 连接维度：每 CID 在活跃连接表内，活跃连接数超上限时拒绝新连接（返回 `connection-refused`）；② 请求维度：每 CID 滑动窗口 1s 限 N 个请求（环桶计数）；③ IP 维度兜底：单 IP 每 10s 最多建立 5 个新连接（防 CID 刷新绕过）；④ 满足任一限制即拒绝并返回原因。写出核心实现与过期清理策略。

```javascript
class QuicLimiter {
  constructor({ maxConns, maxReqPerSec, maxNewConnsPer10s }) {
    this.maxConns = maxConns; this.maxReq = maxReqPerSec; this.maxNew = maxNewConnsPer10s;
    this.active = new Map();   // cid -> lastSeen
    this.reqWin = new Map();   // cid -> [ts...]
    this.ipNew = new Map();    // ip -> [ts...]
  }
  onConnect(cid, ip) {
    const now = Date.now();
    // IP 新建连接限速
    const arr = (this.ipNew.get(ip) ||= []);
    while (arr.length && now - arr[0] > 10_000) arr.shift();
    if (arr.length >= this.maxNew) return 'ip-conn-limit';
    // 活跃连接上限
    if (this.active.size >= this.maxConns) return 'conn-limit';
    this.active.set(cid, now);
    arr.push(now);
    return null;
  }
  onRequest(cid) {
    const now = Date.now();
    const arr = (this.reqWin.get(cid) ||= []);
    while (arr.length && now - arr[0] > 1000) arr.shift();
    if (arr.length >= this.maxReq) return 'req-rate-limit';
    arr.push(now);
    this.active.set(cid, now); // 刷新活跃
    return null;
  }
  cleanup(idleMs = 60_000) {
    const now = Date.now();
    for (const [cid, ts] of this.active) if (now - ts > idleMs) {
      this.active.delete(cid); this.reqWin.delete(cid);
    }
  }
}
```

**评分点**：
- 双维（CID 连接/请求）+ IP 兜底三维设计，识破 CID 刷新攻击面
- 滑动窗口用时间戳队列实现且边界清理正确
- 活跃表基于最后活跃时间过期清理，防止内存泄漏
- 拒绝原因可区分，支撑监控归因
