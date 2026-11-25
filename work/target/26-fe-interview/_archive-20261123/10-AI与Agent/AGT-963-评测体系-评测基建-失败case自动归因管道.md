---
title: [963] 评测失败后自动归因的管道怎么搭
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 评测, 归因]
type: 面试题
---

## 963：评测失败后自动归因的管道怎么搭

**答**：
- 归因管道四步：捕获失败（断言不过 + trace）→ 自动分类（规则先行：工具调用错位/检索空/格式非法）→ LLM 归因（给失败 trace 让模型输出「失败环节 + 假设原因 + 建议改动」）→ 入看板按类别聚合。
- 规则归因优先：70% 的失败能用规则直接定位（如「调用了不存在的工具」），LLM 只处理规则剩余的 30%，成本可控。
- 归因结果必须可反驳：每个自动归因带「证据引用」（trace 的哪一步），人工审核时能快速验证或推翻。
- 追问钩子：归因和修复怎么联动？——按类别建立「标准修复动作」库（检索空 → 查索引健康；格式非法 → 加结构化输出约束），常见类自动生成修复 PR 草案。

```ts
async function attribute(fail) {
  const rule = rules.find(r => r.match(fail.trace));      // 规则先行
  if (rule) return { ...rule.classify(fail), by: 'rule' };
  const llm = await llmAttribute(fail.trace);             // LLM 兜底
  return { ...llm, by: 'llm', evidence: llm.steps };      // 必须带证据
}
```

