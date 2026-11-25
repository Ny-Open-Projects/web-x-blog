---
title: [RBL-934] 综合深水：性能预算的分配算法——从 TTI 目标到各资源预算的自顶向下分配
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-934：综合深水：性能预算的分配算法——TTI 目标的自顶向下分配

**答**:
- 预算分配的两方向：自底向上（现状 +10% 宽松 RBL-662）vs **自顶向下**（目标 TTI → 反推各资源预算）：TTI 3s（P75 设备）= 网络（html 0.3s + DNS/TLS 0.5s）+ 渲染 0.7s + JS 执行 0.8s → **JS 传输预算 = 剩余 0.7s × 带宽 = ~90KB gzip**——自顶向下给出「科学依据的预算」，而不是「现状加宽容忍」。
- 分配的传递：总 JS 预算 → 入口预算（首屏）→ 各 chunk（按路由权重）→ 三方脚本配额（预留 20%——RBL-882 独立预算）；「预算的层级传递」让每个团队拿到可执行的数字。
- 预算与指标的校准闭环（RBL-880）：分配的假设（渲染 0.7s）要用 RUM 验证——假设错了预算就错；「预算推导表」记录每个参数来源（RUM P75/设备分布），可审计。
- 预算的动态性：设备分布随时间变化（低端机占比下降 → 预算可放宽）——年度校准 RBL-880。
- 追问钩子：为什么「自顶向下」比「自底向上」更可能推动真实优化？——自底向上的预算是「现状 + 容忍」（默认接受膨胀），自顶向下是「目标倒逼」（预算 < 现状时必须优化）——预算的政治学：它定义了「谁要为超标负责」；自顶向下的预算配上归因报告（RBL-739）让超标有「具体的优化路径」而非「抽象的更快」。

```javascript
// 自顶向下预算分配
function allocateBudget({ ttiTargetSec, networkSec, renderSec, jsExecSec, bandwidthKbps, thirdPartyShare = 0.2 }) {
  const jsTransferSec = ttiTargetSec - networkSec - renderSec - jsExecSec;
  if (jsTransferSec <= 0) throw new Error('时间预算不足——目标或假设需要调整');
  const totalJsKB = +(jsTransferSec * bandwidthKbps / 8).toFixed(0);   // KB(gzip)
  const thirdPartyKB = Math.floor(totalJsKB * thirdPartyShare);
  const firstPartyKB = totalJsKB - thirdPartyKB;
  return {
    derivation: `TTI ${ttiTargetSec}s - 网络${networkSec}s - 渲染${renderSec}s - 执行${jsExecSec}s = JS ${jsTransferSec}s`,
    totalJsKB, thirdPartyKB, firstPartyKB,
    entryKB: Math.floor(firstPartyKB * 0.6),             // 入口占大头
    routeChunksKB: firstPartyKB - Math.floor(firstPartyKB * 0.6),
  };
}
console.log(allocateBudget({ ttiTargetSec: 3, networkSec: 0.8, renderSec: 0.7, jsExecSec: 0.8, bandwidthKbps: 1000 }));
// JS 传输 0.7s × 125KB/s ≈ 87KB → 三方 17KB / 自有 70KB
```
