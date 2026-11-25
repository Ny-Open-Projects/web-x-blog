---
title: [MFW-650] 服务端埋点的事件收集端点
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-650：服务端埋点收集端点

**答**:
- 埋点收集端点（route handler）的生产要求：1) **fire-and-forget**（收集后立即返回——处理异步化（队列/批量写——同步写 DB 阻塞响应 RBL-569）；2) **批量**（client 端 batch（N 事件一次发——navigator.sendBeacon keepalive）+ server 端批量写（队列 flush——写放大控制）；3) **schema 校验**（入口校验事件 schema（脏数据拒绝 RBL-645 的入口版）；4) **隐私**（IP 截断/无 PII——匿名聚合 RBL-601；5) 限流（防滥用：事件洪水的 DDoS 面 RBL-607）。
- sendBeacon 的语义：页面卸载时的可靠发送（keepalive fetch——不阻塞卸载；「离开页面也送达」的埋点保障）。
- 收集端点的容量：埋点 QPS = 页面 PV × 事件数（大促 10 万 PV × 10 事件 = 100 万 QPS——收集端的容量与降级（过载丢采样——全量 vs 采样 RBL-938 错误采样的埋点版）。
- 追问钩子：为什么「埋点收集要 fire-and-forget + 批量写」而不是「同步写 DB」？——同步写：收集端点延迟 = DB 写延迟（用户无感但 server 占用——并发上限被 DB 拖垮）；fire-and-forget：响应即回（收集端无限吞吐——DB 写异步缓冲）；批量：100 万事件/秒 = 100 万写/秒（单条写不可行）→ 批量 flush（1000 事件/批 = 1000 写/秒）；「收集与处理的解耦」是埋点架构的基本盘——与日志/监控的采集管线同构（RBL-938）。

```typescript
// 收集端点（fire-and-forget + 批量）
// app/api/collect/route.ts
const buffer: Event[] = [];
let flushTimer: NodeJS.Timeout | null = null;
function scheduleFlush() {
  if (flushTimer) return;
  flushTimer = setTimeout(async () => {
    flushTimer = null;
    const batch = buffer.splice(0, buffer.length);
    if (batch.length) await writeToWarehouse(batch);     // 批量写（队列/warehouse）
  }, 5000);                                              // 5s flush 窗口
}
export async function POST(req: Request) {
  const events = await req.json();                       // batch 格式
  for (const e of events) {
    if (!validateEvent(e)) continue;                     // schema 校验：脏数据丢弃
    buffer.push(minimize(e));                            // 最小化（IP 截断/无 PII）
  }
  scheduleFlush();
  return new Response(null, { status: 204 });            // 立即返回——fire-and-forget
}
// client 批量发送（sendBeacon）
const queue: Event[] = [];
setInterval(() => {
  if (!queue.length) return;
  navigator.sendBeacon('/api/collect', JSON.stringify(queue.splice(0, queue.length)));
}, 10000);                                               // 10s 批量
addEventListener('pagehide', () => navigator.sendBeacon('/api/collect', JSON.stringify(queue)));   // 卸载也送达
```
