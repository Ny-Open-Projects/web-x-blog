---
title: [ARC-287] AB 平台如何支持多变量实验：正交因子设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-287：AB 平台如何支持多变量实验：正交因子设计？
**答**：
- 多变量（如按钮颜色×文案×位置）的两种设计：全因子（2×2×2=8 组，样本要求大但能看交互效应）vs 分层正交（每个变量一个独立层，用户同时吃多个变量的组合，样本省但看不到变量间交互）。
- 选择原则：变量间可能有交互（位置影响文案效果）→ 全因子；变量明显独立 → 正交分层。平台按实验申报的"预期交互"自动建议设计。
- 前端实现：变量读取 API `exp.getValue('btn.color')` 组合各层结果；渲染时把组合值注入组件；埋点快照记录**完整组合指纹**（color=red&copy=B&pos=top），分析侧按指纹聚合。
- 防组合爆炸：平台限制同层实验数与变量数，组合数超阈值的申报需要统计评审。

```typescript
// 多变量读取与指纹
function fingerprint(uid) {
  return ['btn.color', 'btn.copy', 'btn.pos']
    .map(k => `${k}=${exp.getValue(k, uid)}`).join('&');
}
// 全因子组分配：组号 = factorA*4 + factorB*2 + factorC（3 因子 8 组）
function fullFactorial(uid, factors) {
  const n = factors.length;
  let g = 0;
  factors.forEach((f, i) => { if (bucketId(`f:${f}`, uid) % 2) g |= 1 << (n - 1 - i); });
  return g;                                    // 0~2^n-1 → 每组一个组合，可测交互效应
}
```
