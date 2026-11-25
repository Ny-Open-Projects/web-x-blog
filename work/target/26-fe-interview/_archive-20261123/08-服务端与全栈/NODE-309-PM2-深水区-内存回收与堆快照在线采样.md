---
title: [NODE-309] PM2 深水区：内存回收与堆快照在线采样？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-309：PM2 深水区：内存回收与堆快照在线采样？
**答**:
- 内存异常响应流：RSS 告警 → 在线采样（--inspect 或 v8.startCoverage/heapsnapshot 信号触发）→ snapshot diff 定位 → 修复 → max_memory_restart 兜底。
- 在线堆快照：给进程发 SIGUSR2（自写 handler 调 v8.writeHeapSnapshot）——不停机采样，注意采样本身阻塞主线程几秒（低峰执行）。
- 快照对比三看：constructor 分组增长（泄漏对象类型）、retainer 链（谁持有）、字符串/闭包堆积。
- 长期防护：每日定时快照入库对比趋势（泄漏早期发现）。

```javascript
// SIGUSR2 触发堆快照
process.on('SIGUSR2', () => {
  const v8 = require('node:v8');
  const file = `/tmp/heap-${process.pid}-${Date.now()}.heapsnapshot`;
  v8.writeHeapSnapshot(file);
  upload(file);                                    // 采样后自动上传分析平台
});
// 配套 RSS 监控
setInterval(() => {
  const rss = process.memoryUsage().rss / 1e6;
  metrics.gauge('rss', rss);
  if (rss > 600) report('rss-high');               // 快照触发条件
}, 10_000);
```
