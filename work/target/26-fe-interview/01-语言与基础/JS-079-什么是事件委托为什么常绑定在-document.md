---
title: [JS-079] 什么是事件委托？为什么常绑定在 document 或容器上？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-079：什么是事件委托？为什么常绑定在 document 或容器上？

**答**：
- 利用事件冒泡，把子元素的监听统一挂到父容器，由 e.target 判断真正来源。
- 优点：减少监听器数量、动态新增子元素无需重新绑定。
- 注意 currentTarget（绑定的元素）与 target（实际触发的元素）的区别。
- 限制：focus/blur 等不冒泡的事件需用捕获或 focusin 替代；中间 stopPropagation 会阻断委托。

```html
<ul id="list">
  <li data-id="1">a</li>
  <li data-id="2">b</li>
  <!-- 动态新增的 li 也能被处理 -->
</ul>
```

```javascript
document.querySelector('#list').addEventListener('click', (e) => {
  const li = e.target.closest('li'); // closest 容错内部嵌套元素
  if (!li || !e.currentTarget.contains(li)) return;
  console.log('clicked id:', li.dataset.id);
  console.log(e.currentTarget.id, e.target.textContent); // list 与具体 li
});

// 动态新增自动生效
const li = document.createElement('li');
li.dataset.id = '3';
li.textContent = 'c';
document.querySelector('#list').appendChild(li);
```
