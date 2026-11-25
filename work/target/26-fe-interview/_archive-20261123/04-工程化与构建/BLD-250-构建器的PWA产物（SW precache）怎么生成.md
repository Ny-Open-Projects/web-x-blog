---
title: [BLD-250] PWA 产物（Service Worker precache）怎么生成？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-250：PWA 产物怎么生成？
**答**：
- precache 清单：构建时从 manifest 生成 precache 列表（hash 文件 + revision）——SW 生成是构建流程的一环（依赖产物清单，SCN-BLD-240）。
- 缓存策略编排：precache（App shell 全量）+ runtime caching（接口 networkFirst/图片 cacheFirst 按资源类型路由）。
- 更新语义：SW 更新 = 新 precache 清单 diff（增量安装）+ skipWaiting/waiting 的 UX（更新提示而非静默替换——用户可能正在填表单）。
- 一致性风险：precach 的 HTML 引用旧 chunk——SW 版本与产物版本绑定（同一构建产出）。
- 追问钩子：为什么「SW 更新提示而非静默 skipWaiting」——静默更新会杀死用户正在进行的会话（表单填一半页面重载）；waiting + 用户确认（「有新版本，刷新生效」）把更新时机交给用户——这是 PWA 与普通网页在「版本切换 UX」上的本质差异，也呼应 SCN-OPS-232 长会话处理。

```javascript
// workbox 构建期生成
injectManifest({ precache: manifestToPrecacheList(manifest),   // 从构建 manifest 生成
  navigateFallback: '/index.html' });
// runtime 路由
registerRoute(({url}) => url.pathname.startsWith('/api/'), new NetworkFirst());
registerRoute(({request}) => request.destination === 'image', new CacheFirst());
// 更新 UX
self.addEventListener('waiting', () => showUpdateToast());   // 用户确认后 skipWaiting
```
