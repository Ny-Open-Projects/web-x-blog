---
title: [AGT-118] 冷启动如何优化（首 token 延迟优化全清单）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-118：冷启动如何优化（首 token 延迟优化全清单）？
**答**：
- 首 token 延迟（TTFT）构成：网络往返 + 请求排队 + prompt 处理（prefill）+ 模型调度；TTFT 与输入 token 数强相关——砍输入是最直接的手段。
- 优化清单：系统提示瘦身与历史摘要化、检索条数收敛、上游前缀缓存（system 与历史稳定在前）、keep-alive 连接复用、网关与模型同区域部署。
- 体验兜底：流式 + 骨架屏把「等待」变「进行中」；超时分级（2s 提示、8s 提供取消）。
- 监控按 P50/P95/P99 分位而非均值，TTFT 与总时长分开看。

```typescript
// TTFT 测量与冷启动优化落地
export async function streamWithTTFT(messages: ChatMessage[], onDelta: (t: string) => void) {
  const t0 = performance.now();
  let firstTokenAt: number | null = null;
  // keep-alive：Node 侧复用连接，省 TCP + TLS 握手
  // new https.Agent({ keepAlive: true, maxSockets: 64 })

  // prefix caching：system 与历史稳定在 messages 前部，命中上游前缀缓存
  const res = await upStream({
    model: 'gpt-4o-mini',
    messages,                                   // 输入越短 prefill 越快
    stream: true,
    stream_options: { include_usage: true },
  });
  for await (const ev of parseSSE(res.body!)) {
    if (ev.data === '[DONE]') break;
    const delta = JSON.parse(ev.data)?.choices?.[0]?.delta?.content;
    if (delta) {
      if (firstTokenAt === null) {
        firstTokenAt = performance.now();
        metrics.record('ttft_ms', firstTokenAt - t0);      // 按 P95 观测
      }
      onDelta(delta);                                      // 骨架屏已提前展示，这里接增量
    }
  }
  metrics.record('total_ms', performance.now() - t0);
}
// 前端：请求发出的瞬间渲染思考骨架屏，感知延迟与真实 TTFT 解耦
```
