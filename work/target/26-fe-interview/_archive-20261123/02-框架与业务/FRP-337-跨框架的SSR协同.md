---
title: [FRP-337] 跨框架的 SSR 协同
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## FRP-337：跨框架的 SSR 协同

**答**：
- 场景：一个页面多框架 SSR（主框架页面嵌子框架 island）——每框架各自 renderToString 后拼 HTML
- 拼接顺序与数据：island 的数据获取在「服务端执行」（框架各自）——拼装层（Node 中间层）编排「主框架渲染 + island 渲染」的并行
- 水合独立性：各 island 独立 hydrate（各自框架的 hydrateRoot/createSSRApp）——互不阻塞，TTI 按岛分摊
- 资源协议：island 产出的 JS/CSS 清单由拼装层聚合进 HTML（避免重复加载框架 runtime——共享 externals）
- 深水点：island 间通信（服务端拼好的页面里两框架交互）——与客户端微前端同一套总线协议（CustomEvent + 内核 store）

```javascript
// Node 拼装层
const [mainHtml, islandHtml, islandManifest] = await Promise.all([
  renderMainApp(url),
  renderVueIsland({ props }),           // 各框架各自 SSR
  manifestPromise,
]);
const html = injectIsland(mainHtml, islandHtml, islandManifest);  // 替换占位 + 聚合资源
// 客户端: 各 island 独立 hydrate
```
