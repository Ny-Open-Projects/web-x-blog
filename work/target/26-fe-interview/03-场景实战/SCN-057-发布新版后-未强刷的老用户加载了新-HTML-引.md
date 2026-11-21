---
title: [SCN-057] 发布新版后，未强刷的老用户加载了新 HTML 引用旧 chunk，页面报 ChunkLoadError，如何根治多版本共存问题？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-057：发布新版后，未强刷的老用户加载了新 HTML 引用旧 chunk，页面报 ChunkLoadError，如何根治多版本共存问题？
**答**：
- 根因是 HTML 与 hash 资源不同步：老 HTML 引用的旧 chunk 在新发布后被删除。发布端必须做"不覆盖式发布"：保留最近 N 个版本的静态资源目录。
- 运行时兜底：全局捕获 ChunkLoadError 自动刷新一次页面（重新拉新 HTML），刷新计数防死循环。
- 主动升级：轮询 version.json 对比构建版本，发现新版本在用户切走标签页时静默 reload，把更新成本降到零。

```javascript
// ChunkLoadError 自愈：动态 import 失败时刷新一次，计数防死循环
const RELOAD_KEY = 'chunk-reload';
window.addEventListener('error', (e) => {
  if (!/ChunkLoadError|Loading chunk/.test(e.message || '')) return;
  const last = +sessionStorage.getItem(RELOAD_KEY) || 0;
  if (Date.now() - last < 10000) return;            // 10 秒内已刷新过，不再刷
  sessionStorage.setItem(RELOAD_KEY, String(Date.now()));
  location.reload();                                // 重新拉新 HTML 与配套资源
}, true);

// 版本轮询：发现新版本后，趁用户切走标签页时静默更新
let version = document.querySelector('meta[name="build-version"]').content;
setInterval(async () => {
  const { version: latest } = await fetch('/version.json', { cache: 'no-store' }).then((r) => r.json());
  if (latest !== version && document.visibilityState === 'hidden') {
    location.reload();                              // 后台标签页刷新用户无感
  }
}, 5 * 60 * 1000);
```
