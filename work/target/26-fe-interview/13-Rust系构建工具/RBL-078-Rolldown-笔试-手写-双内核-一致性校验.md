---
title: [RBL-078] 笔试：手写 dev/prod 产物一致性校验器（模块集合比对）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-078：笔试：手写 dev/prod 产物一致性校验器（模块集合比对）
**题目**：实现 checkParity(devStats, prodStats)：1) 比较两次构建的模块集合（path 集合差集）；2) dev 有 prod 无 → 报「dev-only 依赖」（prod 会被摇掉）；3) prod 有 dev 无 → 报「prod-only 依赖」（条件加载，dev 不感知，可能带隐藏副作用）；4) 输出差异清单与影响面；5) 只对业务模块（src/ 下）报差异，node_modules 忽略。

```javascript
function checkParity(devStats, prodStats, { sourcePattern = /^src\// } = {}) {
  const modOf = (stats) => {
    const set = new Set();
    for (const c of stats.chunks || [])
      for (const m of c.modules || [])
        if (sourcePattern.test(m)) set.add(m);
    return set;
  };
  const dev = modOf(devStats), prod = modOf(prodStats);

  const devOnly = [], prodOnly = [];
  for (const m of dev) if (!prod.has(m)) devOnly.push(m);
  for (const m of prod) if (!dev.has(m)) prodOnly.push(m);

  const impact = (list) => {
    // 影响 = 引用这些模块的入口（此处简化为模块数）
    return list.map(m => ({ module: m }));
  };
  return {
    devOnly: impact(devOnly),   // prod 下被摇除 → dev 可用 prod 404
    prodOnly: impact(prodOnly), // dev 不感知 → 带未验证代码上线
    summary: {
      devOnlyCount: devOnly.length,
      prodOnlyCount: prodOnly.length,
      pass: devOnly.length === 0 && prodOnly.length === 0,
    },
  };
}
module.exports = { checkParity };

// 场景：dev 用 import.meta.env.DEV 加载调试面板，prod 摇掉 → devOnly 面板
// 检查点：prodOnly = 0（防止未在 dev 验证过的代码上线）
```
**评分点**：
- 双集合差集方向语义（dev-only vs prod-only）。
- sourcePattern 过滤业务模块（噪音治理）。
- pass 判定与 summary（CI 可直接消费）。
- 能讲出双内核不一致的具体事故场景（dev 依赖 prod 摇除导致线上才炸）。
- 差异项带上下文（引用方）者加分。
