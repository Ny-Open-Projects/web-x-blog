---
title: [SCN-1213] AI 产品的 RAG 检索引用渲染
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1213：AI 产品的 RAG 检索引用渲染

**答**：
- 引用：回答带引用标注（[1][2]），点击展开来源卡片（文档名/片段/链接）。
- 溯源：悬浮引用高亮原文片段（对照）。
- 信任：无引用支撑的结论标注"模型推断"（可核实性）。

```javascript
// 引用渲染
function renderCitations(answer, sources) {
  const refs = [...answer.matchAll(/\[(\d+)\]/g)]
    .map(m => sources[+m[1] - 1]).filter(Boolean);
  return {
    html: answer.replace(/\[(\d+)\]/g,
      (m, n) => `<sup class="cite" data-ref="${n}">[${n}]</sup>`),
    sources: refs.map(s => ({ title: s.title, snippet: s.snippet, url: s.url })),
    uncovered: sources.length === 0 ? '本回答无检索依据' : null,
  };
}
```
