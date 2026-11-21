---
title: [BLD-068] 联邦、iframe、qiankun（微前端框架）如何选型？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-068：联邦、iframe、qiankun（微前端框架）如何选型？
**答**：
- iframe：最强隔离（JS/CSS/存储全隔离），但 URL 不同步、弹层跨壳、通信 postMessage 繁琐、性能开销大；适合强异构（跨团队技术栈、不可信脚本、第三方插件）。
- qiankun：基于 single-spa + importHTML，HTML 入口、JS 沙箱（Proxy 劫持 window）与样式隔离方案较完整；适合"多团队整站改造"、子应用技术栈杂、需要沙箱兜底的场景；子应用需做生命周期改造。
- MF：模块级集成粒度最细（可共享组件/工具而非整应用）、体验原生、依赖协商自动；但无沙箱、shared 契约要求高、SSR 弱。
- 决策线：要"共享模块"选 MF；要"应用沙箱"选 qiankun；要"完全隔离/外部系统"选 iframe；三者可组合（MF 共享底层、qiankun 沙箱壳）。

```javascript
// text 代码块：选型决策对照表
// 维度              iframe            qiankun             Module Federation
// 集成粒度          整应用             整应用               模块/组件级
// JS 隔离           完全              Proxy 沙箱           无（需约定）
// CSS 隔离          完全              实验性 scoped/前缀    无（需 CSS Modules/前缀）
// 独立部署          支持              支持                 支持（remoteEntry 契约）
// 依赖去重          不共享            可 external          shared 运行时协商
// 通信              postMessage       props/globalState    模块导入/Context
// SSR               无               有限                 有限（同进程方案）
// 典型场景          第三方嵌入         大型中台整站          云产品组合 + 设计系统复用
```

## 第十章 其他工具与对比（BLD-069 ~ BLD-100）
