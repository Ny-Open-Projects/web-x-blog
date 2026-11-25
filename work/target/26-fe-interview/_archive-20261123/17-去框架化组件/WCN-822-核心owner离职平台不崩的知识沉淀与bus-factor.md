---
title: [WCN-822] 核心 owner 离职如何保证平台不崩？（Bus Factor 与知识沉淀）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-822：核心 owner 离职如何保证平台不崩？（Bus Factor 与知识沉淀）

**答**：
- 结论先行：Bus Factor=1（某个模块只有一个人懂）是平台最大的隐性风险——治理目标是把关键模块的知识复制到至少 2~3 人，并把「隐性知识」转成「可查文档与可跑自动化」。
- 衡量：统计每个组件/子系统的 owner 数与「只有一人能改」的模块占比；对高价值模块要求主备 owner 结对。
- 知识显性化：关键决策写 ADR、架构与边界写设计文档、常见排障写 runbook；文档与代码同源（类型→文档→demo→测试）降低腐烂概率。
- 结对与轮值：核心模块强制 code review 双人、on-call 轮值、定期「反向讲解」由备 owner 主讲、主 owner 纠错，逼出知识转移。
- 自动化兜底：把「只有老员工知道的规则」（如发布检查、灰度步骤）固化进 CI 与脚本，减少对人脑记忆的依赖。
- 追问钩子：面试官会问「来不及交接人就走了怎么办」——答：靠平时沉淀的 runbook + ADR + 自动化预案应急，同时临时冻结该模块的破坏性变更，争取交接窗口。

```javascript
// Bus Factor 审计：找出单点依赖模块
const modules = [
  { name: 'token-pipeline', owners: ['Alice', 'Bob'] },
  { name: 'ds-table',       owners: ['Alice'] },
  { name: 'ssr-renderer',   owners: ['Carol'] },
];
function busAudit(mods) {
  return mods.filter(m => m.owners.length < 2)
             .map(m => `${m.name}: 仅 ${m.owners.join(',')}（单点风险）`);
}
console.log(busAudit(modules));
// 治理建议：为 ds-table / ssr-renderer 指定 backup owner
```
