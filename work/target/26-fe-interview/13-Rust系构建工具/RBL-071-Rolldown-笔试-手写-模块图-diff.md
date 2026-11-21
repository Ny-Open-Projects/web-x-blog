---
title: [RBL-071] 笔试：手写两次构建的模块归属 diff 工具（chunk 迁移检测）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-071：笔试：手写两次构建的模块归属 diff 工具（chunk 迁移检测）
**题目**：实现 diffChunkMembers(before, after)：输入两次构建的 chunk 信息数组 [{ chunkName, modules: ['src/a.ts', ...] }]，输出：1) 新增/删除的 chunk；2) 模块从 chunk X 迁移到 chunk Y 的清单；3) 同名 chunk 成员一致时输出 stable；4) 迁移会影响缓存命中，输出受影响入口的警告；5) 支持 --json 输出。

```javascript
function diffChunkMembers(before, after) {
  const b = new Map(before.map(c => [c.chunkName, new Set(c.modules)]));
  const a = new Map(after.map(c => [c.chunkName, new Set(c.modules)]));

  const added = [...a.keys()].filter(k => !b.has(k));
  const removed = [...b.keys()].filter(k => !a.has(k));

  // 模块 -> chunk 归属映射
  const ownerOf = (map) => {
    const m = new Map();
    for (const [chunk, mods] of map) for (const mod of mods) m.set(mod, chunk);
    return m;
  };
  const oB = ownerOf(b), oA = ownerOf(a);
  const moved = [];
  for (const [mod, beforeChunk] of oB) {
    const afterChunk = oA.get(mod);
    if (!afterChunk) continue; // 删除的模块不在此统计
    if (afterChunk !== beforeChunk)
      moved.push({ mod, from: beforeChunk, to: afterChunk });
  }
  const stable = [...a.keys()].filter(k =>
    b.has(k) && setsEqual(b.get(k), a.get(k)));
  const affected = [...new Set(moved.flatMap(x => [x.from, x.to]))];
  return { added, removed, moved, stable, affectedChunks: affected };
}
const setsEqual = (s1, s2) =>
  s1.size === s2.size && [...s1].every(x => s2.has(x));
module.exports = { diffChunkMembers };
```
**评分点**：
- 双 Map 结构：chunk 视角 + 模块归属视角（diff 需要两种投影）。
- 迁移检测的语义（from→to），不只是"有无变化"。
- 归属变化影响长效缓存——输出受影响 chunk 清单（工程意识）。
- stable 判定用集合相等（顺序无关）。
- 能联系 CI 门禁：moved 数量突增通常由 manualChunks/advancedChunks 配置改动引起。
