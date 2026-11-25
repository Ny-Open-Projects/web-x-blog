---
title: [WCN-271] TC39 Signals 提案的核心设计与对生态的意义？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-271：TC39 Signals 提案的核心设计与对生态的意义？
**答**：
- 提案定位：语言级原语（Signal/Computed/Effect 三原语 + 统一调度语义），框架实现其上。
- 意义：跨框架信号互操作（React/Vue/Solid 消费同一信号实例），消掉各库绑定层。
- 当前状态：早期阶段，API 语义（push/pull 混合模型）仍在演进。
- 工程动作：自有信号库 API 设计向提案对齐（命名/语义），降低未来迁移成本。

```javascript
// TC39 草案形态
const counter = new Signal.State(0);
const double = new Signal.Computed(() => counter.get() * 2);
new Signal.Effect(() => console.log(double.get()));   // 调度语义由规范统一
r
```
