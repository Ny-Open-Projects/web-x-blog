---
title: [904] RAG 答案的引用溯源怎么做，如何高亮到原文
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 引用溯源]
type: 面试题
---

## 904：RAG 答案的引用溯源怎么做，如何高亮到原文

**答**：
- 让模型在生成时标注引用：每个关键结论后附 [1][2] 编号，编号映射到本次检索的 chunk 列表；比生成后再匹配可靠。
- 前端高亮：chunk 元数据带文档路径与字符偏移（start/end），点击引用角标滚动到原文片段并高亮区间；偏移在索引阶段切分时就记录，避免事后模糊匹配。
- 校验层：答案中出现的引用编号必须存在于本次检索列表，越界编号剔除并计入幻觉指标。
- 追问钩子：模型编造引用编号怎么办？——用「先抽取答案句子，再与来源做相似度校验」的二次对齐兜底，相似度低于阈值的句子降级显示「未核实」。

```ts
interface Chunk { text: string; doc: string; start: number; end: number }
function renderCitations(answer: string, chunks: Chunk[]) {
  // 编号由 prompt 约定：模型只能引用给定列表
  return answer.replace(/\[(\d+)\]/g, (_, n) => {
    const c = chunks[Number(n) - 1];
    if (!c) { track('bad_citation'); return ''; } // 越界引用剔除
    return '<a href="#cite-' + n + '" data-doc="' + c.doc + '" data-start="' + c.start + '">[' + n + ']</a>';
  });
}
```

