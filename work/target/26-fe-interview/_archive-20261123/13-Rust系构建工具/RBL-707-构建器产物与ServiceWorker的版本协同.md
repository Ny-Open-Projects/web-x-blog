---
title: [RBL-707] 构建器与 Service Worker 的版本协同：预缓存清单与更新语义
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-707：构建器与 Service Worker 的版本协同：预缓存清单与更新语义

**答**:
- SW 预缓存（precache）：SW 安装时把「本版本全部产物」下载缓存——构建器是唯一知道「全部产物清单」的角色，sw-precache 式清单（文件名+revision hash）由构建器生成注入 SW；清单本身是 SW 的版本指纹（内容变 → SW 更新）。
- 更新的坑与构建器的解法：1) **清单里含 sw.js 自己** → SW 更新循环（每次构建 SW 变 → 重新下载 SW 变化 → 死循环）；构建器生成清单时必须排除 sw.js 与其 sourcemap；2) hash 产物的 revision 用文件名 hash（同名即同内容）；3) 导航预加载与运行时缓存的边界（预缓存管本版本、runtime cache 管跨版本）。
- 增量发布的体积问题：每版本全量预缓存（10MB 应用 = 每次更新下载 10MB）——优化是「差异预缓存」（新清单对比旧清单，只下载变化的文件）；构建器输出「新旧清单 diff」给 SW 运行时。
- SW 更新时序：新 SW 安装完成 → waiting（旧 SW 控制页面）→ 需要用户刷新或 skipWaiting；构建器能做的是「新版本通知」语义（清单版本暴露给页面，页面提示刷新）——版本切换的用户体验设计。
- 追问钩子：为什么预缓存清单必须排除 sw.js？——SW 用清单做「缓存内容是否变化」的判定，若清单包含 sw.js 的内容 hash，SW 文件自身变化导致 hash 变 → 每次发布 SW 都「更新」→ 所有用户重新下载全部缓存；这既是浪费也是更新抖动。

```javascript
// 构建器生成 SW 预缓存清单
function generateSWManifest(manifest) {
  const precache = manifest.files
    .filter(f => f.role !== 'service-worker' && !f.name.endsWith('.map'))
    .map(f => ({ url: `/${f.name}`, revision: f.hash ?? sha(f.content) }));
  return precache;
}
// workbox 注入
const swCode = `precacheAndRoute(${JSON.stringify(generateSWManifest(manifest))});`;

// SW 侧差异更新（新旧清单 diff）
async function precacheDiff(oldManifest, newManifest) {
  const oldUrls = new Map(oldManifest.map(e => [e.url, e.revision]));
  const toAdd = newManifest.filter(e => oldUrls.get(e.url) !== e.revision);
  const toRemove = [...oldUrls.keys()].filter(u =>
    !newManifest.some(e => e.url === u));
  for (const e of toAdd) await cache.add(new Request(e.url));
  for (const u of toRemove) await cache.delete(u);       // 增量预缓存
}
```
