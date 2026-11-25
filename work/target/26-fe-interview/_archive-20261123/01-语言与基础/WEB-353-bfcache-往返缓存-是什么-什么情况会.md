---
title: [WEB-353] bfcache（往返缓存）是什么？什么情况会让它失效？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-353：bfcache（往返缓存）是什么？什么情况会让它失效？
**答**：
- bfcache 保存页面的完整内存快照（JS 状态+DOM），前进/后退瞬间恢复，连 JS 都不重新执行，比强缓存快一个量级。
- 失效因素：unload/beforeunload 监听、Cache-Control: no-store、HTTPS 证书问题、打开 WebSocket（旧规范）、内存压力。
- 工程要点：用 pageshow 的 persisted 判断 bfcache 恢复，重连 WS/刷新时间；别用 unload，改用 pagehide。

```javascript
window.addEventListener('pageshow', (e) => {
  if (e.persisted) reconnectWS();     // bfcache 恢复后 WS 已死
});
window.addEventListener('pagehide', save);   // 不要用 unload
console.log('no-store 会禁用 bfcache —— 敏感页才值得');
```
