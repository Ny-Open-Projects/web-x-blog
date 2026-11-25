---
title: [TST-575] AI 驱动的探索性测试如何落地
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-575：AI 驱动的探索性测试如何落地

**答**：
- 结论：AI 作为「探索伙伴」——基于页面结构/接口文档建议探索路径、生成变异操作序列、把探索中发现的问题结构化记录，而非替代人的直觉。
- 做法：给 AI 应用状态与历史探索轨迹，让它建议「还没覆盖的操作组合」；探索中自动记录步骤与截图；发现后用 AI 辅助复现步骤整理成回归用例。
- 追问钩子：探索性测试强调人的直觉，AI 会不会限制创造力？——把 AI 当「候选建议生成器」而非指令，人可忽略；AI 负责广度，人负责深度与洞察。

```javascript
// 探索建议：基于已覆盖组合，推荐未探索的操作对
function suggestExplore(actions, coveredPairs) {
  const suggestions = [];
  for (let i = 0; i < actions.length; i++) for (let j = 0; j < actions.length; j++) {
    if (i === j) continue;
    const key = `${actions[i]}>${actions[j]}`;
    if (!coveredPairs.has(key)) suggestions.push(key);
  }
  return suggestions.slice(0, 8); // 优先返回少量高价值建议
}
```
