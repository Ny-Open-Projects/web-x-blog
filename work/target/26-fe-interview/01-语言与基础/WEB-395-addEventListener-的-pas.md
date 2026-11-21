---
title: [WEB-395] addEventListener 的 passive 选项到底省了什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-395：addEventListener 的 passive 选项到底省了什么？
**答**：
- touchstart/wheel 等事件默认可 preventDefault，浏览器必须等监听器跑完才知道要不要取消默认滚动 → 滚动等待主线程。
- passive: true 承诺不调用 preventDefault → 浏览器立即滚动，不等主线程，跟手性大幅提升。
- Chrome 对 document 级 wheel/touch 默认 passive；但在具体元素上仍要显式声明。

```javascript
el.addEventListener('touchstart', onMove, { passive: true });  // 不阻塞滚动
// 需要 preventDefault 的手势才用默认（非 passive）
el.addEventListener('touchmove', gesture, { passive: false });
console.log('passive = 放弃 preventDefault 换滚动优先');
```
