---
title: [MFW-652] Suspense 错误边界在流中的行为
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-652：Suspense 错误边界在流中的行为

**答**:
- 流式渲染中的错误语义：1) **shell 已发后组件抛错**——HTML 已发送（不能改 status code）：错误边界的 fallback 流式注入（$RC 注入 error UI RBL-507）；2) **shell 内错误**（根级——页面 500 + error 页整发）；3) error.tsx 的流式版：段级 error 边界 = 流中的「错误占位替换」。
- 客户端错误恢复：流中的错误 UI 已注入 → error.tsx 的 reset() → 重新渲染该段（客户端导航/刷新语义 RBL-536）；「流中错误不影响其他段」的隔离语义。
- 服务端错误的上报：onError 回调（流中错误记录——trace/监控 RBL-542；「错误发生在流中」的延迟上报（错误时 shell 已发——500 无法返回——错误只能靠 onError 旁路上报而非响应码）。
- 追问钩子：为什么「shell 已发后错误」不能返回 500？——shell 已发 = 200 已写头（HTTP 语义：头不可撤回）；错误段只能流内降级（fallback 注入）；「错误监控的补偿」：响应码无法表达 → onError 旁路（错误计数/trace——监控依赖 onError 而非 status code）——流式架构的错误语义与「监控信号的位置」联动：监控必须适配流式（status-only 监控 = 流中错误全漏）。

```tsx
// 流式错误的三种形态
// 1) shell 内错误 → 整页 500 + error 页
// 2) 段内错误（流中）→ error.tsx fallback 流式注入
// app/products/[id]/error.tsx
'use client';
export default function Error({ error, reset }) {
  return <div role="alert">加载失败 <button onClick={reset}>重试</button></div>;
}
// 3) 段内错误的旁路上报
// instrumentation.ts
export function register() {
  // Next 的 onError 钩子
}
// page.tsx 渲染时
renderToPipeableStream(<App />, {
  onError(err, digest) {
    reportError(err, digest);                            // 旁路上报（响应码无法表达）
    console.error(digest);                               // digest 注入 HTML——client 可关联
  },
});
// 流中的错误 UI：$RC 注入 fallback（RBL-507）
// <div><!--$?--><template id="B:0"></template><!--/$--></div>
// <div hidden id="S:0"><div role="alert">加载失败</div></div>
// <script>$RC("0","S:0")</script>
```
