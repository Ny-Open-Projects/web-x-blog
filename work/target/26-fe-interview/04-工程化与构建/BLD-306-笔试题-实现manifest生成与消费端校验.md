---
title: [BLD-306] 笔试题——实现 manifest 生成与消费端校验？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-306：手写 manifest 校验

**需求与边界**：
- 需求：生成统一 manifest（SCN-BLD-240 schema）并校验——① 完整性（entry/chunks/assets 引用的文件全部存在于产物目录）；② 依赖图一致性（chunk.imports 中的 chunk 在 manifest 内）；③ 无环校验（chunk 依赖图——SCN-BLD-214 死锁防御）；④ schema 版本与消费端兼容。
- 边界：① 文件存在性是绝对校验（缺失即阻断——HTML 悬空引用防御）；② 环检测输出环路径；③ schemaVersion 兼容检查（消费端只认 v2 时 v1 拒绝）。

**答**：
```javascript
function verifyManifest(manifest, dist) {
  const issues = [];
  const allFiles = new Set(Object.values(manifest.chunks).map(c => c.file)
    .concat(Object.values(manifest.assets).map(a => a.file))
    .concat(Object.values(manifest.entry)));
  // 1. 文件存在性
  for (const f of allFiles)
    if (!fs.existsSync(path.join(dist, f)))
      issues.push({ type: 'FILE_MISSING', file: f, level: 'block' });   // 悬空引用
  // 2. 依赖图一致性
  for (const [name, c] of Object.entries(manifest.chunks))
    for (const imp of c.imports ?? [])
      if (!(imp in manifest.chunks))
        issues.push({ type: 'IMPORT_NOT_IN_MANIFEST', chunk: name, import: imp });
  // 3. 无环
  const color = {}, cycles = [];
  const dfs = (n, path) => {
    if (color[n] === 1) { cycles.push([...path.slice(path.indexOf(n)), n]); return; }
    if (color[n] === 2) return;
    color[n] = 1; path.push(n);
    (manifest.chunks[n]?.imports ?? []).forEach(i => dfs(i, path));
    color[n] = 2;
  };
  Object.keys(manifest.chunks).forEach(n => dfs(n, []));
  cycles.forEach(c => issues.push({ type: 'CHUNK_CYCLE', cycle: c, level: 'block' }));
  // 4. schema 版本
  if (!CONSUMERS.every(c => c.accepts(manifest.schemaVersion)))
    issues.push({ type: 'SCHEMA_INCOMPAT', schemaVersion: manifest.schemaVersion });
  return { ok: !issues.some(i => i.level === 'block'), issues };
}
```

**评分点**:
- 四项校验（文件存在/依赖一致/无环/schema 兼容）。
- 环检测输出环路径（SCN-BLD-214 死锁防御）。
- 阻断级别区分（文件缺失阻断/schema 不兼容可降级）。
- 消费端兼容显式检查（多消费方版本协商）。
