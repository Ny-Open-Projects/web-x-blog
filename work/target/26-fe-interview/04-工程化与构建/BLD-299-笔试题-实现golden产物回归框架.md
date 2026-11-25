---
title: [BLD-299] 笔试题——实现 golden 产物回归框架（升级验证）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-299：手写 golden 回归框架

**需求与边界**：
- 需求：构建工具升级验证（SCN-BLD-252）——① fixture 矩阵构建（代表性项目集）；② 新旧产物 diff 自动分类（hash-only/collection/semantic）；③ semantic 级变化必须人工解释（阻断）；④ golden 更新流程（解释后更新基线）。
- 边界：① 分类器规则（hash-only = 文件内容变但 chunk 集合与导出面不变）；② semantic 检测（导出面 diff——产物暴露的 API 变了）；③ 更新 golden 需关联解释记录（审计）。

**答**：
```javascript
async function goldenRegression(oldTool, newTool, fixtures) {
  const report = [];
  for (const fixture of fixtures) {
    const old = await build(fixture, oldTool);
    const cur = await build(fixture, newTool);
    const d = classifyDiff(old, cur);
    report.push({ fixture: fixture.name, ...d });
  }
  const semantic = report.filter(r => r.semantic.length);
  const collection = report.filter(r => r.collection.length);
  if (semantic.length || collection.length)
    return {
      blocked: true,
      explain: [...semantic, ...collection].map(r =>
        `${r.fixture}: ${[...r.semantic, ...r.collection].join(', ')}——逐项解释后更新 golden`),
    };
  return { blocked: false, hashOnly: report.length };   // hash-only 自动放行
}
function classifyDiff(old, cur) {
  const chunkSetSame = sameChunkNames(old, cur);
  const exportsSame = sameExportSurface(old, cur);     // 导出面（semantic 判据）
  const contentChanged = anyContentDiff(old, cur);
  return {
    hashOnly: contentChanged && chunkSetSame && exportsSame,
    collection: !chunkSetSame ? chunkSetDiff(old, cur) : [],
    semantic: !exportsSame ? exportSurfaceDiff(old, cur) : [],
  };
}
// 更新 golden（解释后）
updateGolden(newTool, { explained: '升级 terser → esbuild，minify 字节差' });
```

**评分点**:
- 三级分类（hash-only/collection/semantic——人工注意力聚焦）。
- 导出面作为 semantic 判据（产物 API 语义）。
- 阻断 + 解释清单（升级验证可操作）。
- golden 更新关联解释记录（审计——SCN-BLD-252）。
