---
title: [AIC-041] AI Code Review 在整个质量门禁流水线里应该放在哪一步？它替代和不能替代什么？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-041：AI Code Review 在整个质量门禁流水线里应该放在哪一步？它替代和不能替代什么？
**答**：
- 摆放位置：lint/type-check/单测之后、人类 review 之前——先用廉价确定性工具过滤掉低级问题，AI 审「语义层」（逻辑漏洞、边界、设计），人只审「意图与取舍」。
- 能替代：风格类意见（本来就该 lint 管）、明显 bug 模式、遗漏的边界处理、缺失测试的提醒——机械量大且规则明确的部分。
- 不能替代：业务正确性判断、架构取舍、与产品需求的对齐、团队政治与沟通——这些信息在 diff 之外。
- 关键设计：AI 意见必须分级（blocker/suggestion/nit），只有 blocker 参与阻断；否则噪音会把人淹没导致「狼来了」。
- 追问钩子：AI review 的意见也要留痕统计——意见采纳率低于 20% 的规则类别应下线，防止门禁变成噪音源。

```yaml
# 门禁流水线（.ai/gate.yml 示意）
pipeline:
  - lint          # ESLint
  - typecheck     # tsc --noEmit
  - unit-test     # vitest
  - ai-review:    # 语义层审查，产出分级意见
      model: reviewer-v2
      prompt: prompts/review.md
      levels: [blocker, suggestion, nit]
      block_on: [blocker]
  - human-review  # 只处理 blocker 解释 + 意图确认
```
