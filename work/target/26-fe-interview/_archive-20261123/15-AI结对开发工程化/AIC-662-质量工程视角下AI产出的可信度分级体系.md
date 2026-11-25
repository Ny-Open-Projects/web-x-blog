---
title: [AIC-662] 怎么给 AI 产出做「可信度分级」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-662：怎么给 AI 产出做「可信度分级」？

**答**：
- 结论先行：**不是所有 AI 代码都值得同等审查——按「风险 × 验证充分度」分级，低风险走快速通道，高风险强制严格审查**（AIC-254 PR 风险分级 / AIC-380 许可度）。
- 分级维度：1) **变更风险**：改的是核心支付/权限 = 高，改展示文案 = 低；2) **AI 置信度信号**：校准后置信度（AIC-641）、测试通过率、是否为幻觉高发区；3) **验证充分度**：有无测试覆盖、是否经过交叉审查、变异分数是否达标。
- 四级示例：1) **L0 免审**：纯文案/格式变更 + 格式化工具验证通过；2) **L1 快审**：常规功能 + 测试全绿，单人快速扫；3) **L2 严审**：核心模块或高风险，强制双人 review + 交叉模型审查；4) **L3 禁入**：AI 在安全/加密/资金结算等关键领域的产出，必须人重写或逐行验证。
- 动态调整：某模型/某任务类型近期缺陷率高，其产出自动降一级——分级不是静态标签，随质量信号浮动。
- 追问钩子：为什么「统一审查强度」是浪费？——因为 AI 产出的风险分布极不均匀，80% 是低风险样板代码、20% 是高风险逻辑；对全部一视同仁地严审，会把审查精力耗在低风险代码上，真正危险的 20% 反而得不到足够关注——分级是把有限审查资源投到刀刃上。

```typescript
type Output = { risk: 'high'|'medium'|'low'; testPass: boolean; crossReviewed: boolean; domain: string };

function trustLevel(o: Output): 'L0'|'L1'|'L2'|'L3' {
  if (['payment', 'crypto', 'permission'].includes(o.domain)) return 'L3';
  if (o.risk === 'high' || !o.testPass) return 'L2';
  if (o.risk === 'medium' || !o.crossReviewed) return 'L1';
  return 'L0';
}

console.log(trustLevel({ risk: 'low', testPass: true, crossReviewed: true, domain: 'display' })); // L0
console.log(trustLevel({ risk: 'high', testPass: true, crossReviewed: true, domain: 'list' }));    // L2
console.log(trustLevel({ risk: 'low', testPass: true, crossReviewed: true, domain: 'payment' })); // L3
```
