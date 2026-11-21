---
title: [FRP-111] 流式 SSR 与选择性 hydration 是什么？"后到先 hydrate"如何实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-111：流式 SSR 与选择性 hydration 是什么？"后到先 hydrate"如何实现？

**答**：
- 流式 SSR：`renderToPipeableStream`（React 18）/ Vue 的 `renderToNodeStream` 把页面**按 Suspense 边界分块**输出——能立即渲染的部分先发 HTML，慢的数据源对应的 Suspense 边界先发 fallback 占位，数据就绪后**同一连接继续推送**补丁脚本。
- 选择性 hydration：HydrationController 按流到达顺序逐块激活——先到的块**先完成 hydration 可交互**，不必等整页；用户点击尚未 hydrate 的区域时，React 会**优先 hydrate 该子树**再回放这次点击（18 的 selectNav 特性）。
- out-of-order 机制：慢块完成时推送内联脚本 `$RC("B:1", "S:1")`——把隐藏 div 里缓存的真 HTML **move 到 fallback 占位处**（服务端不重发整页）；客户端据此更新 Suspense 边界状态并 hydrate 新内容。
- 收益：TTFB 与 FCP 大幅提前、慢接口不再阻塞整页、交互就绪时间分段优化；这是 RSC（FRP-106）复用的同一套流协议。

```javascript
// 简化实现，帮助理解流式输出与 out-of-order 替换
function renderToStream(appTree) {
  const chunks = [];
  // 1. 先输出 shell：立即可渲染的部分 + 慢块占位
  chunks.push(`<div id="app">${appTree.fast}</div>`);
  appTree.slow.forEach((s, i) => {
    chunks.push(`<!--S:${i}-->` + s.fallback + `<!--/S:${i}-->`);
    chunks.push(`<div hidden id="P:${i}"><!-- 真实内容缓存区 --></div>`);
    s.promise.then((html) => {
      // 2. 数据就绪：把真 HTML 推入缓存区，再推替换脚本
      chunks.push(`<div hidden id="P:${i}">${html}</div>`);
      chunks.push(`<script>$RC("P:${i}","S:${i}")</script>`); // out-of-order 补丁
    });
  });
  return chunks;
}
// $RC：客户端 runtime 提供的全局函数（React 内部实现）—— move 缓存内容到占位并 hydrate
function $RC(contentId, placeholderId) {
  const content = document.getElementById(contentId);
  const placeholder = document.getElementById(placeholderId).previousSibling;
  placeholder.replaceWith(content.firstChild); // DOM move，不重新请求
  hydrateSubtree(content.firstChild);          // 只 hydrate 这一块：选择性 hydration
}
function hydrateSubtree(el) { /* 绑定事件与 fiber 恢复 */ void el; }

// 用法：首屏秒回，评论区 2 秒后到达
const stream = renderToStream({
  fast: '<header>Header</header>',
  slow: [{ fallback: '<span>loading comments...</span>',
    promise: new Promise((r) => setTimeout(() => r('<ul><li>comment</li></ul>'), 100)) }],
});
stream.forEach((c) => process.stdout?.write?.(c) ?? console.log(c));
// 输出顺序：header -> fallback 占位 -> （异步）真内容缓存区 + $RC 替换脚本
```
