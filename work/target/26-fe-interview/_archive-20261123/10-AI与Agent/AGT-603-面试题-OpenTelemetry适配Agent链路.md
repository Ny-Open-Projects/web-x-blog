---
title: [AGT-603] 把 Agent 链路接入公司现有 OTel 体系，semantic convention 怎么定？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-603：把 Agent 链路接入公司现有 OTel 体系，semantic convention 怎么定

**答**：
- 复用 OTel 三大信号：trace（span 树）、metrics（tokens/成本/延迟直方图）、logs（结构化日志带 traceId）；不自造协议，用 gen_ai semantic convention（gen_ai.system/model/usage.tokens 等属性名）。
- 前端用 OTel JS SDK 生成 traceId 并通过 HTTP header（traceparent）透传，服务端续接——前端只需注入，不必采集全量 span（前端 span 采样率低）。
- 采样策略分级：错误与高成本任务 100% 采集，正常任务头部采样（如 10%），调试会话强制全采。

```javascript
// 前端：生成并透传 traceparent
import { context, trace } from '@opentelemetry/api';
const span = trace.getTracer('ai-ui').startSpan('agent.ui.turn');
const tc = propagation.Carrier();
propagation.inject(context.active(), tc);     // { traceparent: '00-...' }
fetch('/api/agent/run', { headers: tc });
// 服务端属性名走 gen_ai 约定
span.setAttribute('gen_ai.system', 'openai');
span.setAttribute('gen_ai.usage.prompt_tokens', usage.promptTokens);
```

