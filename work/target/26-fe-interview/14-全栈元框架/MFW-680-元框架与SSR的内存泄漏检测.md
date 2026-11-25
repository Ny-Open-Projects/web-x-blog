---
title: [MFW-680] SSR 的内存泄漏检测
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-680：SSR 内存泄漏检测

**答**:
- SSR server 的内存泄漏源：1) **模块级缓存无限增长**（Map/Set 的 module-level cache——无上限：每请求写入 → 内存线性增长 RBL-619 LRU 的缺失）；2) **事件监听器未清理**（middleware/组件的全局 listener——每请求 addEventListener 无 removeEventListener）；3) **闭包捕获**（组件的闭包引用大对象——GC 无法回收）；4) **流未关闭**（未消费的 ReadableStream——缓冲堆积 RBL-505 背压）。
- 检测手段：1) **进程内存曲线**（RSS 随时间增长不回落——泄漏信号 RBL-569 内存画像）；2) heap snapshot diff（两次 snapshot 的对象计数差——增长类型定位（Map/Array/Closure））；3) **泄漏类型判定**（增长曲线斜率 × 流量相关性：随请求增长 = 每请求泄漏；随时间增长 = 定时器泄漏）。
- SSR 特有的缓解：worker 重启策略（内存到阈值 → 优雅重启——进程回收兜底——与「修复泄漏」不冲突（重启是缓解，修复是根治））。
- 追问钩子：为什么「模块级缓存」是 SSR 内存泄漏的头号来源且 LRU 是唯一解？——module-level Map = 进程存活期间永不 GC（引用持有）；每请求写入 → O请求数增长（一天 100 万请求 = 100 万条目）；LRU（cap + 淘汰）是唯一解：cap 上限（内存预算）+ 淘汰（旧条目回收）；TTL 兜底（逻辑过期——两层 RBL-619）；「module-level mutable in SSR」的统一治理：缓存用 LRU、状态用 ALS（RBL-657）、定时器用清理——每类泄漏的模式化修复。

```typescript
// 内存泄漏检测（进程内）
const memoryCurve: number[] = [];
setInterval(() => {
  memoryCurve.push(process.memoryUsage().rss / 1024 / 1024);
  if (memoryCurve.length > 100) {
    const slope = linearSlope(memoryCurve);              // 增长斜率
    if (slope > 1) warn(`RSS 增长 ${slope.toFixed(1)}MB/采样——疑似泄漏`);
    memoryCurve.shift();
  }
}, 30000);
// heap snapshot diff（诊断）
// kill -USR2 <pid> → heapdump → 两次对比（Map 增长最多的类型 = 泄漏源）
// LRU 兜底（RBL-619）
const requestCache = lru(10000, 60000);                  // 上限 1 万 + 1min TTL
// worker 重启缓解（PM2/Docker 健康检查）
// healthcheck: memoryUsage.rss > 1.5GB → restart
```
