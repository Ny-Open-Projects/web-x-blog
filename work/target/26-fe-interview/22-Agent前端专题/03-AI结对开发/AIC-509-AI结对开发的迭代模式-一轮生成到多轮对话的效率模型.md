---
title: [AIC-509] AI 结对的迭代模式与效率模型
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-509：AI 迭代模式与效率模型

**答**:
- AI 迭代的效率模型：1) **一轮生成**（精确 prompt → AI 一次通过——效率最高但 prompt 成本高（需要完整接口/约束/示例）；2) **多轮对话**（模糊 prompt → AI 试错 → 人反馈 → AI 修正（3~5 轮收敛）——prompt 成本低但时间成本高；3) **效率公式**：`总时间 = prompt 时间 + N × (AI 生成 + 人审查 + 反馈)`——N（迭代次数）与 prompt 精确性负相关；「一轮生成的 ROI」：prompt 多花 5 分钟、省 3 轮迭代 × 2 分钟 = 省 1 分钟——ROI 取决于任务复杂度（简单任务模糊即可、复杂任务精确 prompt 回报高）。
- 迭代模式的决策树：1) 简单任务（<10 行）→ Inline 模式（一次补全——不值得多轮对话）；2) 中等任务（10~100 行）→ Chat 模式（2~3 轮——结构化 prompt）；3) 复杂任务（>100 行/多文件）→ Agent 模式（任务描述 + AI 自主迭代——人审最终 diff）；「模式选择的决策维度」= 任务复杂度 × 变更范围 × 审查成本。
- 追问钩子：为什么「AI 的迭代收敛速度」取决于「人的反馈质量」？——AI 试错：错误输出 → 人反馈"不对，是因为 X" → AI 修正；"X" 的精确性决定修正效率（"不对" = AI 再猜；"不对，因为 async 函数不能用 forEach" = AI 一次修正）；「反馈的信息量」：包含原因的反馈 = AI 一次修正；不包含原因 = AI 继续猜（迭代次数不减）——人的反馈质量 = AI 的收敛速度（Navigator 的角色不仅是审查而是「精确指导」）。

```typescript
// AI 迭代效率模型
interface Iteration { prompt: string; aiOutput: string; humanFeedback?: string; }
function estimateIterations(task: { complexity: 'simple'|'medium'|'complex', promptQuality: 1|2|3 }): number {
  const base = { simple: 1, medium: 2, complex: 4 };
  const qualityBonus = { 1: 2, 2: 1, 3: 0 };            // prompt 越精确迭代越少
  return Math.max(1, base[task.complexity] - qualityBonus[task.promptQuality]);
}
// 总时间估算
function totalEffort(task, aiSpeedSec = 5, humanReviewSec = 30, promptSec = 60) {
  const iters = estimateIterations(task);
  const promptTime = task.promptQuality === 3 ? promptSec * 2 : promptSec;  // 精确 prompt 更长
  return {
    iterations: iters,
    totalTimeSec: promptTime + iters * (aiSpeedSec + humanReviewSec),
    savingVsNoAI: iters * 300,                           // 对比人工写码 5min/迭代
  };
}
console.log(totalEffort({ complexity: 'medium', promptQuality: 3 }));
// { iterations: 1, totalTimeSec: 155, savingVsNoAI: 600 }
```
