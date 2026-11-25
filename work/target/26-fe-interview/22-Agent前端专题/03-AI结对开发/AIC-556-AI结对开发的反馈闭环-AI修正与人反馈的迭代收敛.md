---
title: [AIC-556] AI 修正与人反馈的迭代收敛
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-556：AI 迭代收敛

**答**:
- AI 修正的迭代收敛模型（RBL-509 的深化）：1) **收敛条件**：AI 输出的变化量递减（第 1 轮改 50 行、第 2 轮改 10 行、第 3 轮改 2 行——收敛到 0 = 稳定）；2) **不收敛的信号**：变化量不递减（每轮都大改——AI 在"震荡"而非收敛——需要人介入而非继续迭代）；3) **震荡的原因**：反馈矛盾（第 1 轮说"用 hooks"第 2 轮说"不要 hooks"——AI 在两个指令间震荡）；反馈模糊（"不对"——AI 不知道怎么改——每轮随机变化）；4) **收敛检测**：连续 2 轮的变化量 < 上轮的 50% → 正在收敛；变化量不降或上升 → 震荡 → 需要人重新描述意图。
- 追问钩子：为什么「反馈包含原因」能加速收敛？——"不对" = AI 只知道错了不知道为什么（下一轮可能换一个错误方向——随机搜索）；"不对，因为 async 函数不能用 forEach" = AI 知道错误原因（下一轮直接修正原因——定向修正）；「反馈的信息量 = 收敛速度」：有原因的反馈 = 定向修正（1 轮收敛）；无原因的反馈 = 随机搜索（可能 N 轮不收敛）；Navigator 的核心技能 = 给出包含原因的反馈（RBL-501 的"精确指导"）。

```typescript
// AI 迭代收敛检测
interface Iteration { output: string; feedback?: string; changedLines: number; }
function checkConvergence(iterations: Iteration[], { convergeRatio = 0.5 } = {}) {
  if (iterations.length < 2)
    return { converging: null, oscillating: false, changes: [] };
  const changes = iterations.map(i => i.changedLines);
  const ratios: number[] = [];
  for (let i = 1; i < changes.length; i++) {
    ratios.push(changes[i - 1] > 0 ? +(changes[i] / changes[i - 1]).toFixed(2) : 0);
  }
  // 收敛：连续比率 < convergeRatio
  const converging = ratios.slice(-2).every(r => r < convergeRatio);
  // 震荡：变化量不减或增加
  const oscillating = ratios.slice(-2).some(r => r >= 1);
  const hasReasonFeedback = iterations.some(i => i.feedback && i.feedback.length > 20);
  return { converging, oscillating, changes, ratios,
    suggestion: oscillating
      ? '检测到震荡——请提供包含原因的具体反馈（而非"不对"）'
      : converging ? '正在收敛——继续当前迭代' : '需要更多迭代或人介入' };
}

// 自测
// 收敛：变化量递减
let r = checkConvergence([
  { output: 'v1', changedLines: 50 },
  { output: 'v2', changedLines: 10, feedback: '不对，因为 async 函数不能用 forEach' },
  { output: 'v3', changedLines: 2 },
]);
console.log(r.converging === true && r.oscillating === false);

// 震荡：变化量不减
r = checkConvergence([
  { output: 'v1', changedLines: 50 },
  { output: 'v2', changedLines: 60 },                    // 增加！
  { output: 'v3', changedLines: 55 },                    // 不减
]);
console.log(r.oscillating === true);
console.log(r.suggestion.includes('震荡'));

// 单轮
r = checkConvergence([{ output: 'v1', changedLines: 10 }]);
console.log(r.converging === null);                      // 不够数据
// 空轮
console.log(checkConvergence([]).converging === null);
```

**评分点**：
- 收敛检测（连续比率 < 50% = 递减——变化量收敛的量化）；震荡检测（变化量不减——AI 在两个方向间跳动）
- 反馈质量的影响（有原因的反馈 = 定向修正——收敛加速）；suggestion 的可操作性
- 边界（单轮/空轮/连续收敛/震荡）；收敛的量化指标
- 能说清「反馈包含原因 = 定向修正加速收敛；无原因反馈 = AI 随机搜索可能震荡——Navigator 的核心技能是给出精确反馈」属于加分
