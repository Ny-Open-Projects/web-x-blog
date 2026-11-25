---
title: [R19-354] commit 三阶段深水：beforeMutation / mutation / layout
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Fiber]
type: 面试题
---

## R19-354：commit 三阶段深水：beforeMutation / mutation / layout

**答**：
- beforeMutation：读取快照（getSnapshotBeforeUpdate），Class 组件专属——DOM 变更前的滚动位置等保存
- mutation：同步执行 DOM 增删改（Placement/Deletion/Update），在此阶段卸载组件执行 cleanup（useEffect 的销毁函数不在这——那在下一轮 layout 后异步）
- layout：同步执行 componentDidMount/useLayoutEffect/this.forceUpdate——此刻 DOM 已更新但浏览器未绘制，可以同步读布局并改 DOM（避免闪烁）
- useEffect 调度：layout 阶段结束后「异步调度」flushPassiveEffects（Scheduler Normal 优先级）——这就是 useEffect 比布局阶段晚且不阻塞绘制的原因
- 深水点：commitRootImpl 的「双 pass」——同步 pass 完成后，立即检查是否有新的同步级更新需要连续 commit（continuous commits）

```text
commit 流程:
  beforeMutation: getSnapshotBeforeUpdate
  mutation:      insertBefore/appendChild/removeChild + commitUpdate(props diff)
  layout:        useLayoutEffect / componentDidMount (同步, 可读布局)
  (异步)          flushPassiveEffects → useEffect
绘制: layout 完成后浏览器才 paint
```
