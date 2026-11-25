---
title: [AGT-702] 知识库里的表格（财务数据/配置参数）如何切块与索引才能被准确问答？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-702：知识库里的表格（财务数据/配置参数）如何切块与索引才能被准确问答

**答**：
- 表格三种表示并存：① Markdown 线性化（整表转文本，小表直接进 chunk）；② 行级展开（大表每行转"列名：值"句子，行级检索）；③ 表头+摘要索引（大表的概览块说明"此表是什么/列含义/行数"，命中后取回全表）。
- 关键：表格 cell 里的值必须与表头绑定检索（"2023 年 Q3 华东区退款率"需要 行头+列头+cell 三元组语义），纯文本切块会断开这个绑定。
- 数值精度问题：答案生成时表格数据用结构化传递（JSON 而非渲染后的文本），避免模型抄错数字。

```javascript
function tableToChunks(table) {
  if (table.rows.length <= 10)
    return [{ kind: 'table-md', text: toMarkdown(table) }];   // 小表整体
  return [
    { kind: 'table-summary', text: tableSummary(table) },     // 概览块
    ...table.rows.map((row, i) => ({                          // 行级展开
      kind: 'table-row',
      text: row.map((cell, j) =>
        `${table.headers[j]}: ${cell}`).join('；')            // 行头绑定列头
        + `（第${i + 1}行，来源：${table.title}）`,
      rowRef: i })),
  ];
}
```

