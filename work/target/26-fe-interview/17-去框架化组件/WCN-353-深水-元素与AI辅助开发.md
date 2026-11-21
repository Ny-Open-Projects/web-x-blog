---
title: [WCN-353] AI 辅助元素开发（生成/审查/迁移）的落点？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-353：AI 辅助元素开发（生成/审查/迁移）的落点？
**答**：
- 生成：按 API 规范生成元素骨架（含 a11y/测试骨架）——规范即提示词。
- 审查：AI 检查元素代码违规（裸值/innerHTML/缺清理）——模式库驱动。
- 迁移：框架组件 → WC 的机械转换 AI 辅助（人审语义差异）。
- 评测：AI 产出过同一门禁（行为/a11y/视觉测试全绿才收）。

```javascript
// AI 审查规则集（提示词注入）
const rules = ['禁裸值样式', 'innerHTML 必须转义', 'disconnected 必须清理',
  '事件必须 detail 类型化', 'a11y：role/aria 齐全'];
r
```
