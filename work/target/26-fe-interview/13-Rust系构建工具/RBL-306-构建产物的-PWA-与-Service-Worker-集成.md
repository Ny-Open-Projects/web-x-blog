---
title: [RBL-306] 构建产物与 PWA/Service Worker 的集成
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-306：构建产物与 PWA/Service Worker 的集成

**答**:
- Workbox 集成：构建期生成 precache manifest（全部产物 hash 清单）→ SW 精确预缓存；runtime 缓存路由（API networkFirst/静态 cacheFirst）
- 关键机制：SW 文件本身不缓存（每次浏览器检查更新）、版本变更触发 skipWaiting+clientsClaim（可控更新策略：提示用户刷新而非静默）
- 构建产物约束：precache 体积预算（离线全量缓存要控制清单）、sw 与产物同发布（hash 清单同步生成）
- 调试与验证：SW 更新流程端到端测试（老版本→新版本→刷新生效）；注意 SW 缓存导致的「发版后用户看到旧页面」类事故

```javascript
// vite/rspack PWA 插件配置要点
new WorkboxPlugin.GenerateSW({
  precacheManifest: manifest,   // 构建产物清单
  clientsClaim: true, skipWaiting: true,   // 或提示式更新
  runtimeCaching: [{ urlPattern: /\/api/, handler: 'NetworkFirst' }],
})
```
