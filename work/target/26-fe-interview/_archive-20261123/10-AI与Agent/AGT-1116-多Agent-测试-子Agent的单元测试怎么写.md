---
title: [1116] 子 Agent 怎么做「单元测试」
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 测试]
type: 面试题
---

## 1116：子 Agent 怎么做「单元测试」

**答**：
- 子 Agent 单测的「单元」是：给定输入与 mock 工具，断言「行为序列 + 结构化输出」，不测自由文本的措辞——prompt 微调导致的措辞变化不应让测试失败。
- 测试金字塔：规则层（意图路由、格式校验）纯单测跑得快、Agent 层（mock 模型或录制的模型响应回放）测行为、集成层（真模型冒烟）每天少量。
- 录制回放：把真实模型响应录制为 fixture，单测用回放（稳定免费），模型升级时重录并 diff——回放既测编排逻辑又留档行为基线。
- 追问钩子：为什么不用真模型跑全量单测？——慢、贵、不确定（同输入不同输出会让断言飘），真模型只留给每日冒烟与夜间回归。

```ts
// 录制回放示例
const fixture = loadRecording('coder-1/fix-typo.json');  // 录制的模型响应
const agent = new CoderAgent({ llm: replayLlm(fixture) });
const out = await agent.run({ task: '修复拼写错误', tools: mockTools() });
expect(out.toolCalls.map(t => t.name)).toEqual(['read', 'edit', 'test']);
expect(out.diff).toMatchFixture('expected.diff');
```

