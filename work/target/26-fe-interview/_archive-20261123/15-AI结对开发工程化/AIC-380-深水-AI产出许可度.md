---
title: [AIC-380] 不同模块给 AI 的「自由度」应该不同，如何设计分级许可体系？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-380：不同模块给 AI 的「自由度」应该不同，如何设计分级许可体系？
**答**：
- 分级维度：业务关键度 × 变更可逆性 × 测试覆盖度——三级：自由生成/生成需人审逐行/仅建议。
- 许可矩阵落配置：目录级声明（src/core → 仅建议；src/pages → 自由生成+门禁）。
- 动态调整：模块出过 AI 相关事故 → 降级许可度；连续 3 个月零事故且门禁健全 → 可申请升级。
- 许可与流程联动：自由级自动合入，人审级强制双人，建议级 AI 出 patch 人手改。

```javascript
const permission = {
  matrix: { 'src/core/**': 'suggest-only', 'src/pages/**': 'auto+gate',
            'src/components/**': 'human-review' },
  dynamic: '事故 → 降级；3 月零事故 → 可申请升级',
  flow: '自由=自动合入 / 人审=双人 / 建议=人手改',
};
r
```
