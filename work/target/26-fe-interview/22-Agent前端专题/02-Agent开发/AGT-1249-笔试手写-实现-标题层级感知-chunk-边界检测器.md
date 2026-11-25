---
title: [1249] 笔试手写：实现 标题层级感知 chunk 边界检测器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG]
type: 笔试题
---

## 1249：笔试手写：实现 标题层级感知 chunk 边界检测器

**答**：实现 chunkByHeading(doc)：doc 为 { level, text }[] 行数组（level 1~4，0 表示正文行），maxLen=500。规则：遇 level<=2 的标题开新块；level>=3 标题并入当前块；单块超过 maxLen 时在最近的正文行边界硬切；标题行永不与正文硬切分离。返回块数组 { lines, chars }。

```js
function chunkByHeading(doc, maxLen = 500) {
  const chunks = [];
  let cur = { lines: [], chars: 0 };
  const push = () => { if (cur.lines.length) chunks.push(cur); cur = { lines: [], chars: 0 }; };
  for (const row of doc) {
    const len = row.text.length;
    if (row.level > 0 && row.level <= 2) push();      // 高级标题强制开新块
    if (cur.chars + len > maxLen && row.level === 0) { // 正文超长硬切
      push();
    }
    cur.lines.push(row.text); cur.chars += len;
  }
  push();
  return chunks;
}
```

**评分点**：
- 层级 <=2 重置边界、>=3 保持上下文（父子分块思想的边界层）
- 硬切只在正文行、标题不孤行
- chars 统计与 maxLen 比较在追加前判断
- 能讨论：块间重叠（overlap）与元数据继承
