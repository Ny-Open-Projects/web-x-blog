---
title: [MFW-872] 流式渲染里 HTML 壳和 Flight payload 双流的 Span 怎么拼成一条完整 trace
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-872：流式渲染里 HTML 壳和 Flight payload 双流的 Span 怎么拼成一条完整 trace

**答**：
- 结论：HTML 流与 RSC Flight 流是两条 HTTP 响应但属于同一次渲染；用统一 traceId + spanId + parentId 贯穿，客户端把它们拼成一棵调用树。
- 落地：服务端为每个 Suspense 边界创建 span，HTML 段与 Flight chunk 携带相同 traceId；采集端按 parentId 重建父子关系。
- 追问钩子：为什么不用两个独立 trace？——无法回答「这个 Flight chunk 对应哪段 HTML、耗时多少」。

```javascript
function startRenderTrace(traceId) {
  const spans = [];
  function span(name, parentId, attrs = {}) {
    const s = { traceId, spanId: genId(), parentId, name, attrs, t0: Date.now() };
    spans.push(s);
    return s;
  }
  function finish(s) { s.duration = Date.now() - s.t0; }
  // HTML 壳 span 与 Flight 洞 span 共享 traceId，用 parentId 关联
  const shell = span('html.shell', null);
  const hole = span('flight.hole', shell.spanId, { boundary: 'comments' });
  return { spans, span, finish, shell, hole };
}
// 采集端：按 parentId 把两流 span 重建为单一 trace 树
```
