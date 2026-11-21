---
title: [OPT-164] Session Replay 如何与性能数据关联，定位"慢会话"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-164：Session Replay 如何与性能数据关联，定位"慢会话"？

**答**：
- 单看指标知道"慢"，回放知道"怎么个慢法"：用户点了几次没反应、骨架屏卡了多久、白屏期间用户在干什么。关联方式是统一的 **sessionId + 时间轴**。
- 实现：回放录制（rrweb）与性能事件（LCP/INP/长任务/请求）共用 session 存储，性能事件作为 mark 写入回放时间轴，回放器上直接标出"此刻 LCP 发生"。
- 采样策略：全量录制成本高，按"慢会话优先"采样——LCP P90 以上、INP > 200ms、发生长任务风暴的会话优先上传回放。
- 隐私合规：输入框脱敏、token 类 DOM 不录制，回放存储设保留期。

```javascript
// 一一对应：rrweb 回放 + 性能事件写入同一时间轴（慢会话优先上传）
import { record } from 'rrweb';

const events = [];
let slowScore = 0;   // 会话"慢程度"打分，决定是否上传

record({
  emit: e => {
    events.push(e);
    if (events.length > 3000) events.splice(0, 500); // 环形缓冲防爆内存
  },
  maskInputOptions: { password: true, tel: true },     // 隐私脱敏
});

// 性能事件：作为自定义事件进时间轴 + 叠加慢分数
new PerformanceObserver(l => {
  for (const e of l.getEntries()) {
    events.push({ type: 'custom', tag: 'perf:lcp', timestamp: e.startTime, value: e.startTime });
    if (e.startTime > 4000) slowScore += 2;   // LCP 超 4s 加权
  }
}).observe({ type: 'largest-contentful-paint', buffered: true });

new PerformanceObserver(l => {
  const n = l.getEntries().length;
  events.push({ type: 'custom', tag: 'perf:longtask', count: n });
  slowScore += n;
}).observe({ type: 'longtask', buffered: true });

// 页面离开：慢会话才上传（快会话丢回放省存储）
addEventListener('pagehide', () => {
  if (slowScore < 3) return;                  // 阈值可按流量调整
  const sessionId = sessionStorage.sid;
  const blob = new Blob([JSON.stringify({ sessionId, slowScore, events })]);
  navigator.sendBeacon('/api/replay', blob);  // 服务端按 sessionId 可关联全部性能埋点
});
```
