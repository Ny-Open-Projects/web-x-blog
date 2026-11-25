---
title: [JS-161] 事件委托的边界？blur/focus/scroll 这些不冒泡的事件怎么办？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-161：事件委托的边界？blur/focus/scroll 这些不冒泡的事件怎么办？

**答**：
- 不冒泡事件清单：focus/blur、mouseenter/mouseleave、scroll（容器自身滚动）、load/unload、media 系列事件。
- 方案一：换冒泡等价事件——focusin/focusout 代替 focus/blur，mouseover/mouseout 代替 enter/leave。
- 方案二：捕获阶段委托——所有事件都有捕获阶段，在 document 上 `addEventListener(type, fn, true)` 能截住不冒泡事件。
- 方案三：scroll 直接监听滚动容器自身，或用 IntersectionObserver 替代滚动位置检测。
- mouseover/out 委托时必须用 relatedTarget + contains 过滤「在子元素间移动」的误触发。

```javascript
// 方案一：focusin/focusout 是会冒泡的 focus/blur
document.addEventListener('focusin', (e) => {
  console.log('聚焦到', e.target.name);        // 可以在 document 层委托
});
document.addEventListener('focusout', (e) => {
  if (String(e.target.value).trim() === '') e.target.classList.add('error'); // 失焦校验
});

// 方案二：捕获阶段委托——blur 不冒泡但有捕获阶段
document.addEventListener('blur', (e) => {
  console.log('捕获阶段截住 blur：', e.target.name);
}, true);

// 方案三：scroll 只发生在滚动容器自身，直接监听它
const list = document.getElementById('list');
list.addEventListener('scroll', () => {
  const nearBottom = list.scrollTop + list.clientHeight >= list.scrollHeight - 50;
  if (nearBottom) console.log('接近底部，加载更多');
});

// mouseenter/leave 不冒泡 → mouseover/out 委托 + relatedTarget 过滤
list.addEventListener('mouseover', (e) => {
  const item = e.target.closest('.item');
  // relatedTarget 是「从哪个元素来」：仍在同一 item 内部移动则忽略
  if (item && !item.contains(e.relatedTarget)) item.classList.add('hover');
});
list.addEventListener('mouseout', (e) => {
  const item = e.target.closest('.item');
  if (item && !item.contains(e.relatedTarget)) item.classList.remove('hover');
});
```

## 追问（补充）

**追问**：

1. focus 与 focusin 的触发顺序和冒泡性差别？ → focus 先触发但不冒泡，focusin 随后触发且冒泡；要委托用 focusin，要最早拦截用捕获阶段的 focus。
2. scroll 为什么无法委托到 document？ → scroll 事件只在滚动元素自身触发、不冒泡，监听 document 收不到子容器滚动，只能监听容器本身或用 IntersectionObserver 替代。
3. mouseover 委托不判 relatedTarget 会怎样？ → 指针在子元素之间移动也会重复触发 over/out，导致 hover 态闪烁、进出计数虚高，必须用 `contains(e.relatedTarget)` 过滤。
