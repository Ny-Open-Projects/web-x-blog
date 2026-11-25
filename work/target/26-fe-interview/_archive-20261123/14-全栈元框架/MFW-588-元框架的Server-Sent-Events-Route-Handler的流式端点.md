---
title: [MFW-588] Route Handler 的流式端点：SSE 与 ReadableStream 的生产实践
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-588：Route Handler 流式端点的生产实践

**答**:
- SSE Route Handler 的生产要素（RBL-570 扩展）：1) **响应头三件套**（content-type: text/event-stream / cache-control: no-cache, no-transform / connection: keep-alive）；2) **服务器超时**（平台函数时限——长连接的任务委派 RBL-569 或 keepalive 续命）；3) **取消传播**（req.signal abort → 上游流取消 RBL-563）；4) **代理缓冲**（nginx 的 proxy_buffering off——缓冲破坏流式实时性：代理配置是流式的隐形杀手）。
- 流式端点的背压：ReadableStream 的 pull 语义（消费端驱动——数据生成按需：LLM token 流的场景）；「生成即推 vs pull 驱动」——pull 驱动防内存膨胀。
- 数据库长连接与流：流式 handler 期间持有的 DB 连接（连接池占用时长 = 流时长——长流耗尽池）；「流内查询的连接释放」（分批查询每批释放）。
- 追问钩子：为什么「代理缓冲」是 SSE 在生产中最常见的静默故障？——nginx 默认 proxy_buffering on（攒够 buffer 才转发——client 一次收到全量而非流式：「SSE 变成了长轮询」——功能看似正常但实时性丢失）；静默的原因：本地 dev 无代理（直接 Node）——上生产经 nginx 才触发；「环境差异的静默故障」类（RBL-956 静默清单）：流式功能的代理配置要进部署检查单。

```typescript
// 流式 Route Handler 生产版
export const runtime = 'edge';                           // 或 nodejs（注意函数超时）
export async function GET(req: Request) {
  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    async pull(controller) {                             // pull 驱动：消费端拉
      const token = await llm.next();                    // 按需生成
      if (token.done) { controller.close(); return; }
      controller.enqueue(encoder.encode(`data: ${JSON.stringify(token)}\n\n`));
    },
    cancel() {
      llm.abort();                                       // client 断开 → 上游取消
    },
  });
  return new Response(stream, {
    headers: {
      'content-type': 'text/event-stream',
      'cache-control': 'no-cache, no-transform',
      'x-accel-buffering': 'no',                         // nginx 缓冲禁用提示
    },
  });
}
// nginx 部署检查单
// proxy_buffering off; proxy_cache off;
# proxy_read_timeout 300s;  # 长连接超时对齐
```
