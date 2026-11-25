---
title: [R19-377] React 大列表渲染策略：窗口化与并发特性配合
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## R19-377：React 大列表渲染策略：窗口化与并发特性配合

**答**：
- 虚拟列表基础：react-window/react-virtuoso——只渲染可见区 + 缓冲；动态高度用测量缓存（ResizeObserver 上报）
- 与 Transition 配合：虚拟列表的「数据过滤」用 transition——列表重排可打断；但虚拟列表本身滚动是同步 DOM 操作（不在 React 渲染里）
- React 19 的 useOptimistic 在列表中的应用：点赞/删除即时反馈——乐观项插入列表（pending 标记），server 返回后校正
- 内存面：虚拟列表的 DOM 复用（key 回收）与 React key 稳定性——滚动时 key 抖动会造成状态丢失（输入框焦点丢失）
- 服务端协同：分页游标 + 预取（滚动方向预判）——「虚拟列表 + 无限加载」的组合模式

```jsx
const rowVirtualizer = useVirtualizer({
  count: items.length,
  getScrollElement: () => scrollRef.current,
  estimateSize: () => 48,
  overscan: 5,
});
// 行组件: 稳定 key + memo + 轻渲染
{rowVirtualizer.getVirtualItems().map(vi => (
  <Row key={items[vi.index].id} style={vi.style} item={items[vi.index]} />
))}
```
