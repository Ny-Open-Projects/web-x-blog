---
title: [ZSM-159] Valtio 的 proxy 响应式原理是什么？snapshot 机制和 useSnapshot 的坑在哪？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-159：Valtio 的 proxy 响应式原理是什么？snapshot 机制和 useSnapshot 的坑在哪？
**答**：
- 原理：proxySet/state 用 ES Proxy 包装对象，写入时拦截 set/deleteProperty 记录变更并通知；读取路径走「不可变快照」——useSnapshot 返回深度只读的 snapshot，React 按快照做常规比较渲染。
- 订阅粒度：proxy 在 render 期间记录「组件实际访问了哪些属性」，只在这些属性变更时重渲染——访问即订阅（和 Jotai/Signal 思路同源，061 已考机制差异，这里考 Valtio 自身）。
- 头号坑：直接改 snapshot（它是冻结的只读副本）不生效；要改就改 proxy 对象 `state.count++`。第二坑：在 render 里解构大对象等于订阅全部字段，粒度优势全无，要按需逐字段读。
- 适用：命令式交互密集的场景（画布、拖拽、表单草稿），`state.x.y.z = 1` 直接改的写法比 Zustand 的展开重建舒服得多。

```javascript
import { proxy, useSnapshot } from 'valtio'

const state = proxy({                     // 可变 proxy：写入侧
  profile: { name: 'A', age: 18 },
  items: ['a', 'b'],
})

function Profile() {
  const snap = useSnapshot(state)         // 只读快照：读取侧
  return (
    // ❌ 反模式：{...snap.profile} 全量解构 = 订阅全部字段
    <>
      <div>{snap.profile.name}</div>      {/* 只订阅 name */}
      <button onClick={() => {            // 直接改 proxy，无需 setState
        state.profile.age++
        state.items.push('c')             // 数组变更也被代理
      }}>长一岁</button>
    </>
  )
}
// 注意：snap 是冻结对象，snap.profile.age++ 会抛错——写只能走 state
```
