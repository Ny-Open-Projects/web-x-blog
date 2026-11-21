---
title: [AGT-127] 自研 LLM 流式协议时，SSE 事件规范应该怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-127：自研 LLM 流式协议时，SSE 事件规范应该怎么设计？
**答**：
- OpenAI 原生 SSE 只带增量文本，业务流需要自己的事件类型：`meta`（会话/模型/预算）→ `delta`（增量）→ `tool_event`（工具执行过程）→ `done`（含完整 usage）→ `error`。
- 每个事件带单调递增 `seq`：前端据此检测乱序/丢包，丢包时不拼接脏数据，而是请求快照校正。
- 提供两类校正事件：`snapshot`（当前全量内容覆盖式重放）用于断线重连与丢包恢复；`usage` 单独成事件便于计费统计而不依赖拼接完整性。
- 事件用 `event:` 字段分类、`data:` 一行 JSON；版本号放 `meta` 事件里，后续加字段向前兼容。

```typescript
// 自研 SSE 流式协议：服务端发事件 + 客户端带 seq 校正的解析器
type StreamEvent =
  | { type: 'meta';        seq: 0;    sessionId: string; model: string; protoVersion: 2 }
  | { type: 'delta';       seq: number; text: string }
  | { type: 'tool_event';  seq: number; callId: string; phase: 'start' | 'end'; name: string; result?: string }
  | { type: 'snapshot';    seq: number; content: string }          // 校正：全量覆盖
  | { type: 'usage';       seq: number; promptTokens: number; completionTokens: number }
  | { type: 'done';        seq: number }
  | { type: 'error';       seq: number; code: string; message: string };

function emit(res: import('express').Response, e: StreamEvent) {
  res.write(`event: ${e.type}\n`);
  res.write(`data: ${JSON.stringify(e)}\n\n`);
}

class StreamClient {
  content = '';
  private lastSeq = -1;
  private buf: string[] = [];

  handle(e: StreamEvent): string {
    if (e.seq <= this.lastSeq) return this.content;              // 重复事件幂等
    if (e.seq > this.lastSeq + 1) {
      this.buf.push(e);                                          // 检测到缺口，先缓存
      if (this.buf.length > 10) { this.lastSeq = e.seq; this.content = ''; return this.content; } // 触发 snapshot 请求
      return this.content;
    }
    this.lastSeq = e.seq;
    switch (e.type) {
      case 'snapshot': this.content = e.content; break;          // 校正覆盖
      case 'delta':    this.content += e.text; break;
      case 'tool_event': /* 渲染工具过程卡片 */ break;
      case 'done':     this.content += '\u0000DONE'; break;      // 终止哨兵
      case 'error':    throw new Error(`${e.code}: ${e.message}`);
    }
    const next = this.buf.shift();
    if (next && next.seq === this.lastSeq + 1) this.handle(next); // 递归消费缓存
    return this.content;
  }
}
```

---

## 二十三、上下文工程
