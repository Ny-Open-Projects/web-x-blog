---
title: [ZSM-615] React 并发特性（transition/Suspense）对状态库的额外要求
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-615：React 并发特性（transition/Suspense）对状态库的额外要求

**答**：
- 并发渲染的本质要求：**渲染必须是可中断、可重入、可丢弃的**。状态库因此有三条硬要求：1) getSnapshot 必须纯且稳定（同状态同引用，无副作用）；2) 渲染期间禁止 setState（并发模式下渲染可能被丢弃，写入会永久化脏状态）；3) 订阅通知要与 React 调度协作（批处理，不是来一次 flush 一次）。
- transition（useTransition/startTransition）：把低优先级状态变更标记为可打断——外部 store 场景的坑：transition 期间 store 已更新，但渲染还没提交，此时用户输入又触发高优先级更新，React 会「双渲染」（旧状态树 + 新状态树并存）。这就是 Zustand 需要 commit 后校验防撕裂的原因（ZSM-501）。
- Suspense：异步 atom 抛 promise 挂起渲染，此时「组件树数据还没 ready 但 store 已经变了」——恢复后重放 selector 时输入可能已变，selector 必须无记忆化泄漏（不能缓存到「预期输入」之外的东西）。
- useDeferredValue：外部 store 的值不能直接塞进去——deferred 的值要经过 React 状态/内部订阅流转，直接读 store 会绕过并发调度。
- 追问钩子：官方 `useSyncExternalStore` 就是并发时代状态库的接线标准——v4 之前的 Zustand 用自定义 hook 在 StrictMode/并发下都会出撕裂 bug。

```javascript
// 并发要求的正反例
// 反例 1：渲染期间 setState（渲染可能被丢弃）
function Bad({ id }) {
  const data = useStore((s) => s.data)
  if (!data) useStore.setState({ requested: id })   // BAD：渲染中写状态
  return <div>{data}</div>
}
// 正例：副作用放事件或 effect
function Good({ id }) {
  useEffect(() => { useStore.setState({ requested: id }) }, [id])   // OK
}

// 反例 2：transition 直接用外部 store 值
const value = useStore((s) => s.bigTree)     // transition 里旧新树并存 → 撕裂风险
const [isPending, start] = useTransition()
start(() => useStore.setState({ bigTree: next }))   // OK：set 在事件里，渲染走 useSyncExternalStore 校验

// useDeferredValue 与外部 store 的正确组合
function Search() {
  const kw = useStore((s) => s.kw)
  const deferredKw = useDeferredValue(kw)     // React 内部延迟，不直接绕过调度
  const results = useMemo(() => search(deferredKw), [deferredKw])
  return <List results={results} />
}
```
