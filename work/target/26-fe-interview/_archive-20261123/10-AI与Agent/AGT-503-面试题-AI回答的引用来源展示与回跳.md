---
title: [AGT-503] 回答里引用了知识库/RAG 片段时，前端如何展示引用并支持点击回跳原文？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-503：回答里引用了知识库/RAG 片段时，前端如何展示引用并支持点击回跳原文

**答**：
- 模型输出用特殊标记（如 [^1] 或 <cite id>）标注引用，前端渲染成可点击角标；标记必须来自服务端结构化数据，不要让模型自由发挥 URL（会编造）。
- 点击角标展开「来源卡」：原文片段 + 高亮命中句 + 元信息（文档名/更新时间/置信度），支持跳转到原文档锚点。
- 无引用支撑的段落要弱化展示（灰色边或"未引用来源"提示），这是幻觉治理在 UI 层的最后一道防线。

```javascript
// 引用渲染：把 [^1] 替换为可点击组件，点击弹出来源卡
function renderWithCitations(text, sources) {
  return text.replace(/\[\^(\d+)\]/g, (_, n) => {
    const src = sources[+n - 1];
    if (!src) return ''; // 服务端没有对应来源的引用号直接丢弃，防幻觉
    return `<cite data-id="${src.id}" title="${src.docName}">[${n}]</cite>`;
  });
}
function onCiteClick(srcId) {
  const src = sources.find(s => s.id === srcId);
  openSourceCard(src);            // 弹层：片段+高亮+元信息
  bus.emit('cite:jump', src.anchor); // 若原文档已打开则滚动到锚点
}
```

