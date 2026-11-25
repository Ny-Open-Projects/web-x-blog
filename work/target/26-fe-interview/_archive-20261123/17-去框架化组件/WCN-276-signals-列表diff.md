---
title: [WCN-276] 列表数据的信号化（数组信号 + keyed 更新）如何避免全列表重渲染？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-276：列表数据的信号化（数组信号 + keyed 更新）如何避免全列表重渲染？
**答**：
- 数组信号整体替换会触发全列表 effect——keyed 节点级订阅才是细粒度。
- 模式：per-item 信号（itemSignals: Map<key, signal>），数组信号只存 key 顺序。
- 增删 = 改顺序数组 + 增删 item 信号；修改 = 改对应 item 信号——DOM 只动受影响项。
- 库支持：solid 的 For 组件/keyed each 已内置此模式。

```javascript
const keys = signal<string[]>([]);            // 顺序
const items = new Map<string, Signal<Item>>(); // 内容
function updateItem(id, patch) {
  items.get(id).value = { ...items.get(id).value, ...patch };  // 只动一项
}
// <For each={keys}> 内部按 key 复用 DOM 节点
r
```
