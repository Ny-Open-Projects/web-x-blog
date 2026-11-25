---
title: [SCN-725] 分位数聚合口径怎么选（P50/P95/P99 与多级聚合误差）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-725：分位数聚合口径怎么选？
**答**：
- 主指标 P95 辅以 P50/P99：P50 反映典型体验、P95 是 SLO 常用档、P99 用于深水排查；只看一个分位数必被博弈（优化 P95 牺牲 P99 谁都不知）。
- 多级聚合误差：分钟级 P95 再聚合成小时级 P95 ≠ 真实小时 P95（分位数不可平均！）——正确做法是分钟级存 t-digest，小时级合并 digest 再取分位数。
- 口径卡写清：「P95」的计算对象（请求级/页面加载级/会话级）、合并算法、误差范围。
- 看板提示：跨粒度对比时标注「digest 合并无偏」vs「均值近似有偏」。
- 追问钩子：为什么分位数不能跨粒度平均——P95 的含义是 95% 个体低于此值，把每小时 P95 平均没有任何统计意义，慢请求集中在某小时会被稀释。

```javascript
// 正确的多级聚合：digest 合并
const minuteDigests = await tdstore.read(sliKey, minuteRange);
const hourDigest = TDigest.merge(minuteDigests);     // 合并后取分位：无偏
const trueP95 = hourDigest.quantile(0.95);
// 错误示范：
// const wrongP95 = mean(minuteDigests.map(d => d.quantile(0.95)));  // 有偏！
```
