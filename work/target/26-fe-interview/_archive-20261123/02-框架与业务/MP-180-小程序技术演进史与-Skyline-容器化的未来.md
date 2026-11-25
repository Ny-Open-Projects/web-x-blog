---
title: [MP-180] 小程序技术演进史与 Skyline/容器化的未来怎么看？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-180：小程序技术演进史与 Skyline/容器化的未来怎么看？
**答**：
- 演进主线：2017 微信上线（双线程 + WebView 渲染）→ 分包/插件/云开发补工程能力 → 同层渲染解决原生组件覆盖问题 → **Skyline 渲染引擎**（去 WebView：渲染在 native，逻辑与渲染同线程通信更近，支持 worklet 动画）→ 跨端框架生态繁荣。
- Skyline 关键变化：不再每个页面一个 WebView，`setData` 跨线程损耗降低；CSS 子集受限（部分选择器/布局能力差异），需按适配清单开发。
- 容器化趋势：小程序运行时作为标准容器被集成进 App（FinClip/uni 小程序 SDK），"小程序"从微信专属能力变成**通用 hybrid 形态**。
- 面试表达：演进的本质是"管控与性能的再平衡"，回答时按时间线 + 每阶段解决的问题展开。

```json
{
  "__app.json__ Skyline 适配声明",
  "rendererOptions": { "skyline": { "defaultDisplayBlock": true, "disableABTest": false } },
  "lazyCodeLoading": "requiredComponents",
  "__page.json__ 页面级开启",
  "renderer": "skyline",
  "componentFramework": "glass-easel",
  "navigationStyle": "custom",
  "__note__ Skyline 不支持 navigationBar 默认导航，需自定义导航栏"
}
```
