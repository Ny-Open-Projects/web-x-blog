---
title: [AIC-090] 团队的 AI 实践怎么持续沉淀？「好 prompt 复用率」和「实践文档化」之间怎么选？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-090：团队的 AI 实践怎么持续沉淀？「好 prompt 复用率」和「实践文档化」之间怎么选？
**答**：
- 沉淀物优先级：能复用的 prompt/模板 > 可执行的检查规则 > 叙述性经验文档——前两者直接改变产出，第三者容易被写完即忘。
- 复用率指标驱动：模板库统计「每个模板的月调用次数」，连续两月 0 调用的模板要么改进要么删除；复用率高的模板优先打磨质量。
- 文档化的唯一可行方式：把「经验」变成「钩子」——事故复盘落到规则（AIC-080）、最佳实践落到模板注释、踩坑落到失败样本库；纯文档（wiki 长文）只适合介绍型内容。
- 沉淀渠道要在工作流内：任务结束时一个命令提交「本次 prompt + 结果评分」，好经验自动进待审区，人每周花 15 分钟审一次——离工作流越远沉淀越死。
- 追问钩子：面试官考的是「你有没有让知识流动起来的机制设计」，答案里必须有指标和入口，否则就是空谈文化。

```javascript
// 一键沉淀：任务结束提交 prompt + 评分
async function promotePrompt(promptId, result) {
  await db.insert('prompt_candidates', {
    promptId, score: result.score, reusedFor: result.taskKind,
    status: 'pending_review', sampledOutput: result.sample,
  });
  // 每周审：score >= 4 且同类调用 >= 3 次 → 转正进 prompts/，走 PR review
}
```
