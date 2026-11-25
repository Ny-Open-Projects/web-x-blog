---
title: [AIC-824] 「幻觉率」怎么量化？能给它定一个 SLO 吗？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-824：「幻觉率」怎么量化？能给它定一个 SLO 吗？
**答**：
- 幻觉定义要先收敛：分**事实性幻觉**（编造不存在的事实/API）和**忠实性幻觉**（不遵循给定上下文，答非所问）。两种检测方式不同：前者靠外部知识源核验，后者靠「答案是否可由上下文蕴含」（可用 NLI 模型）。
- 量化：在 golden 集上标注「是否含幻觉」，计算 `幻觉率 = 含幻觉答案数 / 总答案数`，并给置信区间（二项分布 Wilson 区间）；样本太少时区间很宽，不能据此下结论。
- SLO 可以定但要分层：高风险场景（涉及金额、法律、医疗）幻觉率目标应接近 0，普通场景可接受>2%；同时要配套「幻觉发生时的影响度」（是否导致错误操作），单纯看率不够。
- 工程手段降低幻觉：RAG 提供证据、要求引用来源、low temperature、工具校验、拒答机制（不确定时说不知道）。**拒答率要一起看**——幻觉率下降但拒答率飙升，用户体验反而变差。
- 追问钩子：能说出「幻觉率和拒答率要联合评估，否则模型学会'什么都不说'来刷指标」的候选人，理解了指标博弈的本质。

```typescript
// Wilson 置信区间：小样本下比正态近似更稳健
function wilson(successes: number, n: number, z = 1.96) {
  if (!n) return [0, 0];
  const p = successes / n;
  const d = 1 + z * z / n;
  const center = (p + z * z / (2 * n)) / d;
  const margin = z * Math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d;
  return [center - margin, center + margin];
}

function hallucinationReport(hallucinated: number, refused: number, total: number) {
  const rate = total ? hallucinated / total : 0;
  const [lo, hi] = wilson(hallucinated, total);
  return {
    rate: +rate.toFixed(3),
    ci95: [+lo.toFixed(3), +hi.toFixed(3)],
    refusalRate: total ? +(refused / total).toFixed(3) : 0,
    verdict: hi < 0.02 ? 'pass' : 'needs work',
  };
}
console.log(hallucinationReport(3, 5, 100)); // { rate:0.03, ci95:[...], refusalRate:0.05, verdict:'needs work' }
```
