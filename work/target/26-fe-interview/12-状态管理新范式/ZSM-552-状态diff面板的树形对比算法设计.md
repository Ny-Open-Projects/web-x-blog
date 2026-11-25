---
title: [ZSM-552] 状态 diff 面板的树形对比算法怎么设计才不卡
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-552：状态 diff 面板的树形对比算法怎么设计才不卡

**答**：
- 朴素递归 diff 大状态树的问题：万级节点的 store 每次变更全量递归比较，JSON.stringify 比较更是双倍开销。原则：**引用相等的子树直接剪枝**（不可变更新保证引用变才内容变），只在「引用不同」的层递归——这让 diff 成本正比于实际变更路径，而非状态总量。
- 输出结构：扁平的 `{ path, kind: 'added'|'removed'|'changed', prev, next }` 列表，UI 按路径分组渲染树。数组用 index diff（可配 LCS 优化，通常不需要）。
- 防卡手段：diff 放在空闲时间（requestIdleCallback）或 Web Worker；单次变更超过 N 条 diff（如 500）时降级为「大变更」只显示顶层摘要；对比缓存（Map<nextRef, prevRef>）避免重复比较。
- 渲染层：diff 结果虚拟滚动展示，值展示用 JSON 截断（超长字符串/大数组折叠），点击展开再懒序列化。
- 追问钩子：Map/Set/循环引用是 diff 实现的边界——用 WeakSet 记录访问路径检测循环，Map 按键浅比较。

```javascript
function diffState(prev, next, path = '', out = [], budget = { n: 500 }) {
  if (budget.n-- <= 0) { out.push({ path: path || '(root)', kind: 'truncated' }); return out }
  if (Object.is(prev, next)) return out                    // 引用相等：剪枝
  const bothObj = isPlainObj(prev) && isPlainObj(next)
  if (!bothObj) {
    out.push({ path, kind: 'changed', prev, next })
    return out
  }
  const keys = new Set([...Object.keys(prev), ...Object.keys(next)])
  for (const k of keys) {
    const p = path ? `${path}.${k}` : k
    if (!(k in prev)) out.push({ path: p, kind: 'added', next: next[k] })
    else if (!(k in next)) out.push({ path: p, kind: 'removed', prev: prev[k] })
    else if (isObj(prev[k]) && isObj(next[k])) diffState(prev[k], next[k], p, out, budget) // 递归
    else if (!Object.is(prev[k], next[k])) out.push({ path: p, kind: 'changed', prev: prev[k], next: next[k] })
  }
  return out
}

function isObj(v) { return v && typeof v === 'object' }
function isPlainObj(v) { return isObj(v) && !Array.isArray(v) }

// 用例
const a = { user: { name: 'a' }, items: [1], meta: { big: 'unchanged ref' } }
const b = { ...a, user: { name: 'b' }, items: [1, 2] }
console.log(diffState(a, b))
// [{ path: 'user.name', kind: 'changed' }, { path: 'items', kind: 'changed' }]
// meta 引用未变被剪枝，不进入比较
```
