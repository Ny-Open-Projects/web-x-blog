---
title: [ALG-209] 权限系统：判断两个权限集合的包含关系并找出差集（O(n) Set 运算）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

**场景**：权限改版，旧权限集合 A（数组）→ 新权限集合 B。要输出：新增（B-A）、移除（A-B）、保留（A∩B），并判断 B 是否完全覆盖 A（升版校验）。数组遍历两两比较 O(n·m) 会慢，用 Set。

**思路**：Set 构建 O(n)，差集/交集 O(min(n,m))。

```javascript
function diffPermissions(oldList, newList) {
  const oldSet = new Set(oldList), newSet = new Set(newList);
  const added = [], removed = [], kept = [];
  for (const p of newSet) oldSet.has(p) ? kept.push(p) : added.push(p);   // B 遍历一次
  for (const p of oldSet) if (!newSet.has(p)) removed.push(p);
  return { added, removed, kept, fullyCovered: removed.length === 0 };
}
diffPermissions(['read', 'write', 'admin'], ['read', 'export']);
// => { added: ['export'], removed: ['write','admin'], kept: ['read'], fullyCovered: false }
// 复杂度：O(n+m) 时间、O(n+m) 空间
// 注意：Set.has 是 O(1) 均摊；数组 includes 是 O(n)——这就是"别用 includes 写双层循环"的原因
```

**评分点**：
- Set 代替嵌套 includes（复杂度从 O(n·m) 降到 O(n+m)），这是本题核心考点。
- 一次遍历同时产出三组结果（added/removed/kept）。
- fullyCovered 判定（removed 为空）。
- 能说出 Set.has 均摊 O(1) 的原理（哈希）。
