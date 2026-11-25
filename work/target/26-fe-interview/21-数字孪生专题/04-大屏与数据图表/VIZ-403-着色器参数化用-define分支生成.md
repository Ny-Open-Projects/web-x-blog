---
title: [VIZ-403] 着色器参数化：用 define/分支生成变体
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-403：着色器参数化：用 define/分支生成变体

**答**：
- 变体：同一 shader 不同特性（光照数/贴图开关）用 #define 生成多版本，编译期裁剪分支。
- 管理：变体 key（feature 位掩码）-> 缓存 program；数量爆炸控制（组合上限 + 使用统计淘汰）。
- 替代：UBO + 统一分支（动态分支便宜化后）减少变体数，按数据分歧度权衡。

```javascript
// 变体生成
function buildVariants(base, features, usedStats) {
  const keys = Object.keys(features);
  const out = {};
  for (const mask of allCombinations(keys)) {    // 按 usedStats 裁剪
    if ((usedStats[mask] ?? 0) === 0 && Object.keys(usedStats).length > 16)
      continue;                                  // 淘汰未用变体
    const defines = keys.filter(k => mask.includes(k))
      .map(k => `#define ${k.toUpperCase()} 1`).join('\n');
    out[mask.join('+')] = defines + '\n' + base;
  }
  return out;
}
```
