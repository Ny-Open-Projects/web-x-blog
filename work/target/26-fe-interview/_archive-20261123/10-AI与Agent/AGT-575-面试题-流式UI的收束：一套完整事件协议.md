---
title: [AGT-575] 把流式 UI 需要的事件收敛成一套协议（delta/tool/lifecycle/control），怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-575：把流式 UI 需要的事件收敛成一套协议（delta/tool/lifecycle/control），怎么设计

**答**：
- 四类事件：data 类（text delta/thinking/tool_call/tool_result）、lifecycle 类（turn_start/done/aborted/error/moderation_stop）、control 类（heartbeat/progress/stall）、meta 类（usage/citations/model_info）。每类事件有稳定 schema 与版本号。
- 关键设计：所有事件带 seq（补拉对齐）与 turnId（多回合复用一条连接）；事件处理前端侧分发到独立 reducer（渲染只认 data 类，监控只认 control 类）。
- 兼容演进：未知事件类型必须可忽略（forward-compatible），新增事件不炸老客户端。

```javascript
const HANDLERS = {
  'text.delta': (s, e) => s.buffer += e.data,
  'tool.call':  (s, e) => s.timeline.add(e.data),
  'tool.result':(s, e) => s.timeline.fill(e.data),
  'turn.done':  (s, e) => finalize(s, e),
  'heartbeat':  (s) => { s.lastEvent = Date.now(); },
  // 未知类型：静默忽略，兼容升级
};
function dispatch(state, ev) {
  state.lastSeq = ev.seq;                       // 统一 seq 维护
  (HANDLERS[ev.type] ?? noop)(state, ev);
}
```

