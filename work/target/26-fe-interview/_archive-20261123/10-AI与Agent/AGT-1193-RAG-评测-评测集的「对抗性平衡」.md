---
title: [1193] 评估集里「容易的题」和「刁钻的题」比例怎么定
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 评估集]
type: 面试题
---

## 1193：评估集里「容易的题」和「刁钻的题」比例怎么定

**答**：
- 比例设计原则：模拟真实分布为主（简单题 60%——多数用户问的是常规问题），刁钻题 25%（边界/干扰/多跳，测鲁棒性），对抗题 15%（诱导/注入/超范围，测安全性）——纯简单题的评估集会培养「盲目的自信」。
- 刁钻题的价值在「区分度」：好模型与普通模型的差距全在刁钻题上体现；用「区分度统计」定期审视每道题的贡献（零区分度的题淘汰）。
- 对抗题单独管理：不进质量平均分（会拉低总分误导），单独出「安全红线」报告。
- 追问钩子：刁钻题会不会让优化方向跑偏（为了刁钻题牺牲简单题）？——用「分组红线」防跑偏：简单题组分数不得下降超过 0.01，刁钻题组的提升才允许合并——两边都有护栏。

```ts
const mix = { easy: 0.6, tricky: 0.25, adversarial: 0.15 };
function report(scores) {
  const g = groupBy(scores, 'kind');
  if (g.easy.avg < last.easy.avg - 0.01) return block('简单题回退，优化跑偏'); // 护栏
  return { overall: wAvg(scores, { adversarial: 0 }),   // 对抗题不进质量分
    safety: g.adversarial.avg, tricky: g.tricky.avg };
}
```

