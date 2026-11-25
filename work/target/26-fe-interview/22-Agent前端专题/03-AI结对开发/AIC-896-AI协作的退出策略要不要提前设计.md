---
title: [AIC-896] 如果哪天不用这个 AI 工具了，退出策略要不要提前设计？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-896：如果哪天不用这个 AI 工具了，退出策略要不要提前设计？
**答**：
- 要。**供应商锁定（lock-in）是 AI 工具链最容易被忽视的风险**：prompt 存在人家私有格式里、规则文件依赖专有语法、评测数据无法导出、SDK 深度耦合——换工具时成本巨大，被绑架。
- 退出策略核心是**保持可迁移性**：① 关键资产（prompt、规则、评测集、交接文档）用**开放格式**存在自己的仓库里（AIC-836 评测即代码），不锁在供应商平台；② 通过统一 SDK / 适配器层访问（AIC-864），换供应商只换适配器；③ 定期做「迁移演练」——真的尝试换一个工具跑一遍，暴露隐藏耦合。
- knowledge 层面：团队能力不能绑定在「会写某工具的 prompt」上，而是绑定在「会拆解任务、定义质量标准」这些可迁移的技能上。
- 商业层面：合同上要有数据导出条款与通知期；成本模型要算「迁移成本」作为切换决策的一部分。
- 追问钩子：能说出「把 prompt/评测/规则用开放格式放自己仓库 + 通过适配器解耦 + 定期迁移演练」的候选人，具备对抗供应商锁定的前瞻性。

```typescript
type Asset = { name: string; format: 'open' | 'proprietary'; location: 'our-repo' | 'vendor' };

function lockInRisk(assets: Asset[]) {
  const locked = assets.filter(a => a.format === 'proprietary' || a.location === 'vendor');
  return {
    lockedAssets: locked.map(a => a.name),
    riskScore: +(locked.length / (assets.length || 1)).toFixed(2),
    exitPlan: locked.length
      ? ['将专有格式导出为开放格式(Markdown/YAML)',
         '通过统一 SDK 解耦调用',
         '每季度做一次迁移演练']
      : '资产均在自有仓库且为开放格式，退出成本低',
  };
}
console.log(lockInRisk([
  { name:'prompt 模板', format:'open', location:'our-repo' },
  { name:'评测集', format:'proprietary', location:'vendor' }, // 锁定风险
]));
```
