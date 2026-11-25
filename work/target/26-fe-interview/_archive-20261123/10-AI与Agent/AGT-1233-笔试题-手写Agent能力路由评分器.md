---
title: [1233] 笔试手写：实现按通过率与成本的能力选择（带灰度约束）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent]
type: 笔试题
---

## 1233：笔试手写：实现按通过率与成本的能力选择（带灰度约束）

**需求**：实现 select(registry, cap, ctx)：registry 为 { [cap]: [{ name, status, stats: { passRate, costMs, canaryPct } }] }。规则：status==='ok' 才参选；默认按 passRate 降序、costSensitive 时按 passRate/costMs；canaryPct > 0 的实现以该概率被随机选中（灰度探路——rand 注入）；无实现抛错。返回选中对象与 { canary: bool }（是否为灰度命中）。

```js
function select(registry, cap, ctx = {}, rand = Math.random) {
  const impls = (registry[cap] || []).filter(i => i.status === 'ok');
  if (!impls.length) throw new Error('no impl: ' + cap);
  // 灰度探路：有 canaryPct 的实现按概率优先试用
  const canaries = impls.filter(i => i.canaryPct > 0);
  for (const c of canaries) {
    if (rand() < c.canaryPct) return { ...c, canary: true };
  }
  const score = ctx.costSensitive
    ? i => i.stats.passRate / i.stats.costMs
    : i => i.stats.passRate;
  const sorted = [...impls].sort((a, b) =>
    score(b) - score(a) || (a.name < b.name ? -1 : 1));
  return { ...sorted[0], canary: false };
}
const reg = { search: [
  { name: 'es', status: 'ok', stats: { passRate: 0.9, costMs: 100 }, canaryPct: 0 },
  { name: 'vec2', status: 'ok', stats: { passRate: 0.88, costMs: 90 }, canaryPct: 0.1 },
]};
console.log(select(reg, 'search', { costSensitive: true }, () => 0.05));
// vec2 命中灰探（0.05 < 0.1）canary true
console.log(select(reg, 'search', { costSensitive: true }, () => 0.5)); // es
```

**评分点**：
- 灰度探路逻辑（rand < canaryPct 命中新实现——数据收集通道）
- canary 命中标记（行为差异可观测）
- 评分与稳定排序；空实现抛错
- 能讨论：canary 的表现数据回流（passRate 更新——自优化路由）、灰度挂的自动回退

