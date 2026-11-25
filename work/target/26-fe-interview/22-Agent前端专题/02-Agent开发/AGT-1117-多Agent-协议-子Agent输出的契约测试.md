---
title: [1117] 子 Agent 输出契约（Schema）怎么测
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 契约]
type: 面试题
---

## 1117：子 Agent 输出契约（Schema）怎么测

**答**：
- 契约测试测「边界」：输出必须通过声明的 JSON Schema（必填字段、枚举值、类型），消费方（下游 Agent）按契约依赖——契约变了下游就崩，所以契约变更是 breaking change，要走版本化。
- 双向契约：生产方测「我的输出满足契约」，消费方测「我能处理契约允许的所有合法值」——很多 bug 是消费方只处理了常见值。
- 契约演进纪律：加可选字段=兼容；改类型/删字段=升版本（v1/v2 并存过渡期），下游迁移完再下线 v1。
- 追问钩子：模型输出偶发不满足契约怎么办？——重试（带上错误信息让模型自修，2 次）→ 降级（宽松模式 + 标记）→ 失败上报；「契约失败率」本身是核心监控指标。

```ts
const outSchema = z.object({ status: z.enum(['ok','partial','failed']),
  artifacts: z.array(z.string()), summary: z.string().max(200) });
async function runCoder(task) {
  for (let i = 0; i < 2; i++) {
    const raw = await llm(briefPrompt(task), { retryHint: i && '上次输出未通过 schema' });
    const parsed = outSchema.safeParse(raw);
    if (parsed.success) return parsed.data;
  }
  return degrade(task);   // 宽松降级 + 标记
}
```

