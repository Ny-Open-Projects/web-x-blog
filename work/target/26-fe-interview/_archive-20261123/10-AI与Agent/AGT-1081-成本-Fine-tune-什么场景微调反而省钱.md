---
title: [1081] 微调（fine-tune）在什么情况下是省钱的
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 成本延迟, 微调]
type: 面试题
---

## 1081：微调（fine-tune）在什么情况下是省钱的

**答**：
- 微调省钱场景：高度重复的窄任务（固定格式抽取/分类）——微调小模型替代旗舰 prompt，单位成本降 10 倍以上；长系统指令（每请求 2k 的规则 prompt 微调「烧进」权重）——省掉的 prompt token 长期摊薄微调成本。
- 微调不省钱场景：知识频繁更新（重训成本高于检索注入）、通用能力任务（旗舰模型底座不可替代）、数据量不足（少于 1000 条效果难保障）。
- 决策公式：微调成本（训练 + 维护 + 重训周期）< 节省的推理差价 × 预计用量；用量是关键变量，低频任务永远别微调。
- 追问钩子：微调会不会带来安全回退？——会，微调后拒答能力可能弱化，微调数据里要掺安全样本，且微调版必须重跑安全回归集。

```ts
function ftDecision({ task, volume, ftCost, inferCostBig, inferCostSmall }) {
  const save = volume * (inferCostBig - inferCostSmall);   // 年推理节省
  return save > ftCost * 1.5        // 1.5 倍安全边际（含重训）
    ? { verdict: 'fine-tune', model: 'small', data: task.samples }
    : { verdict: 'keep-prompting' };
}
```

