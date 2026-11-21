---
title: [DP-261] 源码识别：Next.js Streaming/渐进注水源码中的调度？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-261：源码识别：Next.js Streaming/渐进注水源码中的调度？
**答**:
- 流式模板：SSR 输出骨架（含 Suspense placeholder）先发送，慢数据 resolve 后继续推送对应 chunk（<template> 填充 + 脚本交换）——"先到先渲染"的流水线。
- 观察者（水合协调）：客户端按 chunk 到达顺序逐步水合（selective hydration），事件优先级（被点击区域优先水合）是调度策略。
- 命令：水合完成边界发送的脚本（$RC(resolve, node)）是"占位替换"命令。
- 识别要点：能说清"SSR 流式的 TTFB 与 FCP 解耦"——慢模块不再阻塞整个 HTML。

```javascript
// React 18 renderToPipeableStream（源码级心智）
renderToPipeableStream(
  <Layout><Suspense fallback={<Skel/>}><SlowList/></Suspense></Layout>,
  {
    onShellReady() { pipe(res); },            // 1) 骨架立即冲刷
    onError(e) { log(e); },
  },
);
// SlowList resolve → React 序列化该 Suspense 边界内容 → 追加 chunk：
// <template id="S:1">…真实内容…</template><script>$RC("S:1","B:0")</script>   // 替换命令
// 客户端：selective hydration —— 用户先点哪块先水合哪块（idle 剩余块排队，优先级调度）
```
