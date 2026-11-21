---
title: [JS-164] DOM 批量修改如何优化？DocumentFragment 与读写分离是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-164：DOM 批量修改如何优化？DocumentFragment 与读写分离是什么？

**答**：
- 每次插入/读取布局属性都可能触发重排，循环里「读一次写一次」会造成布局抖动（layout thrashing）。
- DocumentFragment 是内存中的临时容器，拼装过程不进文档不重排，最后 appendChild 一次挂载。
- 读写分离：先批量读所有布局属性（只读不写），再批量写样式（只写不读），把 n 次重排压成 1 次。
- 批量读取本身不重排（缓存了布局），批量写完后布局只计算一次。
- 极端场景可离屏修改（display:none 下改完再显示），或直接改 className 一次性切换。

```javascript
// 反面教材：循环逐条插入 + 循环里交替读写
// for (...) { list.appendChild(row); console.log(list.scrollHeight); }

// 优化一：DocumentFragment 内存拼装，一次挂载
const list = document.getElementById('list');
const frag = document.createDocumentFragment();   // 不在文档中，操作零重排
for (let i = 0; i < 1000; i++) {
  const row = document.createElement('div');
  row.textContent = `row ${i}`;
  frag.appendChild(row);
}
list.appendChild(frag);                            // 只触发一次重排

// 优化二：读写分离，消灭布局抖动
const rows = [...document.querySelectorAll('.row')];
const heights = rows.map((r) => r.offsetHeight);   // 先批量读（此时布局只计算一次）
rows.forEach((r, i) => {
  r.style.height = `${heights[i] + 2}px`;          // 再批量写（写期间不读布局）
});
// 反例：读写交替 rows.forEach(r => r.style.height = r.offsetHeight + 2 + 'px')
// 每次写都会使下一次读强制重排 → n 次重排

// 优化三：display none 离屏批量修改（大改动时）
// container.style.display = 'none'; 批量改; container.style.display = '';
```
