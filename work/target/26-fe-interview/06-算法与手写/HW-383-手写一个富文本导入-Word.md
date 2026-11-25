---
title: [HW-383] 手写一个富文本导入 Word：样式映射降级策略
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-383：手写一个富文本导入 Word：样式映射降级策略

**答**：
- 需求：实现 WordImport：Word HTML（粘贴/文件）解析——Word 特有标记清理（mso 样式/office 命名空间标签）；样式映射（Word 样式 → 内部 blocks：标题层级从 h1-h6 或 mso-outline 级别推断，列表识别 ul/ol）；降级策略（无法识别的样式退为普通段落，保留文本）；图片提取（data-uri 或引用占位）。
- 边界：mso-list 缩进推断列表层级；表格保留结构（转为表格块）；嵌套 div 段落合并；字节数上限截断。
- 评分点：mso 清理；层级推断；降级保文本。

```javascript
function wordImport(html) {
  const root = new DOMParser().parseFromString(html, 'text/html').body;
  root.querySelectorAll('[class*="Mso"], [style*="mso"]').forEach(el => {   // mso 清理
    [...el.attributes].forEach(a => { if (a.name === 'style' || a.name.startsWith('class')) el.removeAttribute(a.name); });
  });
  root.querySelectorAll('o\:p, xml, style, meta').forEach(el => el.remove());   // office 命名空间
  const blocks = [];
  const walk = (el, listDepth = 0) => {
    for (const node of el.children) {
      const tag = node.tagName.toLowerCase();
      if (/^h[1-6]$/.test(tag)) {                            // 标题推断
        blocks.push({ type: 'h' + tag[1], text: node.textContent.trim(), marks: [] });
      } else if (tag === 'ul' || tag === 'ol') {
        walkList(node, tag, listDepth + 1, blocks);          // 列表（缩进层级）
      } else if (tag === 'table') {
        blocks.push(toTableBlock(node));                     // 表格保留结构
      } else if (tag === 'p' || tag === 'div') {
        const text = node.textContent.trim();
        if (text) blocks.push({ type: 'p', text, marks: inlineMarks(node) });   // 降级为段落
        if (node.querySelector('img')) blocks.push({ type: 'image', src: 'placeholder', alt: 'word-image' });
        walk(node, listDepth);                               // 嵌套 div 递归
      } else walk(node, listDepth);
    }
  };
  walk(root);
  return blocks;
}
function walkList(el, tag, depth, blocks) {
  for (const li of el.children) {
    if (li.tagName === 'LI')
      blocks.push({ type: 'li', ordered: tag === 'ol', depth, text: li.textContent.trim(), marks: [] });
    const sub = li.querySelector('ul,ol');
    if (sub) walkList(sub, sub.tagName.toLowerCase(), depth + 1, blocks);   // 嵌套列表
  }
}
function inlineMarks(el) {                                  // 行内样式降级
  const marks = [];
  el.querySelectorAll('b,strong').forEach(() => marks.push({ type: 'bold', start: 0, end: 1 }));
  return marks;
}
function toTableBlock(tableEl) {
  const rows = [...tableEl.querySelectorAll('tr')].map(tr =>
    [...tr.querySelectorAll('td,th')].map(td => ({ text: td.textContent.trim() })));
  return { type: 'table', rows, cols: Math.max(...rows.map(r => r.length)) };
}
```
