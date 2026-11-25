---
title: [ZSM-368] 怎么给状态做 diff 工具（看清一次变更改了什么）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-368：怎么给状态做 diff 工具（看清一次变更改了什么）

**答**:
- 实现：set 前存 prev，set 后递归 diff（按路径输出 added/changed/removed），打印为 path: old → new 三元组；大对象只 diff「变更路径」（引用不同的子树才深入）
- 深度控制：数组用 id 键 diff 而不是下标（下标 diff 全错位）；循环引用走 once 标记
- 展示形态：console 表格、devtools 面板时间线（与 Redux DevTools 集成），关键变更可跳转源码位置（stack 抓取）
- 用途：评审大变更、定位「谁改的」、回放调试时的 diff 流（比全量快照省 10 倍存储）

```javascript
function diffState(prev, next, path = '', out = []) {
  if (prev === next) return out
  if (typeof prev !== 'object' || typeof next !== 'object' || !prev || !next)
    return (out.push({ path, from: prev, to: next }), out)
  const keys = new Set([...Object.keys(prev), ...Object.keys(next)])
  for (const k of keys) diffState(prev[k], next[k], path ? `${path}.${k}` : k, out)
  return out
}
// 输出示例：user.name: "a" → "b"；items[3].qty: 1 → 2
```
