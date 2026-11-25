---
title: [NODE-818] 笔试题——实现 HTML 静态资源注入（manifest 驱动 + preload 编排）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-818：手写资源注入

**需求与边界**：
- 需求：SSR HTML 资源注入（SCN-BLD-325/240）——① manifest 驱动（entry/chunks/assets——SCN-BLD-240 schema）；② preload 编排（modulepreload 依赖链 + 字体 crossorigin——SCN-ENG-325）；③ 资源位置（CSS head/script deferred——FOUC 防御，SCN-BLD-236）；④ 注入一致性校验（manifest 引用的资源全存在——SCN-BLD-306）。
- 边界：① chunk 依赖链 preload（SCN-ENG-325 深度限制）；② buildinfo meta 注入（SCN-ENG-309 三通道）；③ CSP nonce 注入（SCN-BLD-246）。

**答**：
```javascript
function injectAssets(html, manifest, { nonce }) {
  const tags = [];
  for (const c of manifest.chunks[manifest.entry].imports ?? [])   // 依赖链 modulepreload（SCN-ENG-325）
    tags.push(`<link rel="modulepreload" href="/${c.file}">`);
  for (const css of manifest.chunks[manifest.entry].css ?? [])
    tags.push(`<link rel="stylesheet" href="/${css}">`);
  for (const font of manifest.assets.fonts ?? [])
    tags.push(`<link rel="preload" href="/${font.file}" as="font" crossorigin>`);   // crossorigin！（SCN-ENG-241）
  tags.push(`<script defer src="/${manifest.entry.main}"></script>`);   // deferred（SCN-BLD-236）
  tags.push(`<meta name="build:commit" content="${manifest.build.commit}">`);   // buildinfo（SCN-ENG-309）
  return html.replace('</head>', `${tags.join('\n')}</head>`);
}
// 注入一致性（SCN-BLD-306）
verifyAssetsExist(manifest);                           // 悬空引用防御
```

**评分点**:
- manifest 驱动注入（SCN-BLD-240 schema 契约）。
- preload 编排（modulepreload 链 + 字体 crossorigin——SCN-ENG-325/241）。
- 位置语义（CSS head/script defer——FOUC 防御）。
- buildinfo meta + 悬空校验（SCN-ENG-309/BLD-306）。
