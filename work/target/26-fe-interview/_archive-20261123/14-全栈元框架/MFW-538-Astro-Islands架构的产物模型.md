---
title: [MFW-538] Astro Islands 架构：静态主体与交互岛屿的产物模型
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-538：Astro Islands：静态主体与交互岛屿

**答**:
- Islands 产物模型：页面默认纯静态 HTML（零 JS）——交互组件是「岛」（`<Counter client:load />` 指令：load/idle/visible/media——岛屿加载时机声明 RBL-957）；框架无关（岛可 React/Vue/Svelte 各自 runtime—— island 级框架隔离）。
- 指令的产物语义：client:load（水合立即）/client:idle（空闲）/client:visible（视口内才加载——IntersectionObserver）/client:media（媒体查询匹配）——「水合时机」是岛的核心配置（RBL-947 预取降级链的加载时机版）。
- 与 RSC 的对比：RSC 静态部分也是 server 渲染（服务端计算）；Astro 静态部分是构建期纯 HTML（无 server 依赖——内容站极致）；「服务端渲染的静态 vs 构建期渲染的静态」：前者可动态数据、后者零运行时。
- 岛间通信：无共享 runtime——通过 DOM 事件/URL/全局 store（nanostores）——岛是「微前端粒度的组件化」（RBL-766 隔离哲学的组件版）。
- 追问钩子：为什么 Islands 的「框架无关」在工程上是双刃剑？——多框架 = 多 runtime 常驻（React+Vue 各 40KB——岛多时 runtime 累加爆炸）；「每岛独立」换来的是渐进迁移自由（老 Vue 页面加 React 岛）；N 岛 M 框架的体积矩阵是架构约束：岛少用混搭、岛多收敛单框架——「隔离粒度 × runtime 成本」的权衡与微前端完全同构。

```astro
---
// 静态主体：构建期纯 HTML
const products = await fetch('/api/products').then(r => r.json());   // 构建期 fetch
---
<html>
  <body>
    {products.map(p => <div>{p.name}</div>)}            {/* 零 JS */}
    <Counter client:visible {count={0}} />              {/* 岛：视口内才水合 */}
    <Search client:idle />                              {/* 空闲时 */}
    <Carousel client:media="(min-width: 768px)" />      {/* 桌面才需要 */}
  </body>
</html>
<!-- 岛的水合协议：astro-island 自定义元素包裹 + 指令参数编码 -->
<!-- 客户端 runtime 按指令时机唤醒对应框架 -->
```
