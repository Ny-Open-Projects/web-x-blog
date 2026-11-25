---
title: [1024] 怎么把 Agent 安全经验沉淀成团队资产
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 知识沉淀]
type: 面试题
---

## 1024：怎么把 Agent 安全经验沉淀成团队资产

**答**：
- 三类资产：攻击知识库（手法 + 复现步骤 + 当前拦截状态，红队维护）、防御手册（每条防线的设计依据、失效模式、降级预案，蓝队维护）、判例库（历史事故的定界与处置，新人培训素材）。
- 资产要「活」：每个新攻击手法入库时自动生成回归用例；每条防线变更时链接到它防御的手法清单，形成攻防映射矩阵。
- 培训节奏：新人入职必过「注入攻防工作坊」（亲手打一遍自家系统再修）；每季度防线变更宣讲。
- 追问钩子：怎么衡量沉淀有效？——「同类攻击复发率」：知识库覆盖的攻击类别在事故中复发应趋近 0，复发即知识库失效信号。

```ts
// 攻防映射矩阵
const matrix = {
  'indirect_injection': { defenses: ['sanitize', 'trust_tier', 'tool_isolation'],
    cases: 14, lastBypass: '2026-09' },
  'jailbreak_roleplay': { defenses: ['input_classifier', 'session_risk'],
    cases: 9, lastBypass: null },
};
async function addAttack(attack) {          // 新手法入库即生成回归用例
  await kb.add(attack);
  await evalStore.add(toRegressionCase(attack));   // 资产「活」起来
}
```
