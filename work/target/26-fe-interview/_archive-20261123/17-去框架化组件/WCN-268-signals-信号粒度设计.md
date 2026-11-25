---
title: [WCN-268] 信号粒度设计原则（一个字段一个信号 vs 大对象信号）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-268：信号粒度设计原则（一个字段一个信号 vs 大对象信号）？
**答**：
- 细粒度：更新精确、订阅精确——但节点数多（内存/图遍历成本）。
- 粗粒度：节点少——但无关字段写入触发下游（需要 equal 精细化弥补）。
- 经验：热路径（高频更新）细粒度，冷数据（低频配置）粗粒度。
- 对象字段的中间态：deep-signal（代理嵌套字段各自成节点）自动细化。

```javascript
// deep-signal：嵌套对象自动细粒化
const s = deepSignal({ user: { name: 'x', age: 1 } });
effect(() => renderName(s.user.name));   // age 变化不影响此 effect
r
```
