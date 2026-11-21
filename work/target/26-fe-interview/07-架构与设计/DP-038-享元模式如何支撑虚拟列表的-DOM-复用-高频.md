---
title: [DP-038] 享元模式如何支撑虚拟列表的 DOM 复用？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-038：享元模式如何支撑虚拟列表的 DOM 复用？（高频）
**答**：
- 10 万条列表如果每条一个 DOM 节点，内存和渲染都会崩——虚拟列表只渲染可视区约 20 条，滚动时**复用**这批节点更新内容。
- 享元思想：DOM 节点是共享的内部资源（少量），列表项数据是外部状态（每次传入）——"对象少、状态外置"。
- 关键实现：监听滚动 → 由 scrollTop 计算起始索引 → 更新可视区节点的 transform/内容。
- 同源应用：Canvas 弹幕、粒子系统、React 的 key 复用 reconciliation。

```javascript
// 虚拟列表最小实现：固定 20 个 DOM 节点，滚动时换数据不换节点
function createVirtualList({ container, itemHeight, total, render }) {
  const VIEW_COUNT = 20;
  container.style.overflow = 'auto';
  container.style.height = `${VIEW_COUNT * itemHeight}px`;
  const spacer = document.createElement('div');        // 撑起总高度
  spacer.style.height = `${total * itemHeight}px`;
  container.appendChild(spacer);

  const pool = Array.from({ length: VIEW_COUNT }, () => { // 享元池：节点只建一次
    const el = document.createElement('div');
    el.style.position = 'absolute';
    el.style.height = `${itemHeight}px`;
    container.appendChild(el);
    return el;
  });

  function onScroll() {
    const start = Math.floor(container.scrollTop / itemHeight); // 起始索引
    pool.forEach((el, i) => {
      const index = start + i;
      if (index < total) {
        el.style.display = 'block';
        el.style.transform = `translateY(${index * itemHeight}px)`;
        render(el, index); // 外部状态（第 index 条数据）注入共享节点
      } else {
        el.style.display = 'none';
      }
    });
  }
  container.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}
createVirtualList({
  container: document.querySelector('#list'),
  itemHeight: 40,
  total: 100000,
  render: (el, i) => { el.textContent = `第 ${i} 行`; },
});
// DOM 恒定 21 个（含 spacer），10 万条数据内存几乎不增长 —— 享元的收益
```
