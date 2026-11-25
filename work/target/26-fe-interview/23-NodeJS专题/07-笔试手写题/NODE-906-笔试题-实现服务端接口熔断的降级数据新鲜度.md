---
title: [NODE-906] 笔试题——实现熔断降级数据的新鲜度标注（缓存 age）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-906：手写新鲜度

**需求与边界**：
- 需求：降级数据新鲜度（SCN-NODE-690/联想-675）——① 降级数据的 age 标注（缓存写入时间——SCN-联想-675 陈旧标注）；② 前端展示（「数据截至 xx:xx」——SCN-联想-675）；③ 新鲜度的分级（<5min 轻微/5~30min 显著/超 30min 警示——SCN-联想-675 分级）；④ 降级数据的禁用场景（实时性敏感 UI——SCN-联想-675）。
- 边界：① age 的传播（缓存值带 ts——SCN-NODE-690）；② 分级阈值配置（SCN-NODE-663）；③ 降级 UI 的差异化（SCN-联想-830 语义映射）。

**答**：
```javascript
async function degradeWithFreshness(key, strategies) {
  for (const s of strategies) {
    const out = await tryStrategy(s, key);
    if (out) {
      const age = Date.now() - out.ts;                 // age 计算（SCN-联想-675）
      return { data: out.data, age,
        level: age < 5 * 60_000 ? 'fresh-ish' : age < 30 * 60_000 ? 'stale' : 'very-stale',
        marker: `X-Degraded: ${s.name};age=${Math.round(age / 60000)}min` };   // 分级标记
    }
  }
}
// 前端：very-stale → 隐藏实时性 UI（SCN-联想-830 语义映射）
```

**评分点**:
- age 计算 + 三级标注（SCN-联想-675）。
- 降级标记携带 age（SCN-NODE-690 双通道）。
- 分级阈值配置化（SCN-NODE-663）。
- 前端语义映射（SCN-联想-830）。
