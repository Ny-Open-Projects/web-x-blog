---
title: [WCN-256] 编译器如何把响应式表达式编译成「信号绑定」？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-256：编译器如何把响应式表达式编译成「信号绑定」？
**答**：
- 编译期分析 JSX/模板中哪些表达式读信号 → 生成对应订阅代码（Vue Vapor/Solid 风格）。
- 静态提升：不含信号的表达式编译为常量（不参与更新）。
- 表达式边界：解构/展开/方法调用等「追踪黑名单」编译期告警（可能丢响应性）。
- 产物形态：createEffect(() => node.prop = expr) 的定向更新。

```javascript
// 输入
<div class={cls()}>{name()}</div>
// 编译产物（Vue Vapor 风格）
const n0 = t0();
bk(n0, () => cls(n0));                  // bind class
createEffect(() => setElementText(n0, name()));  // 静态部分不编译进 effect
r
```
