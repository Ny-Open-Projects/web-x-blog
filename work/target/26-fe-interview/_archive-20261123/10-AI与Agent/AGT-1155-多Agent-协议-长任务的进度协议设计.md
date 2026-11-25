---
title: [1155] 长任务对外的进度事件协议怎么设计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 协议]
type: 面试题
---

## 1155：长任务对外的进度事件协议怎么设计

**答**：
- 事件类型集：phase_start/phase_end（阶段）、step（步骤）、artifact（产物就绪）、degrade（降级声明）、final、error；每个事件带 { taskId, seq, ts, payload }，seq 单调递增用于断点续传。
- 语义要求：phase_start 与 phase_end 必须配对（客户端据此渲染进度条）、degrade 必发（透明降级）、final 唯一且终局（之后不再有事件）。
- 兼容性：事件协议版本化（事件带 v 字段），新增事件类型对老客户端应可忽略——「未知事件不报错」是客户端义务，写进协议文档。
- 追问钩子：进度事件会不会暴露内部信息？——payload 白名单（预定义的事件 schema），自由字段一律过滤；进度协议和 trace 是两套，别把 trace 直接推给用户。

```ts
const PROTO = { v: 2, events: ['phase_start','phase_end','step','artifact','degrade','final','error'] };
function emit(ev) {
  assert(PROTO.events.includes(ev.type), '未知事件类型');
  bus.publish(`task.${ev.taskId}`, { v: PROTO.v, seq: ++seqOf(ev.taskId),
    ts: Date.now(), payload: whitelist(ev) });        // 白名单过滤
}
// 客户端：未知事件类型必须忽略不报错（协议义务）
```
