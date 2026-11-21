---
title: [RBL-202] Rspack 插件里怎么安全读写产物（Source 与 updateAsset）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-202：Rspack 插件里怎么安全读写产物

**答**:
- 产物是 `RspackSource` 抽象（RawSource/ConcatSource/SourceMapSource），读用 `source().buffer()` 或 `sourceAndMap()`（带 sourcemap）
- 写必须走 `compilation.updateAsset(name, newSource)` 或 `emitAsset`，直接改对象无效（资产表在 Rust 侧）
- 修改 JS 内容必须保留 sourcemap：`sourceAndMap()` 取 map → 修改文本 → `new SourceMapSource(newCode, name, map)`，否则 map 断链
- assetInfo（immutable/development）随 updateAsset 第三参数透传，影响 HTTP 缓存头

```javascript
compilation.hooks.processAssets.tap({ name: 'Banner', stage: -100 }, (assets) => {
  for (const name of Object.keys(assets)) {
    if (!name.endsWith('.js')) continue
    const { source, map } = assets[name].sourceAndMap()
    const code = `/*! build:${new Date().toISOString()} */\n` + source
    compilation.updateAsset(name,
      new compiler.rspack.sources.SourceMapSource(code, name, map),
      { development: true })     // 保留 assetInfo
  }
})
```
