---
title: [WEB-175] Memory 面板的快照对比怎么做？retained size 是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-175：Memory 面板的快照对比怎么做？retained size 是什么？
**答**：
- 三步法：操作前拍快照 → 执行可疑操作（开关弹窗 N 次）→ 再拍快照，Comparison 视图看新增对象。
- 两个关键列：Shallow Size（对象自身内存）、Retained Size（对象被 GC 后能释放的总内存，含其引用链）——排查泄漏按 retained size 排序。
- 典型泄漏特征：Detached DOM 数量增长、闭包引用的业务对象残留、全局 Map/数组只增不减。
- 在 Retainers 链里找"谁还攥着它"，通常指向事件监听器或全局缓存。

```javascript
// 可疑泄漏代码：每次渲染都往全局数组塞闭包，DOM 被引用无法回收
const cache = [];
function renderCard(data) {
  const el = document.createElement('div');
  el.textContent = data.title;
  cache.push({ el, onClick: () => open(data.id) }); // el 被全局持有，弹层关闭后成为 Detached DOM
  document.body.appendChild(el);
}
// 修复：弹层销毁时移除引用（el.remove() 并清出 cache），或改用 WeakRef/WeakMap 持有
// 验证：快照对比视图 filter 输入 Detached，关闭弹窗后数量应归零
```
