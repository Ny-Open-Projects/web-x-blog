---
title: [MFW-854] 流式响应能被 CDN 缓存吗，Cache-Control 和 chunk 边界怎么配合
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-854：流式响应能被 CDN 缓存吗，Cache-Control 和 chunk 边界怎么配合

**答**：
- 结论：流式响应理论上可缓存，但 CDN 需缓冲完整流后才能作为缓存体；边到边（chunked）传输通常无法被中间缓存缓存。
- 落地：可缓存内容用「先缓冲后返回」（牺牲 TTFB 换缓存）；追 TTFB 的流式页设 no-store/private，由 ISR 预生成页承担缓存。
- 追问钩子：PPR 如何兼得？——静态壳走 CDN 缓存（完整缓冲），动态洞走流式 no-store。

```javascript
// 模式 A：缓冲后返回 → 可缓存，TTFB 高
async function buffered(req, res) {
  const html = await renderComplete();               // 等全部完成
  res.setHeader('Cache-Control', 'public, s-maxage=60');
  res.end(html);
}
// 模式 B：边到边流式 → 低 TTFB，不可中间缓存
async function streaming(req, res) {
  res.setHeader('Cache-Control', 'private, no-store');
  for await (const c of renderChunks()) res.write(c);
  res.end();
}
// PPR：壳=模式A（CDN 缓存），洞=模式B（流式私有）
```
