---
title: [AGT-194] Agent 可观测性的 OpenTelemetry 语义约定是什么？如何接入？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-194：Agent 可观测性的 OpenTelemetry 语义约定是什么？如何接入？
**答**：
- OTel 的 GenAI 语义约定把一次 LLM 应用运行映射为标准 Span 层级：根 span（agent.run）→ LLM 调用 span（gen_ai.* 属性：模型、token 数、温度）→ tool 执行 span → 检索 span（检索 query 与命中数）——各家 SDK 的私有 trace 格式有了统一出口。
- 核心属性命名空间：`gen_ai.system`（供应商）、`gen_ai.request.model`、`gen_ai.usage.input_tokens/output_tokens`、`gen_ai.prompt.0.content`（消息，需脱敏后采样上报）——采集侧统一后，后端 Jaeger/Tempo/Datadog 通用。
- 前端接入点：浏览器端用 OTel JS 上报用户侧体验 span（从发送到渲染完成），通过 traceparent 与后端 span 串联，实现「用户点了什么 → 后端哪一步慢」的完整链路。
- 采样与隐私策略：LLM 的 prompt/completion 内容默认不上报（体积与 PII 风险），只上报结构与用量；debug 时对特定 trace 开全量采样。

```typescript
// OTel GenAI 语义约定接入：Agent 运行 → 标准 span 链
import { trace, context, SpanStatusCode } from '@opentelemetry/api';

const tracer = trace.getTracer('agent-runtime', '1.0.0');

export async function tracedAgentRun(sessionId: string, input: string, run: () => Promise<string>) {
  return tracer.startActiveSpan('agent.run', {
    attributes: { 'gen_ai.system': 'openai', 'session.id': sessionId, 'agent.name': 'support-bot' },
  }, async (root) => {
    try {
      const answer = await tracedLlmCall('gpt-4o-mini', [{ role: 'user', content: input }], run);
      root.setStatus({ code: SpanStatusCode.OK });
      return answer;
    } catch (e) {
      root.setStatus({ code: SpanStatusCode.ERROR, message: (e as Error).message });
      throw e;
    } finally {
      root.end();
    }
  });
}

// LLM 调用 span：按 GenAI 约定记录属性（内容默认不上报）
async function tracedLlmCall(model: string, messages: unknown[], run: () => Promise<string>) {
  return tracer.startActiveSpan('chat.completions', {
    attributes: {
      'gen_ai.system': 'openai', 'gen_ai.request.model': model,
      'gen_ai.request.temperature': 0.7,
      'gen_ai.prompt.count': messages.length,       // 消息条数；内容走单独的 debug 采样
    },
  }, async (span) => {
    const out = await run();
    span.setAttributes({
      'gen_ai.usage.input_tokens': 1200, 'gen_ai.usage.output_tokens': 350,   // usage 归一后统一入属性
      'gen_ai.response.finish_reason': 'stop',
    });
    span.end();
    return out;
  });
}

// 工具执行 span + 前端串联：前端携带 traceparent，后端 span 自动挂到同一 trace
export function withToolSpan(name: string, fn: () => Promise<unknown>) {
  return tracer.startActiveSpan(`tool.${name}`, async (span) => {
    try { return await fn(); } finally { span.end(); }
  });
}
// 前端（OTel JS）：
//   fetch('/api/agent', { headers: { traceparent: activeSpan.spanContext()... } })
//   —— W3C Trace Context 透传，用户点击到模型调用的全链路一张图
```
