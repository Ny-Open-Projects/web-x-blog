---
title: [WEB-394] 输入事件从鼠标点击到 JS 回调，路径是怎样的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-394：输入事件从鼠标点击到 JS 回调，路径是怎样的？
**答**：
- OS 事件 → 浏览器进程（浏览器侧路由，区分点击到哪个渲染进程）→ 渲染进程合成器线程 hit-test 定位元素 → 主线程事件循环派发（capture/target/bubble）。
- 关键优化：合成器对非关键输入（滚动）不等待主线程；对点击要等主线程命中测试——所以主线程阻塞时点击也延迟。
- 前端含义：长任务会"吃掉"点击响应；拆分任务（scheduler.yield/isInputPending）保住交互性。

```javascript
// 主线程 200ms 长任务期间点击会排队
console.log('长任务 → hit-test 延迟 → 点击延迟 → INP 变差');
// navigator.userActivation 检查激活态
if (navigator.userActivation?.isActive) openModal();
console.log('拆长任务用 scheduler.yield() 或分片 setTimeout');
```
