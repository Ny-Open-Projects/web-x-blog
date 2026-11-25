---
title: [BLD-240] 产物 manifest 的设计与消费怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-240：manifest 怎么设计？
**答**：
- manifest 内容：入口 → hash 文件映射、chunk 依赖图、预加载清单、资源类型标注（js/css/font/image）、buildinfo 关联——SSR 注入/Service Worker precache/监控还原的共同数据源。
- 设计原则：bundler 无关 schema（SCN-ENG-268 契约）、稳定字段语义（entry/assets/chunks 三区）、版本内嵌（schemaVersion）。
- 消费场景：SSR 的资源注入（HTML 渲染时引用正确 hash）、SW precache 清单、灰度入口切换（SCN-OPS-218）、产物 diff（SCN-ENG-290）。
- 追问钩子：为什么 manifest 要「bundler 无关」——SSR/SW/监控等消费方不应该感知 vite/webpack 的 manifest 格式差异；统一 schema 后换打包器只换生成器，消费方零改动——这是产物契约抽象（SCN-ENG-268）在 manifest 层的直接应用。

```javascript
// 统一 manifest schema
{ schemaVersion: 2,
  entry: { main: 'index-abc123.js' },
  chunks: { 'route-home': { file: 'home-def456.js', imports: ['vendor-react'], css: ['home.css'] } },
  assets: { 'logo': { file: 'logo-789.webp', type: 'image' } },
  build: { commit: 'abc', builtAt: 0 } }
// 消费：SSR 注入
assetsFor(route) → manifest.chunks[route] → <script src>...
```
