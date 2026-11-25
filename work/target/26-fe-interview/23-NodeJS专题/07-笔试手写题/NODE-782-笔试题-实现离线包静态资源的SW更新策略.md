---
title: [NODE-782] 笔试题——实现 SW precache 增量与版本对齐服务端？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-782：手写 SW 服务端

**需求与边界**：
- 需求：SW precache 服务端（SCN-BLD-321 延伸）——① precache 清单端点（按客户端版本 diff 增量——SCN-BLD-321）；② SW 版本与产物一致性校验（buildinfo 绑定——SCN-BLD-303）；③ 旧版本缓存清理通知（activate 语义服务端配合）；④ 兼容期（多版本 SW 并存——SCN-OPS-218）。
- 边界：① 增量 diff 基于客户端上报版本（X-SW-Version——端侧版本感知）；② precache 的签名（清单防篡改——SCN-BLD-322）；③ 版本清单缓存的键维度（buildinfo 全维度——SCN-NODE-718）。

**答**：
```javascript
app.get('/sw/precache', (req, res) => {
  const clientVer = req.headers['x-sw-version'];       // 客户端 SW 版本（增量基线）
  const current = manifestFor(buildInfo.latest);
  const prev = manifestFor(clientVer);
  const incremental = current.allFiles().filter(f =>
    !prev?.has(f.path) || prev.get(f.path).hash !== f.hash);   // 增量（SCN-BLD-321）
  if (buildinfoMismatch(clientVer))                    // 版本一致性（SCN-BLD-303）
    return res.status(409).json({ code: 'VERSION_MISMATCH', note: 'SW 版本与产物不符' });
  res.json({ files: incremental, full: !prev, revision: buildInfo.commit,
    signature: sign(JSON.stringify(incremental)) });   // 清单签名（SCN-BLD-322）
});
// activate 清理（SW 端——服务端提供清理依据）
app.get('/sw/stale-versions', (req, res) =>            // 当前有效版本（旧版本清理依据）
  res.json({ valid: buildInfo.recent(3) }));           // N-1 兼容（SCN-OPS-218 保留窗口）
```

**评分点**:
- 增量 diff 基于客户端版本上报（X-SW-Version——SCN-BLD-321）。
- SW 版本与产物一致性校验（409 拒绝——SCN-BLD-303）。
- 清单签名（防篡改——SCN-BLD-322）。
- N-1 兼容版本清单（旧 SW 保留窗口——SCN-OPS-218）。
