---
title: [RBL-296] Rspack 构建 SSR 双产物（client/server）要点
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-296：Rspack 构建 SSR 双产物（client/server）要点

**答**:
- 双 target 构建：client（web，产出含 runtime 与 CSS 提取）+ server（node，external 全部 node_modules 或全部打包）——external 策略是关键决策（部署形态决定）
- server 产物的特殊处理：动态 import 保持（SSR 流式加载 chunk）、CSS 处理（server 侧忽略或提取给 client）、asset publicPath 注入
- 构建协同：manifest 联动（client 产物清单 → server 渲染时引用正确的 hash 文件名）——SSR 双产物最容易断的就是 manifest 链
- 验证：dev/prod 双模式冒烟 + hydration 一致性（client/server 渲染 diff 必须为零）

```javascript
// server 配置要点
{
  target: 'node',
  output: { filename: 'server.js', libraryTarget: 'commonjs2' },
  externals: [nodeExternals()],       // 或全打包（自包含部署）
  plugins: [new ManifestPlugin({ fileName: 'client-manifest.json' })],
}
```
