---
title: [ZSM-828] React Compiler 对状态层的影响：memo 自动化后还剩什么优化
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-828：React Compiler 对状态层的影响：memo 自动化后还剩什么优化

**答**：
- React Compiler 自动 memo 化组件与 hook（分析依赖自动跳过重渲染）——它改变的是「渲染层优化」的半壁江山：`React.memo/useMemo/useCallback` 大部分可删。**但状态层的三类优化不受影响**：1) 订阅粒度（selector 拆分/useShallow——通知是否到达组件是状态库的事，Compiler 管不到通知层）；2) 扇出（store 通知给多少 observer）；3) 数据形状（归一化/引用稳定性——引用不稳定时 Compiler 的缓存比对也失效）。
- Compiler 的前提是「组件渲染纯函数」——**状态层的渲染期纪律变得更重要**：渲染期读 store 必须纯（不写不随机）、getSnapshot 稳定——违规会直接破坏 Compiler 的缓存假设。ZSM-615 的并发纪律与 Compiler 要求同源。
- 剩下的性能工作重新分布：编译器吃掉 memo 层后，优化重心转向「通知粒度与数据形状」——即 ZSM-618 的形状设计从「锦上添花」变成「唯一的优化面」。
- 对笔试卡的影响：useShallow/memoSelector 类手写题仍有价值（理解闸门原理），但「组件 memo 优化」类答案要更新——面试答「我会先确认 Compiler 是否启用，没启用才手写 memo」体现版本意识。
- 追问钩子：Compiler 与状态库的兼容性风险——库内部的手写 memo/forwardRef 混用可能触发编译器的保守降级（不优化）；状态库升级时关注 Compiler 兼容矩阵。

```javascript
// React Compiler 前后的优化分工
// 编译前（React 18）
const Row = memo(function Row({ id }) {
  const row = useTable((s) => s.rows.get(id))       // 状态库订阅粒度：Compiler 管不到
  const label = useMemo(() => formatLabel(row), [row])   // ← Compiler 可自动
  return <td>{label}</td>
})
// 编译后（React 19 + Compiler）
function Row({ id }) {
  const row = useTable((s) => s.rows.get(id))       // 保留：订阅粒度是库层职责
  const label = formatLabel(row)                     // ← Compiler 自动缓存
  return <td>{label}</td>
}

// 三类优化归属
const RESPONSIBILITY_AFTER_COMPILER = {
  框架接管: ['组件memo', 'useMemo/useCallback 大部分', 'props浅比较'],
  状态库仍管: ['selector订阅粒度', '通知扇出(643)', '数据形状/引用稳定(618)'],
  纪律更严: ['渲染期纯度(615)', 'getSnapshot稳定', '渲染期禁写'],
}
// 面试答法：「先确认 Compiler 启用与否，再决定手写 memo——版本意识」
```
