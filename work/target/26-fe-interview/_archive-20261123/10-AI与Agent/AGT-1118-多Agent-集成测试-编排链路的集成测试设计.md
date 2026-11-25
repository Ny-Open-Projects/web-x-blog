---
title: [1118] 多 Agent 链路的集成测试怎么设计才稳
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 测试]
type: 面试题
---

## 1118：多 Agent 链路的集成测试怎么设计才稳

**答**：
- 集成测试的稳定性来源：环境固定（固定模型版本/固定工具 mock/固定知识库快照），否则每次跑结果都不同没法断言。
- 断言分层：流程断言（走了哪些 Agent、步骤顺序）稳定必测；结果断言（最终产物质量）允许区间断言（如「覆盖率 ≥ 80% 的要点」）；避免精确匹配自由文本。
- 失败隔离：链路失败时报告指出「首次失败的 Agent 与其上游输入」，帮开发者不用从头追——集成测试的调试成本主要在这里。
- 追问钩子：知识库快照怎么固定？——用固定的测试知识库（少量文档、内容进 Git），绝不用生产库做集成测试环境（内容变化会让测试随机挂）。

```ts
const env = fixedEnv({ model: LOCKED_VER, kb: testKb, tools: mockTools });
test('文档审校链路', async () => {
  const t = await orchestrator.run(FIXTURE_TASK, { env });
  expect(t.path).toEqual(['planner', 'reviewer', 'fixer', 'verifier']); // 流程断言
  expect(t.coverage).toBeGreaterThan(0.8);                              // 区间断言
});
```

