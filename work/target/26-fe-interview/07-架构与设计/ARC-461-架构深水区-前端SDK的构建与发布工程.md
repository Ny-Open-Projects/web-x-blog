---
title: [ARC-461] 前端 SDK 的构建与发布工程如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-461：前端 SDK 的构建与发布工程
**答**:
- 双格式产物：ESM（现代打包器）+ UMD（script 直引，第三方宿主），types 完整（dts 生成）；package.json exports 条件导出（import/require/types）。
- 体积纪律：SDK 核心极小（loader < 10KB），重能力按需子包（full/features 子路径）；依赖树审计（不许带 lodash 全量进来——按函数引入或自写）；体积门禁（核心包 gzip 超标阻断发布）。
- 版本发布：changelog 自动化（conventional commits）、pre-release 通道（beta 用户先行）、破坏性变更升级周期承诺（弃用告警两个大版本后移除）。
- 兼容矩阵：目标浏览器集合显式声明（browserslist），发布前跑兼容冒烟（主流 WebView 版本矩阵）。
- 发布验证：npm publish 前发包内容检查（files 白名单、避免把测试/配置发出去）；发布后 canary 验证（内部站点接入 beta 版本真实流量验证）。
```json
{
  "name": "@corp/tracker",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.mjs", "require": "./dist/index.js" },
    "./full": { "import": "./dist/full.mjs" }
  },
  "sideEffects": false,
  "files": ["dist"],
  "scripts": { "prepublishOnly": "npm run build && npm run size-gate && npm run smoke" }
}
```
