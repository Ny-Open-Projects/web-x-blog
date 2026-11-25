---
title: [911] 知识库里的表格和代码块，RAG 检索怎么处理
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 结构化数据]
type: 面试题
---

## 911：知识库里的表格和代码块，RAG 检索怎么处理

**答**：
- 表格：整块保留 + 生成「行级摘要」辅助召回（把每行转成自然语言句子单独索引，命中后回链到整表），否则「A 产品 2024 年营收」这种 query 向量上和表格单元格里的一串数字毫无交集。
- 代码：按函数/类边界切，保留签名行 + docstring 作为 chunk 开头；语言识别交给 parser 而非正则。
- 两类内容都建议走「结构化抽取」兜底：表格关键列抽成 key-value 索引，代码抽函数名、参数名的精确索引（BM25）为主、向量为辅。
- 追问钩子：为什么代码不建议只用向量？——代码语义在符号而非自然语言，`useState` 和「hook 状态」的向量距离很远，精确索引才是主力。

```ts
function indexTable(table: Table) {
  index.add({ type: 'table', text: table.raw, meta: table.meta });          // 整表
  for (const row of table.rows) {                                           // 行级摘要
    index.add({
      type: 'row_digest',
      text: table.columns.map((c, i) => c + '是' + row[i]).join('，'),
      meta: { ...table.meta, rowIndex: row.__i, backlink: table.id }, // 命中回链整表
    });
  }
}
```

