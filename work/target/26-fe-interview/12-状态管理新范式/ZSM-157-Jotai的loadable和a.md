---
title: [ZSM-157] Jotai 怎么精细处理异步 atom 的加载态？loadable 和 abortable atom 分别解决什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-157：Jotai 怎么精细处理异步 atom 的加载态？loadable 和 abortable atom 分别解决什么？
**答**：
- 异步 atom 默认行为是被 Suspense 消费（050/049 已考派生链和 Suspense 边界），但「不想用 Suspense、想在组件里拿到状态机」时要 loadable：`useAtomValue(loadable(atom))` 返回 `{ state: 'loading' | 'hasData' | 'hasError', data }`，组件自己决定每个分支的 UI。
- abortableAtom 解决「参数变了，旧请求作废」：传入一个 abortable signal，参数变化时旧 promise 被 abort，防止慢响应覆盖新值——等价于 Query 的 signal 机制。
- 组合套路：列表页用 loadable（骨架/错误/数据三态就近渲染），详情页用 Suspense（上提边界），切换型数据用 abortable（搜索联想）。
- 追问钩子：能对比「Jotai 三态手动 vs Suspense 隐式」的取舍——手动三态代码多但边界粒度细，Suspense 简洁但边界层级要设计。

```javascript
import { loadable, abortableAtom } from 'jotai/utils'
import { atom } from 'jotai'

const kwAtom = atom('')

// 参数驱动的可中止异步 atom
const suggestionsAtom = abortableAtom((get, { signal }) => {
  const kw = get(kwAtom)
  if (!kw) return []
  return fetch(`/api/suggest?kw=${kw}`, { signal })   // kw 变化自动 abort
    .then(r => r.json())
})

function SuggestBox() {
  const lw = useAtomValue(loadable(suggestionsAtom))
  if (lw.state === 'loading') return <Spinner/>       // 三态手动渲染
  if (lw.state === 'hasError') return <ErrorView retry={/* re-set kw */}/>
  return <List items={lw.data}/>
}
```

## 边界与易错（补充）

**边界与易错**：

- abortable 只中止 fetch 本身，已经进入的 `then` 链不会自动停。后处理里要自己判 `signal.aborted`，否则旧响应仍会写进 store。
- `loadable(atom)` 不要写在组件体内，每次渲染都会包出一个新 atom，缓存直接失效；要提到模块作用域或 `useMemo` 里。
- 三态渲染容易漏掉第四态「有旧数据但正在刷新」。直接闪骨架比保留旧数据体验更差，搜索联想场景应该保留上一批结果并加 loading 指示。
