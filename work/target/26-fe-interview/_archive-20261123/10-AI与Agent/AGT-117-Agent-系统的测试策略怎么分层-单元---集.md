---
title: [AGT-117] Agent 系统的测试策略怎么分层（单元 / 集成 / E2E 各测什么）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-117：Agent 系统的测试策略怎么分层（单元 / 集成 / E2E 各测什么）？
**答**：
- 三层分工：单元层测确定性代码（SSE 解析/partial JSON/RRF 融合——mock 一切 LLM）；集成层测 Agent 循环编排（mock LLM 返回脚本化序列，验证工具调用与终止逻辑）；E2E 层用真实模型跑评测集（质量与回归，nightly）。
- mock LLM 是关键基建：按调用次序返回预设响应，让循环逻辑测试零成本、零随机性。
- 断言标准分层：单测 100% 确定性；评测集允许波动但卡阈值（AGT-093 回归流水线）。
- 契约测试兜底：MCP 工具/上游 API 用契约测试，防 provider 变更悄悄破坏。

```typescript
// vitest：mock LLM 的分层测试
import { describe, it, expect, vi } from 'vitest';

// 可编程 mock：按调用次序返回脚本化响应
function mockLLM(script: string[]) {
  let i = 0;
  return vi.fn(async () => script[i++] ?? 'done');
}

describe('ReAct 循环（集成层：mock LLM）', () => {
  it('搜索后汇总并终止', async () => {
    const llm = mockLLM([
      JSON.stringify({ type: 'act', thought: '先搜索', tool: 'search_docs', args: { q: '部署' } }),
      JSON.stringify({ type: 'final', thought: '已找到', answer: '部署方式是 Docker', confidence: 0.9 }),
    ]);
    const tools = new Map([['search_docs', vi.fn(async () => 'Docker 部署文档内容')]]);
    const result = await runAgentLoop({ llm, tools, maxSteps: 3 });
    expect(tools.get('search_docs')).toHaveBeenCalledWith({ q: '部署' }); // 编排正确
    expect(result.answer).toBe('部署方式是 Docker');
  });
});

describe('单元层：确定性代码', () => {
  it('partial JSON 解析跨 chunk', () => {
    expect(parsePartialJson('{"a": [1, "中')).toEqual({ a: [1, '中'] });
  });
});

describe('E2E 层：真实模型评测（nightly job 触发）', () => {
  it.skip('客服 Agent 评测集通过率 >= 0.9', async () => {
    const report = await runEvalSuite('customer-service');
    expect(report.passRate).toBeGreaterThanOrEqual(0.9);
  });
});
```
