---
title: [AIC-864] 统一 SDK 如何屏蔽底层模型差异，让业务代码不感知供应商？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-864：统一 SDK 如何屏蔽底层模型差异，让业务代码不感知供应商？
**答**：
- 统一 SDK 的核心是**稳定契约**：高层只暴露「能力语义接口」（`chat / embed / evaluate`），把供应商的请求格式、流式协议、错误码、重试策略藏在 SDK 内部（适配器 AIC-808）。
- 差异分类处理：**语法差异**（字段名、事件格式）在适配器层翻译；**能力差异**（某模型不支持 function call）通过「能力声明 + 降级」处理，SDK 主动告知调用方「该能力不可用」而非静默失败；**语义差异**（同样 prompt 不同模型理解不同）无法完全屏蔽，要通过评测暴露并让调用方选择模型。
- SDK 要内置**横切能力**：重试/降级、血缘透传、配额、缓存、指标上报——业务不用自己实现，这也是平台价值的集中体现。
- 版本策略：SDK 用语义化版本（AIC-868），破坏性变更要提前公告+迁移工具；提供「兼容层」让业务平滑升级。
- 追问钩子：能说出「语法差异能屏蔽、能力差异靠声明降级、语义差异靠评测暴露——不要假装都能屏蔽」的候选人，对抽象边界有清醒认知。

```typescript
// 统一 SDK：高层只见能力语义，差异在内部收敛
interface ChatOptions { model?: string; temperature?: number; stream?: boolean }
interface ChatResult { text: string; usage: { tokens: number }; modelUsed: string }

class UnifiedSDK {
  async chat(prompt: string, opts: ChatOptions = {}): Promise<ChatResult> {
    const model = opts.model ?? 'default';
    const adapter = getAdapter(model);            // 内部选供应商
    if (opts.stream && !adapter.capabilities.includes('stream')) {
      // 能力差异：主动降级并告知，不静默失败
      console.warn('stream unsupported, falling back to sync');
    }
    // 横切能力：血缘、重试、配额、指标（业务无感）
    const span = tracer.start({ model, promptVersion: 'p1' });
    try {
      return await withRetry(() => adapter.chat({ prompt, ...opts }));
    } finally {
      meter.record('sdk.chat', { model });
      tracer.end(span);
    }
  }
}
// 业务：const res = await sdk.chat('你好'); —— 完全不感知底层
```
