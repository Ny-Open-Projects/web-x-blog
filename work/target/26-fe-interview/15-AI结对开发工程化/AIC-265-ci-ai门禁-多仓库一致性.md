---
title: [AIC-265] 20 个仓库都要上 AI 门禁，如何统一管理而不用每仓重复配置？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-265：20 个仓库都要上 AI 门禁，如何统一管理而不用每仓重复配置？
**答**：
- 配置中心化：门禁策略/提示词/白名单集中在一个 meta 仓库，版本化发布到各仓（引用版本号）。
- 仓库分级策略：核心仓严格档、边缘仓基础档，按仓库标签自动套配置。
- 例外申报：仓库特殊需求通过 PR 改中央配置，评审留痕——禁止本地私改。
- 效果对比：跨仓采纳率/误报率横向对比，落后仓库定向辅导。

```javascript
const centralConfig = {
  source: 'meta-repo/gate-policy@v3',
  apply: '各仓 gate.yml 引用版本号，CI 校验过期即警告',
  tiers: { core: 'strict', edge: 'basic' },
  override: '只允许 PR 到中央仓库，禁止本地私改',
};
r
```
