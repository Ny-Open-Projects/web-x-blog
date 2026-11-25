---
title: [MP-367] 笔试：手写路径 diff（对象对比 → setData 路径 patch）
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## MP-367：笔试：手写路径 diff

**答**：实现 `diffToPatch(prev, next, maxDepth = 3)`：① 对比两个 state 树，输出「路径 patch」（如 `{'list[2].status': 'done'}`）替代整包 setData；② 数组元素变化输出索引路径；③ 深度限制：超过 maxDepth 的子树直接整包替换（避免路径爆炸）；④ 新增/删除字段处理（删除输出 undefined 值）；⑤ 大小收益对比（patch JSON 大小 vs 全量）。写出实现。

```javascript
function diffToPatch(prev, next, maxDepth = 3, prefix = '') {
  const patch = {};
  const keys = new Set([...Object.keys(prev ?? {}), ...Object.keys(next ?? {})]);
  for (const k of keys) {
    const path = prefix ? `${prefix}.${k}` : k;
    const a = prev?.[k], b = next?.[k];
    if (Object.is(a, b)) continue;
    const bothObj = isPlainObj(a) && isPlainObj(b) && maxDepth > 0;
    if (bothObj) Object.assign(patch, diffToPatch(a, b, maxDepth - 1, path));
    else if (Array.isArray(a) && Array.isArray(b)) {
      // 数组: 逐索引对比(元素为对象时继续深入)
      const len = Math.max(a.length, b.length);
      for (let i = 0; i < len; i++) {
        const ai = a[i], bi = b[i];
        if (Object.is(ai, bi)) continue;
        const ip = `${path}[${i}]`;
        if (isPlainObj(ai) && isPlainObj(bi) && maxDepth > 0)
          Object.assign(patch, diffToPatch(ai, bi, maxDepth - 1, ip));
        else patch[ip] = bi === undefined ? null : bi;   // 删除用 null(小程序语义)
      }
    } else patch[path] = b === undefined ? null : b;
  }
  return patch;
}
function isPlainObj(v) { return v && typeof v === 'object' && !Array.isArray(v); }
// 用法
const patch = diffToPatch(this.data.list, newList);
console.log('patch 大小:', JSON.stringify(patch).length, '全量:', JSON.stringify(newList).length);
this.setData(patch);
```

**评分点**：
- 递归路径生成（对象点路径 + 数组索引路径语法）
- 深度限制防路径爆炸（深层整包替换）
- 删除字段的语义处理（undefined → null）
- 大小收益对比的意识（patch 有时反而更大——元素全换场景）
