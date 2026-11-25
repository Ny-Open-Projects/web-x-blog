---
title: [ZSM-633] 结构共享 replaceEqualDeep：怎么让两次响应的相同子树共用引用
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-633：结构共享 replaceEqualDeep：怎么让两次响应的相同子树共用引用

**答**：
- 问题：两次 fetch 返回的 JSON 即使内容基本相同，对象引用也全新——useQuery data 引用每次都变，所有下游 useMemo/useMemo 依赖全失效，订阅列表组件全量重渲。
- replaceEqualDeep 的做法：递归对比新旧值，**深度相等（deep equal）的子树返回旧引用**，有差异的层新建（内部子树继续递归）。结果：data 顶层引用只在「真正变化」时更新，列表里未变的行保持引用稳定。
- 收益链条：列表组件 props 中 data 稳定 → React.memo 生效 → 只重渲变化的行；再叠加 useShallow 的 selector，重渲半径缩到最小。
- 细节与边界：1) 只有值类型不同才建新对象（`Object.is` 先行短路）；2) 数组按位置对比（不等长时尾巴新建）；3) Map/Set/Date 支持有限，自定义类不建议开启；4) 关闭开关 `structuralSharing: false`——当你需要「每次新引用」触发副作用时才关。
- 追问钩子：结构共享是 O(n) 深比较，超大响应（万级节点）本身有成本——配合 select 切片（select 在结构共享之后执行）让比较范围只覆盖被选的切片。

```javascript
// replaceEqualDeep 骨架
function replaceEqualDeep(prev, next) {
  if (Object.is(prev, next)) return prev              // 引用或原始值相等
  if (typeof prev !== 'object' || typeof next !== 'object' || !prev || !next) return next
  if (Array.isArray(prev) && Array.isArray(next)) {
    if (prev.length !== next.length) return next
    let changed = false
    const out = prev.map((v, i) => {
      const r = replaceEqualDeep(v, next[i])
      if (r !== v) changed = true
      return r
    })
    return changed ? out : prev                        // 全等：整个数组复用旧引用
  }
  if (isPlainObject(prev) && isPlainObject(next)) {
    const keys = new Set([...Object.keys(prev), ...Object.keys(next)])
    if (keys.size !== Object.keys(prev).length || keys.size !== Object.keys(next).length) return next
    let changed = false
    const out = {}
    keys.forEach((k) => {
      const r = replaceEqualDeep(prev[k], next[k])
      if (r !== prev[k]) changed = true
      out[k] = r
    })
    return changed ? out : prev
  }
  return next
}

// 效果
const resp1 = { list: [{ id: 1, n: 'a' }, { id: 2, n: 'b' }] }
const resp2 = { list: [{ id: 1, n: 'a' }, { id: 2, n: 'c' }] }   // 第二行变了
const shared = replaceEqualDeep(resp1, resp2)
console.log(shared.list[0] === resp1.list[0])   // true：未变的行复用引用 → memo 行组件不重渲
console.log(shared.list[1] === resp1.list[1])   // false：变的行新建
```
