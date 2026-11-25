---
title: [ZSM-667] Valtio 的 useSnapshot 访问跟踪：怎么精确知道组件读了哪些属性
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-667：Valtio 的 useSnapshot 访问跟踪：怎么精确知道组件读了哪些属性

**答**：
- useSnapshot 的核心机制：快照对象也是 Proxy，**在渲染期间组件读哪些属性都被记录**（access tracking：get 拦截器把 `(snapshotRef, property)` 写进当前组件的「使用中集合」）；渲染结束后通知阶段只比对「组件实际用过的属性」的版本——没用到的属性变了不重渲。这是「自动订阅粒度」：不需要写 selector，读什么订阅什么。
- 与 Zustand selector 的对比：Zustand 显式声明依赖（selector），Valtio 隐式跟踪（useSnapshot 内部收集）——隐式的优点是零样板、深路径自动细分；缺点是跟踪发生在渲染期，「渲染里条件性读取」导致依赖每次可能不同（这是合法的，下一轮重新收集）。
- 跟踪边界：1) `Object.keys`/解构整个对象=订阅全部；2) 数组 length + 下标读取分别跟踪；3) **渲染外读取不跟踪**（useEffect 里 `snap.x` 不建立订阅——要用 `subscribe` 或把读取放渲染路径）；4) 解构时机：`const { a } = useSnapshot(state)` 在渲染期 OK。
- 性能陷阱：把整个快照传给子组件（props 下传大快照）会把父组件的跟踪范围传染给子组件的比较——子组件应自己 useSnapshot 只取所需。
- 追问钩子：`subscribe(proxy, cb, notifyInSync?)` 的第三个参数——true 时同步逐次触发回调，默认在微任务里批量异步触发（同 tick 多次变更合并为一次）；回调收到的是 ops 变更操作数组，不是快照 diff。

```javascript
import { proxy, useSnapshot } from 'valtio'

const state = proxy({ user: { name: 'a', age: 1 }, config: { theme: 'dark' }, items: [1, 2] })

// 访问跟踪示例：只读 name → 只有 name 变更触发
function NameTag() {
  const snap = useSnapshot(state)
  return <span>{snap.user.name}</span>    // 跟踪 user.name；config/items/age 变更不触发
}

// 解构注意：解构在渲染期即读取 → 被跟踪的字段就是解构的字段
function Card() {
  const { user, config } = useSnapshot(state)   // 跟踪 user.* 与 config.*（对象级）
  return <div>{user.name} / {config.theme}</div>
}

// 反模式：下传大快照
function Bad() {
  const snap = useSnapshot(state)
  return <DeepComp data={snap} />    // ✗ 传染跟踪范围
}
function Good() {
  return <DeepComp />    // ✓ 子组件自己 useSnapshot(state) 只取所需
}

// 渲染外读取不跟踪的坑
function Timer() {
  const snap = useSnapshot(state)
  useEffect(() => {
    const id = setInterval(() => {
      console.log(snap.config.theme)   // ✗ 读的是旧快照，且不建立订阅
    }, 1000)
    return () => clearInterval(id)
  }, [])
  // ✓ 用 subscribe（组件外语义）或渲染期读取
}
```
