---
title: [AIC-215] 为规则体系建一套评测集，应该包含哪些类型的用例？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-215：为规则体系建一套评测集，应该包含哪些类型的用例？
**答**：
- 正例：应一次通过的典型任务（黄金路径），验证规则不误伤。
- 反例：历史违规任务原样保留，验证规则能纠正（核心回归集）。
- 边界例：规则之间的冲突场景、glob 重叠文件，验证优先级正确。
- 每条用例带「期望行为清单」，判定可执行（类型/测试/lint）+ 关键特征断言。

```javascript
const evalSet = [
  { id: 'E-001', type: 'negative', task: '给商品卡加个红色边框', // 诱导硬编码颜色
    expect: ['使用 color.border.accent token', '无 #hex 字面量'] },
  { id: 'E-002', type: 'conflict', task: '在 legacy 目录新增临时页面',
    expect: ['legacy 例外规则生效', '不套用新版规范'] },
];
r
```
