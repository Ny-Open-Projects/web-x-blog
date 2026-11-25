---
title: [WEB-253] 渲染进程沙箱与站点隔离（Site Isolation）
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-253：渲染进程沙箱与站点隔离（Site Isolation）

**答**：
- 沙箱：渲染进程被操作系统限制——不能直接读写文件、发起系统调用受限，一切通过 IPC 向浏览器主进程申请，即使被漏洞攻破也困在沙箱里。
- 站点隔离：Chrome 67 起不同站点（site = scheme + eTLD+1）的页面不共享渲染进程，甚至 iframe 也分进程——解决 Spectre 类侧信道攻击跨站读内存的风险。
- 影响：iframe 数量增加会提高内存与进程数；`document.domain` 跨子域写法被弃用正是因为站点隔离下子域可能不同进程，直接 DOM 访问不可靠。
- 前端感知点：postMessage 替代跨 frame 直接访问；跨站 iframe 的同步 `window.length`/some 同步接口行为变化。

```javascript
// 跨 iframe 正确通信（站点隔离下不能直接碰 contentWindow.document）
window.parent.postMessage({ type: 'ready' }, 'https://parent.example.com');
// 父页面
window.addEventListener('message', (e) => {
  if (e.origin !== 'https://child.example.com') return; // 校验来源
  console.log(e.data);
});
```
