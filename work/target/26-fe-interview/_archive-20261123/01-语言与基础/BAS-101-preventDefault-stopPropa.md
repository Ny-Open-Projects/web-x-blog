---
title: [BAS-101] preventDefault、stopPropagation、stopImmediatePropagation 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-101：preventDefault、stopPropagation、stopImmediatePropagation 有什么区别？
**答**：
- preventDefault：阻止浏览器默认行为（提交表单、跳转链接），不影响事件继续传播。
- stopPropagation：阻止事件继续向其他节点传播，但同一元素上已注册的其他监听器仍会执行。
- stopImmediatePropagation：传播停止，且同一元素上排在它后面的监听器也不再执行。

```javascript
form.addEventListener('submit', (e) => e.preventDefault());  // 阻止提交，冒泡继续
inner.addEventListener('click', (e) => e.stopPropagation()); // 父级的 click 不触发
btn.addEventListener('click', () => console.log('A'));
btn.addEventListener('click', (e) => {
  e.stopImmediatePropagation();
  console.log('B');
});
btn.addEventListener('click', () => console.log('C'));       // 不会打印
```
