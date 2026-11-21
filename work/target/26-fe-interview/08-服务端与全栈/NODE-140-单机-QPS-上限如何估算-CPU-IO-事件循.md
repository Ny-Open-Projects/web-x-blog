---
title: [NODE-140] 单机 QPS 上限如何估算（CPU/IO/事件循环三瓶颈）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-140：单机 QPS 上限如何估算（CPU/IO/事件循环三瓶颈）？
**答**：
- 上限 = **min(计算瓶颈, IO 瓶颈, 事件循环瓶颈)**，逐层压测找短板，公式只做粗估。
- 计算型：压出单实例 QPS 后线性扩展到 `min(cluster 数, 物理核数)`；IO 型：受连接池与下游吞吐限制，`QPS ≈ 下游可用吞吐 / 每请求下游调用数`。
- 事件循环是 Node 特有信号：lag P99 < 100ms 时 CPU 通常 < 80%，超过即接近极限（NODE-105）。
- 方法论：**压测优先于公式**——先压无依赖 ping 测框架上限，再压全链路找差值在哪一层；上线后用真实流量校准并写进容量预案（NODE-099）。

```javascript
// 粗估模型（缓存命中为主的 BFF）
function estimateQps({ singleCoreQps = 1200, cores = 4, targetCpu = 0.7,
  downstreamQps = 8000, callsPerReq = 3 } = {}) {
  const cpuBound = singleCoreQps * cores * targetCpu; // 1200*4*0.7 = 3360
  const ioBound = downstreamQps / callsPerReq;        // 8000/3 ≈ 2666
  return Math.min(cpuBound, ioBound);                 // → 2666，IO 是短板
}
console.log('预估单机 QPS =', estimateQps());

// 实测校准（压测法，比公式可信）：
// autocannon -c 200 -d 60 --latency http://localhost:3000/api/home
// 分层压：ping（框架上限）→ 单依赖 → 全链路，差值即瓶颈层
const BASELINE = { qps: 2666, p99: 300 }; // 上线后用真实流量修正并固化
// 容量预案：目标流量 / 单机实测 = 所需实例数 × 1.5 冗余
```
