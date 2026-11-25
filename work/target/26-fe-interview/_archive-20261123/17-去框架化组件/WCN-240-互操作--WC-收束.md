---
title: [WCN-240] 框架互操作深水区收束（面试答法）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-240：框架互操作深水区收束（面试答法）。
**答**：
- 四层问题：props 传递（attr/property 协议）、事件（原生事件 + 桥接清理）、样式（CSS 变量 + ::part）、状态（句柄注入而非全局总线）。
- SSR/DSD 是现代主线：声明式 shadow 让「框架无关 + SSR 完整」同时成立。
- 治理面：类型分发/API 稳定性/错误协议/版本协商——互操作是工程问题不只是技术问题。
- 反向判断：单框架低寿命场景不迁，记分卡决策。

```javascript
const interop = {
  layers: ['props(attr/prop 协议)', 'events(原生+清理)', 'styles(var+::part)', 'state(句柄注入)'],
  modern: 'DSD 主线：SSR 完整 + 框架无关',
  governance: ['类型分发', 'API 稳定', '错误协议', '版本协商'],
  anti: '单框架 + 短寿命 → 不迁',
};
r
```
