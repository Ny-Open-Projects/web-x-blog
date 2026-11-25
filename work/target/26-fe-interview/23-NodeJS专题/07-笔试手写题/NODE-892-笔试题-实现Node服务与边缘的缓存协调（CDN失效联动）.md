---
title: [NODE-892] 笔试题——实现 CDN 缓存失效联动（数据更新→边缘刷新）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-892：手写 CDN 联动

**需求与边界**：
- 需求：CDN 失效联动（SCN-OPS-256/ENG-256）——① 数据更新触发 CDN purge（边缘刷新——SCN-OPS-256 只刷 HTML 语义的服务端版）；② 分域分级失效（API 缓存/静态缓存——不同策略）；③ 失效的确认（purge 后验证——SCN-OPS-246 校验）；④ 失效风暴防御（合并——SCN-OPS-320）。
- 边界：① 边缘缓存的键（URL+Vary——SCN-NODE-692）；② purge 的成本（全站 vs 精准——SCN-OPS-256）；③ 失效的灰度联动（SCN-OPS-216）。

**答**：
```javascript
async function onCacheableUpdate(keys) {
  const paths = keys.map(k => cachePath(k));           // 数据 → 缓存路径映射
  await cdn.purge({ paths, precise: true });           // 精准 purge（SCN-OPS-256 不全站）
  const verified = await verifyEdgePurge(paths);       // purge 后验证（SCN-OPS-246）
  if (!verified) alert({ type: 'CDN_PURGE_FAIL', paths });
}
// 批量合并（SCN-OPS-320）
const pending = new Set(); let timer;
function onCacheableUpdateMerged(keys) {
  keys.forEach(k => pending.add(k));
  clearTimeout(timer); timer = setTimeout(() => onCacheableUpdate([...pending]), 100);   // 合并
}
```

**评分点**:
- 精准 purge（不全站——SCN-OPS-256）。
- purge 后验证（SCN-OPS-246）。
- 批量合并（SCN-OPS-320）。
- Vary 联动（SCN-NODE-692）。
