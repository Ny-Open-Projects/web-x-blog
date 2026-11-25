---
title: [NODE-085] 复盘两个典型线上事故：内存泄漏与事件循环阻塞？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-085：复盘两个典型线上事故：内存泄漏与事件循环阻塞？
**答**：
- **案例一：内存泄漏**。现象：服务 RSS 每天 08:00 后线性上涨，三天 OOM 重启。定位：heap snapshot 对比发现数万 `Request` 对象被一个 Map 持有——根因是网关把"进行中请求"存入 Map 做去重，异常路径未清理。修复：finally 清理 + LRU 上限 + 水位告警。教训：**任何"登记后删除"结构必须有兜底清理与容量上限**。
- **案例二：事件循环阻塞**。现象：晚高峰 P99 从 80ms 飙到 2s，下游无异常、CPU 800%（8 核打满）。定位：`monitorEventLoopDelay` 高 + clinic flame 显示热点在 `JSON.parse`——某接口把 8MB 的聚合结果 parse/stringify。修复：下游改流式透传（不落地 JS 对象）、大结果直接 pipe、限制 body 上限。教训：**同步序列化是隐形 CPU 杀手，接口体量要有上限**。
- 通用复盘框架：时间线 → 现象 → 定位手段（监控指标 → 剖析工具 → 根因）→ 修复 → 预防（告警阈值、代码规范、压测门禁）。

```javascript
// 案例一修复：带兜底清理的请求去重表
class RequestTracker {
  constructor({ maxEntries = 10000, ttlMs = 60000 }) {
    this.entries = new Map();       // key → { resolve, timer }
    this.maxEntries = maxEntries;
    this.ttlMs = ttlMs;
  }
  register(key) {
    if (this.entries.size >= this.maxEntries) {
      // 容量上限兜底：淘汰最旧，防异常路径泄漏拖垮内存
      const oldest = this.entries.keys().next().value;
      this.evict(oldest, 'capacity');
    }
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => this.evict(key, 'ttl'), this.ttlMs); // TTL 兜底：异常路径也清理
      this.entries.set(key, { resolve, timer });
    });
  }
  complete(key, value) {
    const entry = this.entries.get(key);
    if (entry) { clearTimeout(entry.timer); entry.resolve(value); this.entries.delete(key); }
  }
  evict(key, reason) {
    const entry = this.entries.get(key);
    if (entry) { clearTimeout(entry.timer); entry.reject(new Error(`request evicted: ${reason}`)); }
    this.entries.delete(key);
  }
}

// 案例二修复 + 防护：响应体量上限 + 流式透传
app.get('/api/aggregation', async (ctx) => {
  const upstream = await callDownstream(ctx.query.url);
  const size = Number(upstream.headers.get('content-length') || 0);
  if (size > 2 * 1024 * 1024) {
    // 超过 2MB：不 parse 不 stringify，直接流式转发（零 CPU 序列化）
    ctx.set('content-type', upstream.headers.get('content-type'));
    for await (const chunk of upstream.body) ctx.res.write(chunk);
    return ctx.res.end();
  }
  ctx.body = await upstream.json();   // 小响应才走对象操作
});
```
