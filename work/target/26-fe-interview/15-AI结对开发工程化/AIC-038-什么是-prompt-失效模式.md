---
title: [AIC-038] Prompt 的常见失效模式有哪些？团队怎么系统化地发现和修复这些失效？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-038：Prompt 的常见失效模式有哪些？团队怎么系统化地发现和修复这些失效？
**答**：
- 典型失效模式：约束被无视（规则太多丢中段）、格式漂移（输出越来越啰嗦）、上下文遗忘（长会话忘掉早期要求）、指令覆盖（贴入的代码里藏着新指令）、过度顺从（明明方案有错还硬写）。
- 系统化发现：建立「失败样本库」——每次 AI 产出不可用，记录 prompt、模型、失败类别；月度归类看 TOP 失效模式。
- 修复闭环：对着失败样本改模板 → 用同批任务回归测试新旧模板 → 通过后合入版本化的模板库（prompt 也是代码，要 review 要回滚）。
- 指标化：每类任务的「一次通过率」「返工次数」是 prompt 健康度的直接指标，跌破阈值触发模板治理。
- 追问钩子：失效往往不是模型退步而是**任务构成变了**（新业务、新框架），所以模板库要随技术栈演进定期复审。

```javascript
// 失败样本登记结构（最小可用 schema）
function logPromptFailure({ taskKind, promptVersion, model, category, diff, note }) {
  const categories = ['constraint_ignored', 'format_drift', 'context_forget',
                      'injection', 'sycophancy', 'hallucination'];
  if (!categories.includes(category)) throw new Error('bad category');
  db.insert('prompt_failures', { taskKind, promptVersion, model, category, diff, note, at: Date.now() });
}
// 月度统计：按 category 聚合，找出 top 失效模式驱动模板修复
```
