---
title: [AIC-648] AI 生成代码的圈复杂度回归怎么在 CI 拦截？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-648：AI 生成代码的圈复杂度回归怎么在 CI 拦截？

**答**：
- 结论先行：**用「基线 + 增量阈值」拦截——不要求全仓复杂度达标（历史包袱），只要求本次 AI 新增/修改的函数不超过复杂度阈值**。新增即卡，存量放过（AIC-264 历史包袱）。
- 为什么 AI 容易写高复杂度代码：AI 倾向「一个函数解决所有情况」，堆满 if/switch 嵌套，尤其需求描述含多个条件分支时——它把条件直接翻译成嵌套，不做抽象（AIC-582 认知复杂度）。
- 拦截设计：1) **算基线**：对每个文件记录当前复杂度，作为基线；2) **增量检查**：CI 中计算变更后函数的复杂度，超过基线且超过绝对阈值（如 CC>15）就告警/阻断；3) **分级**：核心模块严（CC>10 阻断），展示模块松（CC>20 告警）；4) **给 AI 反馈**：拦截信息不只是「复杂度高」，而要给出「建议拆出 X 函数」——让 AI 自动重构重试（AIC-558 安全重构）。
- 边界：复杂度指标不完美——有些必要逻辑天然复杂，要允许人工豁免（写理由），避免一刀切。
- 追问钩子：为什么「增量阈值」比「全仓阈值」更能落地？——因为全仓阈值一开，存量代码满屏告警，团队直接忽略（AIC-264）；增量阈值只卡新代码，问题数可控、责任清晰——治理要从「止血」开始，而非「清算历史」。

```typescript
type FnMetric = { name: string; complexity: number; baseline: number; critical: boolean };

function checkComplexityRegressions(fns: FnMetric[]): { blocked: string[]; warned: string[] } {
  const blocked: string[] = [], warned: string[] = [];
  for (const fn of fns) {
    const limit = fn.critical ? 10 : 20;
    // 增量：必须比基线高且超绝对阈值才拦截
    if (fn.complexity > fn.baseline && fn.complexity > limit) {
      (fn.critical ? blocked : warned).push(
        `${fn.name}: ${fn.baseline}→${fn.complexity} (limit ${limit})`,
      );
    }
  }
  return { blocked, warned };
}

console.log(checkComplexityRegressions([
  { name: 'renderList', complexity: 18, baseline: 12, critical: true },  // 阻断
  { name: 'formatDate', complexity: 15, baseline: 14, critical: false }, // 未超20，放过
  { name: 'legacyFn', complexity: 30, baseline: 30, critical: true },    // 无增量，放过
]).blocked.length === 1);
```
