---
title: [BLD-265] 产物体积预算的执行（maxSize 治理）怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-265：体积预算执行怎么做？
**答**：
- 预算层级：入口总预算（首屏 JS 总量）、单 chunk 预算、增量预算（PR diff 上限——Ratchet，SCN-ENG-291）——三层防线。
- 执行点：构建后测量 → 预算比对 → 超限动作（阻断/警告/需审批——按预算级别）。
- 预算的制定依据：页面性能目标反推（TTI 目标 → JS 预算 = 目标 − 网络耗时 − 解析耗时）——预算不是拍脑袋（SCN-ENG-235 路由级预算）。
- 例外通道：超预算审批（带理由与还债计划）——例外记录让「预算执行率」可度量。
- 追问钩子：为什么入口预算要从「性能目标反推」而不是按现状定——按现状定预算（现在 500KB 就定 500KB）只是把现状合法化，没有优化牵引力；从 TTI 目标反推（比如 JS 预算 300KB）能让预算本身成为优化驱动力——预算的价值在于「比现状更小」才有治理意义。

```javascript
// 反推预算
const budget = (ttiTargetMs, networkMs, parseMs) => ttiTargetMs - networkMs - parseMs;
// 例: TTI 2.5s - 网络 1.2s - 解析 0.8s = JS 预算 0.5s ≈ 300KB gzip（4G）
// 执行
const measured = measureGzip(manifest.entry.chunks);
if (measured > budget) gate({ action: 'block-or-approve', over: measured - budget });
```
