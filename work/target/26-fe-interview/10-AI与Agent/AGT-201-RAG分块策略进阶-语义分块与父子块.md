---
title: [AGT-201] RAG 分块策略进阶——语义分块与父子块怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-201：RAG 的分块策略怎么做到进阶——语义分块与父子块？

**答**:
- 固定分块的痛点：按 token 硬切会把语义完整的段落/代码/表格切断，检索命中了碎片却答不出问题——分块的第一原则是"按语义边界切，token 只是上限"。
- 语义分块三层：结构分块（按 Markdown 标题/代码块/表格天然边界，最优先）、句子级语义分块（相邻句 embedding 相似度骤降处切开）、滑动窗口兜底（超长段落二次切，带 overlap 10%~15% 防止边界丢信息）。
- 父子块（small-to-big）：检索用子块（小而精，embedding 质量高），命中后返回父块（大而全，给模型完整上下文）——检索精度与上下文完整性解耦，是生产 RAG 最常用的组合。
- 块元数据必带：来源文档/章节路径/页码/更新时间/权限标签——没有元数据的块无法做引用溯源、过滤与权限剪枝（见 AGT-151 的权限过滤）。

```javascript
// 父子块分块示意
function splitDocument(doc) {
  const parents = splitByHeading(doc);        // 一级：按标题切父块
  return parents.map(p => {
    if (tokenLen(p) <= PARENT_LIMIT) return { parent: p, children: [p] };
    const children = semanticSplit(p, CHILD_TOKENS, OVERLAP); // 语义切子块
    return { parent: p, children };            // 子块带 parent_id / 章节路径
  });
}
// 检索：query → 向量库召回 children top-k
// → 按 parent_id 去重取父块 → 拼上下文
// overlap 防边界：后块复用前块末尾 10% 内容
```
