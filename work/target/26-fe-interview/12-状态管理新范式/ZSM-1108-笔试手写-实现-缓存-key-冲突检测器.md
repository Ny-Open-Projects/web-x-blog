---
title: [1108] 笔试手写：实现 缓存 key 冲突检测器
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 缓存]
type: 笔试题
---

## 1108：笔试手写：实现 缓存 key 冲突检测器

**答**：实现 detectKeyRisks(keys)：keys 为缓存键数组。检测三类风险：① 歧义拼接——不同参数组合拼出同一 key（如 ['a','b'] 与 ['ab'] 产生的 'a|b' vs 'ab' 不同，但 ['a|b'] 与 ['a','b'] 同为 'a|b' 即冲突）；② 完全重复 key；③ 含未定义序列化痕迹（'undefined'、'null' 子串的 key）。返回 { duplicates, ambiguous, dirty }。

```js
function detectKeyRisks(keys) {
  const count = new Map();
  for (const k of keys) count.set(k, (count.get(k) || 0) + 1);
  const duplicates = [...count.entries()].filter(([, n]) => n > 1).map(([k]) => k);
  const seenComps = new Map(); // 归一化参数组合 -> 原始 key
  const ambiguous = [];
  for (const k of keys) {
    const norm = k.split('|').map(s => s.trim()).join('|'); // 分段归一
    if (seenComps.has(norm) && seenComps.get(norm) !== k) {
      ambiguous.push([seenComps.get(norm), k]); // 不同来源同归一化 → 拼接歧义
    } else seenComps.set(norm, k);
  }
  const dirty = keys.filter(k => /undefined|\bnull\b/.test(k));
  return { duplicates, ambiguous, dirty };
}
```

**评分点**：
- 重复、歧义、脏值三类风险分开检测
- 歧义判定的归一化拆分（'|' 分段语义）
- 'undefined' 入 key 是参数漏传的强信号
- 能讨论：根治歧义靠稳定序列化（stableStringify）+ 强类型 key 构造器
