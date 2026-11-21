---
title: [NODE-509] Node 服务的边缘函数（BFF 能力下沉 Edge）边界如何判断？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-509：边缘函数下沉边界
**答**:
- 什么时候下沉 Edge：离用户近的轻逻辑（入口路由/鉴权前置/AB 分桶/HTML 改写/轻缓存聚合——ARC-375 边缘边界）。判断标准：无状态 + 低计算 + 高频 + 时延敏感 → Edge 有收益；有状态/重计算/需要内部网络 → 留在 BFF。
- 下沉后的架构：Edge 层职责收敛（只做"请求改写与路由"不做业务——业务逻辑全留 BFF，防 Edge 逻辑膨胀失控）、Edge 与 BFF 的协议（Edge 转发携带上下文头——身份/灰度已在 Edge 注入 BFF 复用 NODE-496）。
- 一致性挑战：Edge 分桶与 BFF 分桶同源（同 hash 算法——否则前后半链路不同桶 NODE-497）、Edge 缓存与 BFF 失效协同（NODE-508 purge 链路含 Edge 层）。
- 成本与运维：Edge 函数的运行限制（CPU 时间/内存/包体——重逻辑跑不动）、边缘代码发布节奏（与 BFF 联动发布——版本兼容矩阵）、Edge 可观测（边缘层的 trace/日志采集——链路完整 ARC-291）。
- 演进决策：先小范围下沉验证（一个轻接口）→ 收益度量（TTFB 改善/回源率下降）→ 逐步扩面——"为下沉而下沉"是反模式。
```javascript
// Edge 判定清单
const edgeCandidates = {
  'gray-bucket': { stateful: false, compute: 'low', latency: 'critical', verdict: 'edge' },
  'order-agg':   { stateful: true,  compute: 'mid',  latency: 'normal',  verdict: 'bff' },
  'html-rewrite':{ stateful: false, compute: 'low',  latency: 'critical', verdict: 'edge' }
};
// Edge 只做改写与路由：ctx.set('x-uid', jwt.uid); return fetch(bffUrl)  // 业务全在 BFF
```
