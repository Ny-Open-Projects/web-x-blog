---
title: [JS-230] detached DOM 泄漏是什么：怎么排查
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 内存]
type: 面试题
---

## JS-230：detached DOM 泄漏是什么

**答**：
- 定义：DOM 节点已从文档移除，但 JS 里仍有变量/数组/事件回调持有它——「游离 DOM」整棵子树无法回收
- 高发场景：把节点存进数组做缓存/撤销栈、定时器回调引用节点、闭包捕获 table 行、全局变量暂存 modal
- 为什么隐蔽：单看页面没问题，反复进入退出某功能后内存阶梯上升
- 排查：Memory 面板拍快照 → 筛选 Detached（Heap snapshot 的 Detached 标记）→ 看 Retainers 引用链找到持有者
- 修复：存储处改 WeakRef/WeakMap、撤销栈存数据快照而非节点、清理时机与生命周期绑定

```javascript
const removed = []; // ❌ 撤销栈存节点
function remove(row) { removed.push(row); row.remove(); }
// ✅ 存数据快照
function remove(row) {
  removed.push({ html: row.outerHTML, data: row.dataset });
  row.remove();
}
```
