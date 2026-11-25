---
title: [AGT-584] 把流式 UI 渲染管线分层（传输/解析/缓冲/渲染/增强），每层职责边界怎么划？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-584：把流式 UI 渲染管线分层（传输/解析/缓冲/渲染/增强），每层职责边界怎么划

**答**：
- 传输层（SSE/WS 解码、seq 保序、断线补拉）→ 解析层（事件分发、块解析、JSON 渐进解析）→ 缓冲层（打字机节流、rAF 合帧、背压丢弃）→ 渲染层（块组件、虚拟滚动、状态机）→ 增强层（完成后高亮/公式/图表/操作按钮）。
- 层间契约用不可变事件对象（可回放/可测试），每层可独立单测——卡顿或丢字能二分定位到层。
- 反模式警示：跨层直调（渲染层直接改传输状态）、增强层参与流式（增强必须等 complete）是两大耦合源头。

```javascript
// 管线组装：每层入队出队，事件不可变
const pipeline = pipe(
  transport({ onReconnect: gapFetch }),   // 传输：seq/重连
  parse({ blockParser, jsonPartial }),    // 解析：块/渐进JSON
  buffer({ raf, typewriter }),            // 缓冲：节流合帧
  render({ virtualList, stateMachine }),  // 渲染：组件/状态
  enhance({ afterComplete: true }),       // 增强：只在完成后
);
// 回放测试：录一段真实事件流，逐层断言输出
replay(pipeline, recordedEvents, snapshotAssertions);
```

