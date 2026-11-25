---
title: [1126] Agent 链路做的决策怎么生成「人类能看懂」的解释
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 可解释]
type: 面试题
---

## 1126：Agent 链路做的决策怎么生成「人类能看懂」的解释

**答**：
- 解释与 trace 分离：trace 是工程视图（span/消息），解释是叙事视图（「为什么推荐 A 而不是 B」）——从 trace 的关键节点抽取「决策点 + 备选 + 依据」生成叙事。
- 决策点显式化：编排器在关键分叉（路由选择、降级触发、排序取舍）埋「decision 记录」（选项、依据字段、得分），解释器只组装不猜测——事后从 trace 反推的解释容易编故事。
- 分层解释：一句话结论（给用户）、依据列表（给审核人）、完整 trace（给工程师），按受众取层级。
- 追问钩子：解释会不会「事后合理化」？——会，如果解释是模型事后生成的自由文本。对策：决策依据在决策时刻结构化记录，解释只是格式化引用，不做二次创作。

```ts
// 决策时刻记录（不做二次创作）
trace.decision({ point: 'rank_a_vs_b', options: ['A', 'B'],
  scores: { A: 0.82, B: 0.71 }, basis: ['用户偏好字段', '历史通过率'] });
// 解释器：格式化引用
function explain(decisions, level = 'user') {
  const d = decisions.find(x => x.point === 'rank_a_vs_b');
  return level === 'user' ? '推荐 ' + d.options[0] + '，因为与您的偏好匹配度更高。'
    : d;   // 审核人看结构化依据
}
```

