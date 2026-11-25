---
title: [ARC-208] 联邦与 qiankun 微前端的选型边界在哪？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-208：联邦与 qiankun 微前端的选型边界在哪？
**答**：
- 粒度不同：联邦是**模块级**共享（共享一个组件/工具函数），qiankun 是**应用级**集成（整个子应用带路由带生命周期）。
- 选联邦：团队技术栈统一、追求依赖共享与细粒度复用、需要 SSR、应用间是"组件市场"关系。选 qiankun：技术栈异构（jQuery 老系统 + React 新系统）、需要完全独立运行时与样式隔离、子应用有独立路由体系。
- 混用范式：外壳用 qiankun 集成异构遗留系统，壳内同栈新应用之间用联邦共享组件与依赖——两层各管一段。
- 共同代价都要评估：公共依赖治理（externals/共享协商）、联调复杂度、发布编排。没有"零成本微前端"。

```javascript
// 混用示意：qiankun 壳 + 联邦内部共享
registerMicroApps([
  { name: 'legacy-order', entry: '//legacy.example.com', container: '#sub', activeRule: '/order' }, // 老系统：qiankun
  { name: 'new-cart',     entry: '//cart.example.com',   container: '#sub', activeRule: '/cart' },   // 新系统：内部再用联邦
]);
// new-cart 与 new-pay 之间共享组件走联邦：
// cart 的 Header 不自己实现，而是 loadRemote('pay-shared/OrderHeader')
// 决策口诀：换不换技术栈？换→应用级（qiankun）；同栈只想复用代码→模块级（联邦）
```
