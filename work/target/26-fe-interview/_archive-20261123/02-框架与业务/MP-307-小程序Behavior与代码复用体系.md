---
title: [MP-307] 小程序 Behavior：代码复用与组合规则
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-307：小程序 Behavior：代码复用与组合规则

**答**：
- Behavior 是组件的 mixin：data/methods/lifecycleHooks 的复用单元——与 Vue mixin 语义相似（同样有隐式来源问题）
- 合并规则：data 浅合并（同名组件覆盖 behavior）、methods 覆盖、生命周期都执行（behavior 先、组件后）；多 behavior 按声明顺序
- 组合治理：behavior 命名空间化（data 字段带前缀）、纯功能 behavior（日志/曝光埋点）优先——「可预测合并」的规范
- 与全局状态的关系：跨页面复用不放 behavior（放 utils/store）——behavior 只解决「组件级」复用
- 深水点：behavior 的生命周期依赖（attached 里用 this._init 由 behavior 提供）——隐式契约要文档化，否则组合顺序变化就崩

```javascript
// 纯功能 behavior: 曝光埋点
const exposureBehavior = Behavior({
  lifetimes: {
    attached() { this._expId = crypto.randomUUID?.() ?? `${Date.now()}`; },
    ready() { this.createIntersectionObserver().relativeToViewport().observe('.exp', () => track('expose', { id: this._expId })); },
    detached() { this._io?.disconnect(); },
  },
});
Component({ behaviors: [exposureBehavior] });   // 组合即获得曝光能力
```
