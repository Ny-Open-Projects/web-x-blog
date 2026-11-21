---
title: [DP-047] DOM 事件监听为什么是发布订阅（观察者）？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-047：DOM 事件监听为什么是发布订阅（观察者）？
**答**：
- `addEventListener` = 向事件中心（DOM 节点/EventTarget）注册回调；事件触发 = 中心按注册顺序/捕获冒泡规则分发。
- 特点：多播（同一事件多个监听）、可移除（removeEventListener 需要同引用）、有优先级规则（捕获→目标→冒泡）。
- 事件委托：把子元素的监听统一挂到父节点——一次注册管理大量子节点（性能 + 动态子元素）。
- 加分：CustomEvent 让任意业务对象获得 EventTarget 能力——标准化的发布订阅。

```javascript
// 1. addEventListener 就是订阅，事件对象就是通知载荷
const btn = document.querySelector('#btn');
const onClick = (e) => console.log('clicked', e.target.dataset.id);
btn.addEventListener('click', onClick);
btn.removeEventListener('click', onClick); // 退订必须同引用

// 2. 事件委托：父节点统一订阅（发布订阅的多播 + 转发）
document.querySelector('#list').addEventListener('click', (e) => {
  const li = e.target.closest('li[data-id]'); // 冒泡到父节点再分派
  if (li) console.log('删除', li.dataset.id);
});

// 3. CustomEvent：任意对象获得发布订阅能力（标准化事件中心）
const cart = new EventTarget();
cart.addEventListener('item:add', (e) => console.log('购物车角标 +1', e.detail));
cart.dispatchEvent(new CustomEvent('item:add', { detail: { sku: 'A1' } }));
// 购物车角标 +1 {sku: 'A1'}

// 4. 对照手写版理解：EventTarget 的内部就是 Map<type, Set<listener>>
// dispatchEvent 时按 capture/bubble 阶段依次调用 —— 浏览器原生实现的发布订阅
```
