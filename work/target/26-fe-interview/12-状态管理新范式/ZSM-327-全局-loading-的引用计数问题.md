---
title: [ZSM-327] 全局 loading 遮罩为什么会出现提前消失或永转
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-327：全局 loading 遮罩为什么会出现提前消失或永转

**答**:
- 布尔开关模式在并发请求下必然错乱：A 请求结束把 loading 关掉，B 还在跑——必须引用计数（计数 >0 显示）而不是布尔
- 实现：begin/end 配对（try-finally 保证必调 end）、计数衰减到 0 才隐藏；同类聚合（多个模块各自计数再汇总）
- 永转根因清单：begin 后异常路径没 end（缺 finally）、组件卸载未销自己的计数、计数重复递减（降为负后失效）
- 现代替代：TanStack Query 的 isFetching/isMutating 天然是聚合计数；自建 store 时用 Set 存活跃任务 id，size 即计数

```javascript
const tasks = useStore((s) => s.activeTasks)
function withGlobalLoading(fn) {
  const id = Symbol()
  useStore.setState((s) => ({ activeTasks: new Set([...s.activeTasks, id]) }))
  return fn().finally(() =>
    useStore.setState((s) => ({ activeTasks: new Set([...s.activeTasks].filter((t) => t !== id)) }))
  )                                   // finally 保证必减，Set size > 0 显示遮罩
}
```
