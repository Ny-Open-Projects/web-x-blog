---
title: [BLD-320] 笔试题——实现产物与 CSP 报告对账（违规归因）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-320：手写 CSP 对账

**需求与边界**：
- 需求：CSP Report-Only 违规报告与产物对账（SCN-BLD-246）——① 违规聚合（violated-directive + source-file）；② 归因分类（打包器 eval——HMR 残留/style 注入——style-loader/内联脚本——无 nonce）；③ 修复建议映射；④ 收紧判定（违规归零才允许从 Report-Only 转 enforce）。
- 边界：① source-file 从报告的 document-uri/source-file 解析（定位到 chunk）；② 误报过滤（浏览器插件注入的违规——域名白名单）；③ 收紧前回归（enforce 后全功能回归）。

**答**：
```javascript
function cspReconcile(reports, manifest) {
  const grouped = groupBy(reports.filter(r => !isExtensionNoise(r)),   // 插件误报过滤
    r => r['violated-directive']);
  const findings = Object.entries(grouped).map(([directive, list]) => {
    const sample = list[0];
    const chunk = locateChunk(sample['source-file'], manifest);   // 定位产物 chunk
    const cause = classifyCspCause(directive, chunk);
    return { directive, count: list.length, chunk,
      cause, fix: CSP_FIX[cause] };
  });
  return {
    findings,
    canEnforce: findings.length === 0,                 // 归零才收紧
    fixMap: {
      'eval-hmr': '生产构建禁 eval（dev HMR 产物不进 prod）',
      'style-inline': 'style-loader → mini-css-extract（SCN-BLD-206）',
      'script-inline': '内联脚本加 nonce（构建期注入）',
    },
    note: '收紧前跑全功能回归（enforce 后拦截即功能失效）',
  };
}
function classifyCspCause(directive, chunk) {
  if (directive.startsWith('script') && chunk?.includes('runtime')) return 'eval-hmr';
  if (directive.startsWith('style')) return 'style-inline';
  if (directive.startsWith('script') && chunk?.includes('index')) return 'script-inline';
  return 'unknown';
}
```

**评分点**:
- 违规聚合 + chunk 定位（source-file → manifest 归因）。
- 三类归因映射修复（eval/style/inline——SCN-BLD-246 三源）。
- 插件误报过滤（域名白名单）。
- canEnforce 判定（归零才收紧 + 收紧前回归）。
