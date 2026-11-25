---
title: [AIC-125] 怎么评估一次「AI 驱动的技术迁移」（如 webpack→rspack）是否值得？ROI 框架是什么？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-125：怎么评估一次「AI 驱动的技术迁移」（如 webpack→rspack）是否值得？ROI 框架是什么？
**答**:
- ROI 框架：收益（构建提速 × 团队规模 × 每天次数、DX 提升）÷ 成本（迁移工时 × AI 折算率、验证工时、回退期风险）+ 持续维护成本变化。
- AI 对公式两端的影响：迁移工时大幅折算（AI 做 codemod 与配置转换），验证工时不变（产物对比、性能回归、灰度发布都是人的活）；「AI 让迁移变便宜」但不等于「迁移值得做」。
- 决策门槛建议：收益/成本比 > 3 才立项，且必须列出「不迁移的代价」——如果现状没痛，迁移就是为技术升级而升级。
- 评估中的 AI 用法：让 AI 估迁移工作量（扫配置复杂度、插件依赖面）、生成迁移风险清单——但估值要人工校准，AI 系统性乐观。
- 追问钩子：迁移评估最能暴露「会不会算账」，把 AI 的作用限制在「降低成本端」而不是「夸大收益端」是成熟判断。

```javascript
// 迁移 ROI 估算（供决策会使用）
function migrationROI({ speedGainSec, devs, buildsPerDay, migrateHours, aiFactor = 0.4, verifyHours }) {
  const dailySavedMin = devs * buildsPerDay * speedGainSec / 60;
  const yearlyGainH = dailySavedMin * 250 / 60;
  const costH = migrateHours * aiFactor + verifyHours;   // AI 只折算迁移工时
  return { ratio: yearlyGainH / costH, verdict: yearlyGainH / costH > 3 ? 'GO' : 'HOLD' };
}
```
