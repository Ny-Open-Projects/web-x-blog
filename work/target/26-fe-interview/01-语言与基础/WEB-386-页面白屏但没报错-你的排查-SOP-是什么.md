---
title: [WEB-386] 页面白屏但没报错，你的排查 SOP 是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 笔试题
---

## WEB-386：页面白屏但没报错，你的排查 SOP 是什么？
**答**：
- 先分级：JS 报错白屏（看 Console/监控 error）、资源加载失败（Network 看 HTML/JS 404 或被拦）、渲染卡住（Performance 看主线程阻塞）、进程崩溃（renderer crashed）。
- 快速定位：Performance 面板录一次加载看关键节点（DCL/FCP 有没有发生）；Elements 面板看 root 是否空（挂载点被吞/框架未挂载）。
- 线上手段：监控 FCP>阈值 + 白屏检测（对 root 采样截图/元素计数）、sourcemap 还原错误栈、灰度回滚开关。

```javascript
// 白屏检测：DOM 采样
setInterval(() => {
  const root = document.querySelector('#app');
  if (root && root.children.length === 0 && Date.now() - t0 > 3000) {
    report({ type: 'blank', url: location.href, build: BUILD_ID });
  }
}, 1000);
console.log('排查链：Console → Network → Performance → 进程/灰度');
```

**评分点**：
- 结论先行，排查/实现路径清晰
- 覆盖典型异常与边界
- 代码可运行、体现方法论
- 主动给出工程取舍
