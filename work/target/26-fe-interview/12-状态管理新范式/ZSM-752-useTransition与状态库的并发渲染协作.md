---
title: [ZSM-752] useTransition 与状态库：大列表切换不卡输入的并发协作
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-752：useTransition 与状态库：大列表切换不卡输入的并发协作

**答**：
- 场景：万条列表的筛选切换——同步渲染会卡住输入框（重渲 500ms）。并发协作方案：把「重渲染成本高的状态变更」包进 `startTransition`，React 以低优先级调度它，输入（高优先级）可打断——列表过渡期显示旧列表 + isPending 提示。
- 与状态库的协作细节：1) transition 包住的是「触发变更的 action 调用」（`startTransition(() => store.setState(...))`），selector 订阅机制不变；2) transition 期间旧新两棵树并存——外部 store 的 getSnapshot 必须稳定（ZSM-615 防撕裂），Zustand v5 的 commit 校验就是为此；3) **过渡值要独立**：`useDeferredValue(kw)` 派生一个延迟值用于列表查询，输入框绑定原值——同一状态两个消费节奏。
- 派发模式对照：`useTransition` 适合「显式动作」（切 tab、应用筛选）；`useDeferredValue` 适合「连续输入的派生」（搜索结果）。两者都不适合高频动画（transient 更优，ZSM-518）。
- 效果度量：优化前后跑「输入响应延迟」——transition 后输入 keydown 到输入框回显 <16ms（不被列表渲染阻塞），列表切换耗时不变但可打断。这就是 INP 优化的典型手段。
- 追问钩子：transition 里的错误边界——低优先级渲染抛错会重试到高优先级，配合 Suspense 需要注意「过渡中 Suspense 挂起会回退到旧内容」（React 18 行为）而非显示 fallback。

```javascript
import { useTransition, useDeferredValue } from 'react'

function FilterableList() {
  const kw = useStore((s) => s.filterKw)          // 输入值：高优先级
  const items = useStore((s) => s.items)          // 大列表
  const [isPending, startTransition] = useTransition()
  const deferredKw = useDeferredValue(kw)         // 延迟值：列表查询用

  const results = useMemo(
    () => items.filter((i) => i.name.includes(deferredKw)),
    [items, deferredKw],
  )

  return (
    <>
      <input
        value={kw}
        onChange={(e) => {
          // 输入写入 store：同步（高优先级，输入框立即回显）
          useStore.getState().setFilterKw(e.target.value)
        }}
      />
      <button onClick={() => {
        // 重渲染成本高的切换：低优先级（可打断）
        startTransition(() => useStore.getState().applyFilters())
      }}>
        应用筛选 {isPending && '(计算中…)'}
      </button>
      <VirtualList items={results} />
    </>
  )
}

// 度量脚本：输入不被阻塞
// Performance 面板：keydown → input 回显（高优）独立于列表 commit（低优，可中断）
```
