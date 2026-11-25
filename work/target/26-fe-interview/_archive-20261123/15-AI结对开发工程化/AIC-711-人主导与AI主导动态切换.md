---
title: [AIC-711] 结对中人主导与 AI 主导动态切换的信号与时机如何把握
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-711：结对中人主导与 AI 主导动态切换的信号与时机如何把握

**答**：
- 结论先行：主导权不是固定的，而是随任务阶段动态切换——「探索/样板」阶段 AI 主导提效，「关键决策/安全/陌生领域」阶段人主导把控，判断依据是「错误代价 × AI 确定性」。
- 切换信号：1) 低风险高重复（样板、转换）→ 交给 AI；2) 涉及架构/资金/安全 → 收回人主导；3) AI 连续两次给出同类错误 → 立即收回并重构 prompt。
- 交接动作：切换时显式说明「现在由我主导，你只做 X」，避免 AI 继续越权生成。
- 追问钩子：为什么「AI 连续两次同类错误」是强切换信号？——说明当前上下文/prompt 已无法约束该模型，继续投入只会放大错误（RBL-509 迭代收敛失效）。

```javascript
// 主导权决策：错误代价 × 任务确定性
function decideLead(task) {
  const { risk, repeat, aiConfidence } = task; // risk: high/low, repeat: 是否重复, confidence: 0-1
  if (risk === 'high' || aiConfidence < 0.5) return 'human';
  if (repeat && aiConfidence >= 0.8) return 'ai';
  return 'pair'; // 人定方向，AI 出草案
}
console.log(decideLead({ risk: 'low', repeat: true, aiConfidence: 0.9 }));  // ai
console.log(decideLead({ risk: 'high', repeat: true, aiConfidence: 0.9 })); // human（安全红线优先）
console.log(decideLead({ risk: 'low', repeat: false, aiConfidence: 0.6 })); // pair
```
