---
title: [936] 给子 Agent 写任务书（task brief）有哪些生产级要求
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 上下文工程]
type: 面试题
---

## 936：给子 Agent 写任务书（task brief）有哪些生产级要求

**答**：
- 任务书四要素：目标（可验证的完成标准）、输入（数据/文件引用而非粘贴全文）、约束（禁止事项、预算、风格）、返回格式（JSON Schema）；缺一项子 Agent 就会自由发挥。
- 完成 Standard 必须可程序验证：如「输出包含测试通过标志」「diff 行数不超过 200」，不要写「尽量好一点」这种主观词。
- 反例强制：任务书里给 1 个「错误示范」比 3 条正面描述更能约束行为（模型对反例敏感）。
- 追问钩子：任务书太长会不会适得其反？——会，超过 500 token 的任务书优先考虑拆任务而不是加说明。

```ts
const briefSchema = z.object({
  goal: z.string(),                          // 可验证目标
  inputs: z.array(z.string()),               // artifact URI
  constraints: z.array(z.string()),
  forbidden: z.array(z.string()),            // 反例/禁止事项
  outputSchema: z.unknown(),
  budget: z.object({ rounds: z.number(), tokens: z.number() }),
});
// goal 示例：'修复 login.spec.ts 全部失败用例，返回 { passed: true, diff } 且 diff < 200 行'
```

