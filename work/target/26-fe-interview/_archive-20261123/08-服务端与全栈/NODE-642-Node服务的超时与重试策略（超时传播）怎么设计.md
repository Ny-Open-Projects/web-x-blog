---
title: [NODE-642] Node 服务的超时与重试策略（超时传播）怎么设计？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-642：超时与重试怎么设计？
**答**：
- 超时传播：入口请求的总 deadline 逐层递减传递（BFF 总预算 2s → 下游各 800ms，剩余预算动态分配）——上游超时 ≤ 下游剩余，否则上游放弃了下游还在白干（资源浪费 + 响应丢失）。
- AbortController 贯穿：Node 17+ fetch/axios 支持 signal——deadline 生成 AbortSignal，透传给每个下游调用；超时即取消（取消传播到 socket）。
- 重试纪律：只重试幂等请求（GET/幂等写——幂等键）；指数退避 + 抖动；重试预算（总重试时间不超过剩余 deadline）；重试风暴防御（按上游限重试率）。
- 超时分级：连接超时（短）/响应超时（中）/总超时（入口）——三级分离，每级有监控（超时率按级统计）。
- 追问钩子：为什么「deadline 剩余量」比「固定每层超时」更好——固定超时（每层都 3s）在多层链中总耗时失控（3 层 × 3s = 9s > 入口 5s）；剩余量传递保证整链总耗时 ≤ 入口 deadline，且前层快完成后层拿到更多预算——预算制让超时成为「资源分配」问题。

```javascript
async function withDeadline(fn, deadlineMs) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), deadlineMs);
  try { return await fn(ctrl.signal); }                // signal 透传下游
  finally { clearTimeout(timer); }
}
// BFF：总 2000ms → 下游 A 800ms，A 完成后 B 拿剩余
const remaining = deadline - (Date.now() - start);
```
