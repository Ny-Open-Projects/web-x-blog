---
title: [WCN-375] 多团队贡献元素时的质量一致性保障？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-375：多团队贡献元素时的质量一致性保障？
**答**：
- 脚手架：元素模板（含测试/a11y/token/文档骨架）强制起点。
- 评审清单：API 设计/a11y/token 合规/测试覆盖四维强制评审项。
- 自动化拦截：能自动检的进 CI（裸值/清理缺失/axe），人工只看 API 设计。
- 返工率追踪：贡献 PR 一次通过率（低 → 模板/清单改进）。

```javascript
const contribution = {
  scaffold: '元素模板强制起点',
  ci: '自动检（裸值/清理/axe）',
  human: 'API 设计评审（四维清单）',
  metric: '一次通过率',
};
r
```
