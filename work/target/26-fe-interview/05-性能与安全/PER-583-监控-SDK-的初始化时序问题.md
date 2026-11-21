---
title: [PER-583] 监控 SDK 的初始化时序问题：脚本异步加载时首屏指标为什么会漏？怎么保证不漏采？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-583：监控 SDK 的初始化时序问题：脚本异步加载时首屏指标为什么会漏？怎么保证不漏采？

**答**：
- 漏采机制：监控 SDK 若 `async` 晚于首屏渲染执行，`buffered: true` 虽能补回 paint/LCP 历史 entry，但**布局偏移序列、错误堆栈、慢交互细节**没有浏览器缓冲，错过了就永久丢失。
- 不漏采三板斧：SDK 内联到 `<head>` 最先执行（同步）；`buffered: true` 全指标补采；错误监听在 SDK 加载前用极简预埋钩子"（window.onerror 收集到数组，SDK 到位后回放给正式采集器）。
- 采集时机与指标口径的关系：LCP 要在 visibility hidden 时 finalize，CLS 要剔除输入后的偏移——时序错了指标值本身就不对，不只是漏不漏的问题。
- 追问钩子：为什么不用 `document.currentScript` 判断加载时机？——module/defer 场景下 currentScript 为 null，要靠 script 标记属性显式声明模式。

```javascript

// head 内联：先于一切渲染执行
(function () {
  window.__preLog = { errors: [], vitals: [] };           // 极简预埋缓冲
  window.onerror = function (msg, src, line, col, err) {
    window.__preLog.errors.push({ msg, src, line, col, stack: err?.stack, ts: Date.now() });
  };
})();
// SDK 主脚本（可 async，加载后接管）
function initSdk() {
  window.onerror = realErrorHandler;                       // 接管错误采集
  window.__preLog.errors.forEach(realErrorHandler);        // 回放预埋期错误
  delete window.__preLog;
  new PerformanceObserver(l => collect(l.getEntries()))
    .observe({ type: 'layout-shift', buffered: true });    // buffered 补历史
  new PerformanceObserver(l => collect(l.getEntries()))
    .observe({ type: 'largest-contentful-paint', buffered: true });
}
// 关键：预埋钩子保证 SDK 加载前的错误不丢，buffered 保证渲染指标不丢
```
