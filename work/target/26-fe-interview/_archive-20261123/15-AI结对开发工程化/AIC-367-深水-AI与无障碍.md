---
title: [AIC-367] AI 产出的组件如何保证无障碍（a11y）质量？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-367：AI 产出的组件如何保证无障碍（a11y）质量？
**答**：
- a11y 规则进 rules：语义化标签优先/交互元素键盘可达/颜色对比度 token 化保证。
- 自动化检查：axe-core 扫描进 CI 门禁，AI 产出不过 a11y 检查不入库。
- AI 自检清单：生成组件时要求输出「a11y 自检表」（role/aria/焦点顺序），评审对照。
- 真实辅助技术验证：关键组件用屏幕阅读器人工验证——自动化工具覆盖不了体验层。

```javascript
const a11yPipeline = {
  rules: '语义标签/键盘可达/对比度 token',
  ci: 'axe-core 扫描 → block 不过',
  selfCheck: 'AI 输出 role/aria/focus 自检表',
  manual: '关键组件屏幕阅读器人验',
};
r
```
