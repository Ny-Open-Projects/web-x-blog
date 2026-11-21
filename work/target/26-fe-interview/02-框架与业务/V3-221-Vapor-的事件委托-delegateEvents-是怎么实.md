---
title: [V3-221] Vapor 的事件委托（delegateEvents）是怎么实现的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-221：Vapor 的事件委托（delegateEvents）是怎么实现的？
**答**：
- 方案：启动时在 `document`（或 app 容器）上一次性挂委托 listener；编译期把模板上的事件编译为 `delegate(el, 'click', handler)`，把 handler 存到 DOM 节点的属性上。
- 委托命中：真实事件冒泡到容器时，通过 `event.target.closest` 找到注册节点，取出 handler 执行。
- 收益：单节点 0 listener，大量列表节点事件绑定 O(1)；内存与创建耗时都省。
- 例外：`focus/blur/input` 等不冒泡或频繁触发的事件不走委托，直接 `el.addEventListener`（编译器按事件类型分流）。
- 对比 React 17 前后：React 也是 document 委托（17 改到 root），Vue Vapor 复用了同类思路但保留了 Vue 的修饰符编译（`.stop/.prevent` 编译为包装函数）。

```javascript
// 简化实现
const delegatedEvents = new Set(['click', 'dblclick']);
export function delegateEvents(root = document) {
  for (const type of delegatedEvents) {
    root.addEventListener(type, (e) => {
      let node = e.target;
      while (node && node !== root) {
        const handler = node[`$$${type}`]; // 编译器写入节点属性
        if (handler) { handler(e); if (e.cancelBubble) return; }
        node = node.parentNode;
      }
    });
  }
}
export function delegate(el, type, fn) { el[`$$${type}`] = fn; } // 编译产物调用
// 模板 <button @click.stop="n++"> 编译为：
// delegate(n0, 'click', (e) => { e.stopPropagation(); n.value++ })
```
