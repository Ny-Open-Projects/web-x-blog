---
title: [WEB-039] postMessage 如何实现跨窗口通信？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-039：postMessage 如何实现跨窗口通信？
**答**：
- `window.postMessage(msg, targetOrigin)` 可在 iframe、window.open 的窗口、Web Worker 之间安全传数据，不受同源限制。
- 接收方监听 `message` 事件，事件对象带 `data` 与 `origin`；必须校验 `origin` 再使用数据，否则任意页面都能注入。
- targetOrigin 写 `*` 表示不限制，生产环境要写明确源。
- 典型场景：第三方登录弹窗回传、嵌入的广告 iframe 与主站通信、编辑器与预览窗口同步。

```javascript
// 父页面：嵌入第三方 iframe 并接收其消息
const frame = document.createElement('iframe');
frame.src = 'https://editor.example.com/preview';
document.body.appendChild(frame);

window.addEventListener('message', (event) => {
  // 安全校验：只信任声明的源，防止任意页面伪造消息
  if (event.origin !== 'https://editor.example.com') return;
  if (event.data.type === 'height') frame.style.height = `${event.data.height}px`;
  if (event.data.type === 'content') console.log(event.data.html);
});

// 父页面向 iframe 发送指令（等 iframe 加载后）
frame.onload = () => {
  frame.contentWindow.postMessage(
    { type: 'set-theme', theme: 'dark' },
    'https://editor.example.com' // 目标源，不写 *
  );
};
```

```javascript
// iframe 内页面：响应主题并上报高度
window.addEventListener('message', (event) => {
  if (event.origin !== 'https://www.example.com') return;
  if (event.data.type === 'set-theme') document.body.dataset.theme = event.data.theme;
});

window.parent.postMessage(
  { type: 'height', height: document.documentElement.scrollHeight },
  'https://www.example.com'
);
```
