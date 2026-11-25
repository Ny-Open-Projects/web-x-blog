---
title: [ENG-305] 笔试题——实现 sourcemap 版本匹配还原（buildinfo → map → 源码定位）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-305：手写 sourcemap 版本匹配还原

**需求与边界**：
- 需求：错误堆栈（bundle 文件 + 行列）→ 按 buildSha 匹配 sourcemap → 还原为源码位置（文件:行:列 + 上下文代码片段）。
- 边界：① map 缺失时降级输出 bundle 位置（不静默失败）；② 多层堆栈逐帧还原；③ 还原位置落在生成代码（eval/module wrapper）时标注。

**答**：
```javascript
function restoreStack(stack, buildSha, mapStore) {
  return stack.map(frame => {
    const map = mapStore[buildSha]?.[frame.file];     // SCN-ENG-223 buildinfo 匹配
    if (!map)
      return { ...frame, degraded: true, note: 'sourcemap 缺失，仅 bundle 位置' };
    const pos = originalPositionFor(map, { line: frame.line, column: frame.column });
    if (!pos.source || pos.source.includes('eval'))
      return { ...frame, degraded: true, note: '生成代码帧（eval/wrapper）' };
    const context = readSourceContext(pos.source, pos.line, 3);   // 上下文 3 行
    return { ...frame, source: pos.source, line: pos.line, column: pos.column, context };
  });
}
// 上传关联（构建期）
// sentry-cli releases files <buildSha> upload-sourcemaps dist --rewrite
// 保留策略
purgeMaps({ keepReleases: 30 });                     // 与线上版本生命周期对齐
```

**评分点**:
- buildSha → map 的版本匹配（错版本还原错源码——必须严格键控）。
- map 缺失/生成帧降级标注（不静默）。
- 逐帧还原 + 上下文片段（可直接排障）。
- 保留策略与版本生命周期对齐。
