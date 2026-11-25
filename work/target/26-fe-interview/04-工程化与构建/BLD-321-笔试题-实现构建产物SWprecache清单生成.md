---
title: [BLD-321] 笔试题——实现 SW precache 清单生成与增量更新？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-321：手写 SW precache

**需求与边界**：
- 需求：从 manifest 生成 SW precache（SCN-BLD-250）——① 全量清单（hash 文件 + revision）；② 增量更新语义（新旧清单 diff——SW 安装只下载新增）；③ 版本绑定（SW 版本 = buildinfo commit——SW 与产物一致性）；④ 双通道策略生成（precache + runtime 路由规则）。
- 边界：① diff 算法（旧清单还在的文件跳过下载——incremental install）；② HTML 特殊处理（每版本唯一 precache——导航 fallback 指向当前版本）；③ 清理旧缓存（新 SW activate 时删除非当前版本缓存）。

**答**：
```javascript
function generateSW(manifest, prevManifest, buildinfo) {
  const files = manifest.allFiles().map(f => ({
    url: f.path, revision: f.hash }));                 // hash 即 revision
  const prevSet = new Set(prevManifest?.allFiles().map(f => f.path) ?? []);
  const incremental = files.filter(f => !prevSet.has(f.url) ||
    prevManifest.find(f2 => f2.url === f.url)?.hash !== f.hash);   // 新增或内容变化才下载
  return `// SW v=${buildinfo.commit}（与产物绑定——SCN-BLD-250 一致性）
const PRECACHE = ${JSON.stringify(files)};
const PRECACHE_VERSION = 'v-${buildinfo.commit}';
install: caches.open(PRECACHE_VERSION).then(c =>
  Promise.all(incremental.map(f => c.add(new Request(f.url, { cache: 'reload' })))));   // 增量安装
activate: caches.keys().then(keys =>
  keys.filter(k => k.startsWith('v-') && k !== PRECACHE_VERSION)
    .forEach(k => caches.delete(k)));                  // 旧版本缓存清理
routing: { navigateFallback: '/index.html', api: networkFirst, images: cacheFirst }`;
}
```

**评分点**:
- 增量安装（diff 新增/变化才下载——用户体验）。
- 版本绑定（SW 版本 = buildinfo commit——一致性红线）。
- activate 清理旧缓存（版本切换收尾）。
- 双通道策略生成（precache + runtime 路由——SCN-BLD-250）。
