---
title: [MFW-843] PPR 静态壳该什么时候重建，怎么避免数据一变就全站重建壳
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-843：PPR 静态壳该什么时候重建，怎么避免数据一变就全站重建壳

**答**：
- 结论：壳只依赖「结构 + 稳定数据」，高频变化数据放进洞；只有 stable 依赖变更才触发壳重建，dynamic 依赖进洞实时读。
- 落地：构建期给壳的数据依赖打标 stable/dynamic；依赖图追踪哪些壳受 stable 依赖影响，精准重建。
- 追问钩子：怎么判断依赖是 stable？——按变更频率与业务容忍度：导航/品牌 stable，价格/库存 dynamic。

```javascript
const shells = [
  { name: '/product', deps: [{ key: 'brand', kind: 'stable' }, { key: 'stock', kind: 'dynamic' }] }
];
function shouldRebuild(shell, changedKey) {
  return shell.deps.some(d => d.key === changedKey && d.kind === 'stable');
}
// 库存变化 → 不重建壳（走洞实时读）
console.log(shouldRebuild(shells[0], 'stock'));    // false
// 品牌信息变化 → 重建壳
console.log(shouldRebuild(shells[0], 'brand'));    // true
```
