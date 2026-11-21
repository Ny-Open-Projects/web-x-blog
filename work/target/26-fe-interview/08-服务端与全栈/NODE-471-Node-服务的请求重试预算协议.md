---
title: [NODE-471] Node 服务的重试预算协议（全链路重试防风暴）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-471：重试预算协议
**答**:
- 重试风暴：上游故障时每层都重试 → 重试流量放大（3 层 × 3 次 = 27 倍）打垮本来就脆弱的下游。重试预算协议：全链路重试总额受控 + 每层有"重不重"的协商。
- 预算机制：每服务设重试预算（重试请求量 ≤ 正常量的 10%——超预算后本层停止重试，快速失败）；预算在网关/链路层统一（不是每层独立 3 次的算术叠加）。
- 重试协商头：上游告知下游"我会重试"（x-retry-intent: no / attempts-left: 2）——下游据此收紧自己的重试（父链路只剩 1 次机会时，本层不再重试，把机会留给更上层 OR 反之按策略）；与 deadline 传播（NODE-377）配合：剩余时间不够一次完整重试就不重试。
- 重试安全：只幂等操作重试（NODE-381 幂等键让 POST 也可重试）、重试退避 + 抖动（防同步重试波）、重试与熔断联动（熔断打开期间不重试 NODE-352）。
- 观测：重试率按层分布（重试率异常升高是依赖故障的早期信号——比错误率更早）、预算耗尽事件（说明真的故障了）。
```javascript
// 层级重试协商
async function callWithBudget(url, { attemptsLeft, deadline }) {
  if (attemptsLeft <= 1 || deadline.remaining() < rt(url) * 2)   // 没预算/没时间
    return fetch(url, { headers: { 'x-retry-intent': 'no' } });   // 通知下游别指望我重试
  try { return await fetch(url, { headers: { 'x-attempts-left': attemptsLeft - 1 } }); }
  catch (e) { return retryable(e) ? callWithBudget(url, { attemptsLeft: attemptsLeft - 1, deadline }) : throw e; }
}
```
