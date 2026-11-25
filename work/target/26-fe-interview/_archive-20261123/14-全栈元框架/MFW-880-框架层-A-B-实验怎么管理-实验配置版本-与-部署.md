---
title: [MFW-880] 框架层 A/B 实验怎么管理「实验配置版本」与「部署版本」的正交
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-880：框架层 A/B 实验怎么管理「实验配置版本」与「部署版本」的正交

**答**：
- 结论：实验配置（谁能看到哪个变体）应与代码部署版本解耦——变体逻辑预埋在代码里，配置只控制流量分配，这样改实验不必重新发版。
- 落地：代码用 feature flag 包裹变体分支，配置中心下发分桶规则；部署版本变化时变体逻辑仍在，实验可独立启停。
- 追问钩子：预埋变体代码不会让包变大吗？——会，长期需用实验清理机制移除过期分支（对应 SRP 中的清理门禁）。

```javascript
// 代码里预埋两个变体（部署版本的一部分）
function Checkout() {
  const variant = useExperiment('checkout_layout');    // 从配置读变体
  return variant === 'B' ? <CheckoutB/> : <CheckoutA/>;  // 逻辑固定
}
// 配置中心：只控制流量，改实验不发版
const config = await fetchExperimentConfig('checkout_layout');
// { version: 7, buckets: { A: 0.9, B: 0.1 } } —— 独立调整
// 实验结束 → 清理 checkout_layout 相关分支代码
function resolveExperiment(name, userId) {
  const cfg = experiments[name];             // 当前生效配置（独立于部署版本）
  const bucket = hash(userId + cfg.salt) % 1000 / 1000;
  let acc = 0;
  for (const [variant, weight] of Object.entries(cfg.buckets)) {
    acc += weight;
    if (bucket < acc) return variant;
  }
  return 'A';
}
// 改 buckets 只改配置、不重新发版；部署版本里的变体逻辑保持不变
console.log(resolveExperiment('checkout_layout', 'u123'));
```
