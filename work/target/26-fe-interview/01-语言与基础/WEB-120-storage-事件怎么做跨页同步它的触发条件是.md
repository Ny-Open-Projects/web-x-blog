---
title: [WEB-120] storage 事件怎么做跨页同步？它的触发条件是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-120：storage 事件怎么做跨页同步？它的触发条件是什么？
**答**：
- `storage` 事件只在"其他同源标签页修改了 localStorage/sessionStorage"时触发，本页自己的写入不触发——这是它做同步的天然语义。
- 回调带 key/oldValue/newValue/url 与 storageArea；写相同值不触发（值必须变化）。
- 用途：主题/语言偏好同步、购物车跨标签更新；配合版本号字段可做简易"多标签配置热更"。
- 局限：只通知不保证顺序，复杂协调用 BroadcastChannel 或 SharedWorker。

```javascript
// 标签页 A：写偏好
document.querySelector('#theme').onchange = (e) => {
  localStorage.setItem('theme', e.target.value); // 触发其他页的 storage 事件
};

// 标签页 B/C：被动接收
window.addEventListener('storage', (e) => {
  if (e.key === 'theme' && e.newValue) {
    document.documentElement.dataset.theme = e.newValue;
    console.log(`由页面 ${e.url} 同步了主题`);
  }
  if (e.key === 'cart-version' && e.newValue) refreshCart(); // 触发数据刷新
});
```
