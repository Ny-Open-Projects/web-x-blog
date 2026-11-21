---
title: [AIC-245] 全量让 AI 生成测试成本高收益低，如何确定哪些模块值得 AI 生成测试？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-245：全量让 AI 生成测试成本高收益低，如何确定哪些模块值得 AI 生成测试？
**答**：
- 按「变更频率 × 业务风险」矩阵：高频变更 + 高风险（支付/价格/权限）优先全覆盖。
- 低变更 + 纯展示类组件：只生成冒烟渲染用例，不做深度用例。
- 用 git log 热点分析 + 事故记录加权，输出优先级清单定期更新。
- 覆盖率投入产出比：当边际覆盖率提升 < 1% 且模块稳定时停止投入。

```javascript
function prioritize(modules: Array<{ path: string; churn: number; risk: number }>) {
  return modules
    .map(m => ({ ...m, score: m.churn * 0.6 + m.risk * 0.4 }))
    .sort((a, b) => b.score - a.score)
    .map((m, i) => ({ ...m, tier: i < 10 ? 'deep' : i < 30 ? 'smoke' : 'skip' }));
}
r
```
