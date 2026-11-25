---
title: [ZSM-836] 浏览器原生状态 API 盘点：Navigation/View Transition/Command 状态
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-836：浏览器原生状态 API 盘点：Navigation/View Transition/CSS 状态能力

**答**：
- 浏览器正在接管更多「状态职责」，盘点原生能力与状态库的分工：
- **Navigation API**（Chrome）：路由状态原生化——`navigation.currentEntry.state`（每条历史条目携带序列化状态）、`navigate` 事件拦截。与 ZSM-536「URL 为事实源」互补：不进 URL 的导航态（滚动位置/表单草稿）可挂 history state，前进后退原生保留。
- **View Transitions**：跨视图动画的状态衔接——旧视图快照 → 状态变更 → 新视图动画。对状态层的意义：**动画不再要求「状态分步变更」**——一次 setState + View Transition 即可表达「位置迁移动画」（简化 FLIP，ZSM-762）。
- **CSS 原生状态**：`:has()`（父选择器）减少「状态提升到 store」的需求——纯展示联动（子项 hover 影响父样式）不需要 JS 状态；`scroll-driven animations`（滚动进度动画）接管滚动状态——滚动联动从 rAF 手写（ZSM-762）变为声明式 CSS。
- 分工原则更新：**「能进 CSS/平台的不过 JS」**——展示态联动优先 CSS，导航态优先 Navigation API，只有业务态才进状态库。这让 store 更小更聚焦（ZSM-618 形状分离的延伸）。
- 追问钩子：原生 API 的兼容策略——Progressive Enhancement：有 View Transition 用之、无则降级即时切换；`CSS.supports('animation-timeline: view()')` 探测进 ZSM-770 分级策略表。

```javascript
// 原生状态 API 与状态库的分工
// 1) Navigation API：不进 URL 的导航态
navigation.addEventListener('navigate', (e) => {
  if (e.hashChange) return
  // 拦截 SPA 导航：e.intercept({ handler })
})
navigation.currentEntry.state         // { scrollY: 500, draft: '...' } —— 历史条目状态
navigation.navigate('/detail', { state: { from: 'list', selectedId: '7' } })
// 后退时：navigation.currentEntry.state 原生恢复（ZSM-772 bfcache 语义的原生版）

// 2) View Transition：一次 setState 表达位置迁移
document.startViewTransition(() => {
  store.setState({ selectedId: nextId })   // 一次状态变更
  render()                                  // 旧快照 → 新视图 动画过渡
})
// 对比 FLIP（762）：无需手写记录旧位置/transform 补间

// 3) CSS 原生状态：滚动联动不再进 JS
// .progress-bar { animation-timeline: scroll(root); }   ← 滚动进度动画：零 JS 状态
// .card:has(.badge) { border-color: red; }              ← :has 联动：零 store 提升

// 分工原则：能进 CSS/平台的不过 JS
const NATIVE_FIRST = {
  展示联动: 'CSS :has() / scroll-driven —— 零 store',
  导航态: 'Navigation API entry.state —— 原生历史恢复',
  视图动画: 'View Transition —— 简化 FLIP',
  业务态: '仍进状态库（Zustand/Query）',
}
```
