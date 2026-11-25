---
title: [XP-195] Electron 深度链接：自定义协议与路由分发
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-195：Electron 深度链接：自定义协议与路由分发

**答**：
- 题目：Electron 深度链接——自定义协议（app://）注册、参数解析路由分发、浏览器唤起（协议 handler）。
- 思路：app.setAsDefaultProtocolClient 注册协议；第二实例处理（单实例锁场景深链从 argv 来）；路由分发到对应窗口/页面。
- 评分点：协议注册；深链路由；单实例联动。

```javascript
// 主进程：注册协议
app.setAsDefaultProtocolClient('myapp');                           // myapp:// 协议
// macOS：open-url 事件
app.on('open-url', (e, url) => { e.preventDefault(); handleDeepLink(url); });
// Windows/Linux：第二实例 argv（单实例锁场景）
app.on('second-instance', (e, argv) => {
  const url = argv.find(a => a.startsWith('myapp://'));
  if (url) handleDeepLink(url);
});
function handleDeepLink(url) {                                     // 路由分发
  const parsed = new URL(url);
  const route = { path: parsed.host, params: Object.fromEntries(parsed.searchParams) };
  win.webContents.send('deep-link', route);                         // 分发到渲染进程路由
}
// 浏览器侧唤起：<a href="myapp://open?docId=123">在应用中打开</a>
```
