---
title: [AIC-887] 明天要上线，AI 能帮我赶工，但质量门禁过不了，怎么权衡？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-887：明天要上线，AI 能帮我赶工，但质量门禁过不了，怎么权衡？
**答**：
- 先区分门禁级别：**硬红线（Block，如密钥泄露、安全漏洞）不能破**——这是"上线后可能出大事"的底线，没有权衡空间；可降级的是 Warn 级建议（AIC-828）。把「赶工」当成突破红线的理由是典型的风险错配。
- 真正的权衡是**缩小范围而非降低标准**：砍掉非核心功能、把 AI 快速生成的代码限制在低风险模块（展示层而非支付），核心路径手工精做并充分 review——「少做一点但做对」。
- 用**分层发布**争取时间：先上最小可用版本并加开关（feature flag），灰度放量；把 AI 生成部分放后面批次，用影子流量和监控兜底。这样既赶了进度又留了回滚余地。
- 记录**技术债**并设偿还日期：临时方案必须登记 owner 与到期日，否则「赶工」会变成永久烂摊子；下次迭代优先还债。
- 追问钩子：能说出「红线不能破，靠缩小范围和分层发布争取时间，而不是降标准」的候选人，在压力下守住了工程底线。

```typescript
type Item = { name: string; risk: 'low'|'high'; aiGenerated: boolean; mustShip: boolean };

function rushPlan(items: Item[]) {
  const core = items.filter(i => i.mustShip);
  const highRiskAI = core.filter(i => i.risk === 'high' && i.aiGenerated);
  return {
    shipNow: core.filter(i => !(i.risk === 'high' && i.aiGenerated)), // 高风险 AI 代码不上
    defer: highRiskAI.map(i => ({ item:i.name, reason:'高风险 AI 代码需人工精做',
      strategy:'feature flag 关闭 + 下批次灰度' })),
    hardLines: ['安全漏洞','密钥泄露','许可证违规'], // 永不可破
    debt: highRiskAI.length ? { owner:'TBD', due:'next-sprint', registered:true } : null,
  };
}
console.log(rushPlan([
  { name:'营销 banner', risk:'low', aiGenerated:true, mustShip:true },
  { name:'支付计算', risk:'high', aiGenerated:true, mustShip:true },
])); // 支付计算延期，banner 可上
```
