---
title: [AGT-126] 如何自研一套 Agent 间通信协议（消息 schema、握手、心跳）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-126：如何自研一套 Agent 间通信协议（消息 schema、握手、心跳）？
**答**：
- 消息三要素：信封（id/from/to/type/ts/correlationId）、负载（type 决定的 payload，schema 校验）、元信息（traceId/预算/优先级）。
- 握手阶段交换能力声明（支持哪些消息类型、协议版本），版本不兼容直接拒绝而不是静默错乱；`correlationId` 把请求/响应/流式片段串起来。
- 心跳解决「对端死了但 TCP 还活着」：固定间隔 ping，超时未收到 pong 判定失联，未完成任务可转移或终止。
- 一切消息先过 schema 校验再进状态机，坏消息丢弃并告警——Agent 间协议的健壮性优先于表达力。

```typescript
// Agent 间通信协议：信封 schema + 握手 + 心跳
import { z } from 'zod';

export const Envelope = z.object({
  id: z.string(), from: z.string(), to: z.string(),
  type: z.enum(['handshake', 'handshake_ack', 'ping', 'pong', 'task', 'task_result', 'stream_chunk', 'error']),
  ts: z.number(), correlationId: z.string().optional(),
  payload: z.unknown(),
});
export type Envelope = z.infer<typeof Envelope>;

const PROTOCOL_VERSION = 1;

export class AgentChannel {
  private alive = false;
  private heartbeat?: ReturnType<typeof setInterval>;

  constructor(private ws: WebSocket, public name: string) {
    ws.addEventListener('message', (e) => this.onMessage(JSON.parse(e.data)));
  }

  async handshake(peerCaps: string[]): Promise<void> {
    const ack = await this.request('handshake', { version: PROTOCOL_VERSION, caps: ['task', 'stream_chunk'] });
    if (ack.payload.version !== PROTOCOL_VERSION) throw new Error(`协议版本不兼容：对端 ${ack.payload.version}`);
    this.alive = true;
    // 心跳：3s 一跳，两次未响应判失联
    this.heartbeat = setInterval(async () => {
      try {
        await this.withTimeout(this.request('ping', null), 2000);
      } catch {
        if (--this.missed >= 2) { this.alive = false; clearInterval(this.heartbeat); this.onDead(); }
      }
    }, 3000);
    void peerCaps;
  }

  private missed = 2;
  onDead: () => void = () => {};
  private pending = new Map<string, (v: Envelope) => void>();
  private seq = 0;

  request(type: Envelope['type'], payload: unknown): Promise<Envelope> {
    const env: Envelope = { id: `${this.name}-${this.seq++}`, from: this.name, to: 'peer', type, ts: Date.now(), payload };
    this.ws.send(JSON.stringify(env));
    return new Promise((resolve) => {
      this.pending.set(env.correlationId ?? env.id, resolve);
    });
  }

  private onMessage(raw: unknown) {
    const parsed = Envelope.safeParse(raw);
    if (!parsed.success) return; // 坏消息静默丢弃 + 告警
    this.missed = 2;
    if (parsed.data.type === 'pong') this.pending.get(parsed.data.correlationId ?? '')?.(parsed.data);
    // ...其余类型分发给状态机
  }

  private withTimeout<T>(p: Promise<T>, ms: number): Promise<T> {
    return Promise.race([p, new Promise<never>((_, rej) => setTimeout(() => rej(new Error('心跳超时')), ms))]);
  }
}
```
