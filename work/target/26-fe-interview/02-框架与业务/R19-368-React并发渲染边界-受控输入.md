---
title: [R19-368] 并发渲染边界：受控输入与同步优先级
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-368：并发渲染边界：受控输入与同步优先级

**答**：
- 受控输入的隐性同步：input onChange 里 setState 会以「连续事件优先级」（discrete input lane）处理——React 保证输入框实时更新，即使旁边有低优渲染在进行
- 边界一：输入值经过「派生计算」再 setState（如 format(v)）——派生在低优上下文会延迟；保持「原始值直接存、展示层派生」
- 边界二：受控值存外部 store（zustand）——订阅走 useSyncExternalStore，store 更新若在同帧多次会合并；输入延迟症状排查点
- 边界三：Transition 包裹输入 setState（误用）——输入被延迟到低优渲染完成才显示，严重卡顿；Transition 只包结果不包输入
- useOptimistic 的输入场景：即时反馈 + 服务器确认——React 19 对「乐观输入」的官方模式（如点赞立即高亮）

```jsx
// 反模式: transition 包输入
const [isPending, start] = useTransition();
onChange={(e) => start(() => setQuery(e.target.value))}  // 输入延迟!

// 正解: 输入同步 + 结果 deferred
onChange={(e) => setQuery(e.target.value)}               // 同步
const deferred = useDeferredValue(query);                 // 结果侧延迟
```
