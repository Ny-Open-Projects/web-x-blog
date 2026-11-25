---
title: [MFW-505] RSC 流式渲染的背压：可读流的暂停策略与渲染调度
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-505：RSC 流式渲染的背压：可读流暂停与渲染调度

**答**:
- Flight 流的背压：RenderToPipeableStream 输出是 ReadableStream——消费端（HTTP 响应）读取慢时（客户端慢网络）流 backpressure → 渲染暂停？实际行为：**框架不暂停渲染**（渲染继续产出塞缓冲区）——内存增长风险；工程缓解：响应缓冲上限 + 慢客户端超时断开（僵尸连接治理）。
- 调度优先级：Suspense 边界的 resolve 顺序 = 数据到达顺序（不是 importance）——「关键内容后到」的体验问题需要显式调度：关键 Suspense 外层优先（组件树层次控制优先级）+ `renderToReadableStream` 的 onError/onShellReady 时机控制。
- 流的阶段语义：shell ready（同步部分完成，可立即发送 HTML）→ 后续流式补丁；「shell 最小化」是 TTFB 优化的核心（shell 只含骨架——RBL-14 目录的流式基座）。
- abort 语义：客户端断开 → 渲染 abort（onError 收到 abort 错误——数据获取取消传播到 DB 查询——AbortSignal 贯穿 RBL-639 的 SSR 版）。
- 追问钩子：为什么 SSR 流式「不暂停渲染」而 API 流式（SSE）要背压？——SSR 渲染的产出是「一次性的」（这次请求的数据），暂停渲染只延迟不省计算（数据已在内存）；SSE 的生产端可能是持续源（DB CDC）需要真背压；理解「背压的价值 = 生产可再生」——不可再生的渲染选择缓冲 + 超时，可再生的流选择暂停。

```javascript
// SSR 流式渲染的背压治理
import { renderToPipeableStream } from 'react-dom/server';
app.get('/', (req, res) => {
  const { pipe, abort } = renderToPipeableStream(<App />, {
    onShellReady() { pipe(res); },                       // shell 即发：TTFB 最小
    onError(err) {
      if (req.aborted) abort();                          // 客户端断开传播
      else logError(err);
    },
  });
  req.on('close', () => abort());                        // 断开即中止渲染
  // 僵尸连接防护：慢客户端超时
  const watchdog = setTimeout(() => {
    if (!res.writableEnded) { abort(); res.destroy(); }
  }, 30000);
  res.on('finish', () => clearTimeout(watchdog));
});
// 数据获取的取消传播
async function getData(signal) {
  const rows = await db.query('...', { signal });        // AbortSignal 传到 DB
  return rows;
}
```
