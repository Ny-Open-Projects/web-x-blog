---
title: [917] 知识库里大量 PDF 和截图，多模态 RAG 落地的坑
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 多模态]
type: 面试题
---

## 917：知识库里大量 PDF 和截图，多模态 RAG 落地的坑

**答**：
- PDF 的坑在「不是纯文本」：双栏排版把阅读顺序打乱、扫描件是图片、表格是矢量绘制。解析要用布局感知模型（版面分析）而不是 pdftotext 一把梭。
- 截图类：走 caption 模型生成文字描述入索引，命中后原图随引用返回；纯 UI 截图要把图中文字 OCR 出来合并进 caption。
- 图文混排文档建议「图随文走」：图片 caption 与相邻段落合并成一个 chunk，回答时模型可同时引用文字与图。
- 追问钩子：为什么不让多模态模型直接读图而要预生成 caption？——检索阶段要入向量索引必须有文本表示；推理阶段可以直接传图，但成本与延迟要按 QA 优先级控制。

```ts
async function ingestPdf(file) {
  const pages = await layoutParse(file);              // 版面感知：区分文本/表格/图
  for (const p of pages) {
    for (const block of p.blocks) {
      if (block.type === 'image') {
        const caption = await caption(block.image);   // 图 -> 文本入索引
        index.add({ text: block.ocrText + '\n' + caption, meta: { page: p.no, img: block.image } });
      } else if (block.type === 'table') {
        index.add({ text: block.raw, meta: { page: p.no, type: 'table' } }); // 表格整块
      } else index.add({ text: block.text, meta: { page: p.no } });
    }
  }
}
```

