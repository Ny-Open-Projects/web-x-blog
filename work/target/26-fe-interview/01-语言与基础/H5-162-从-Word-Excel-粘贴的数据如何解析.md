---
title: [H5-162] 从 Word/Excel 粘贴的数据如何解析？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-162：从 Word/Excel 粘贴的数据如何解析？
**答**：
- Excel 粘贴：`text/plain` 是 **TSV**（\t 分列、\n 分行）——最可靠的数据通道，直接 split 转表格数据；`text/html` 里有带样式的 `<table>` 可选保留。
- Word 粘贴：`text/html` 是"堆料"——`mso-*` 样式、`o:p` 等命名空间私有标签、条件注释、class 垃圾，需要清洗（解析 → 剥私有标签 → 白名单属性）。
- Word 图片：HTML 里的 img.src 常是本地引用，真实图片在 `clipboardData.items` 的 `image/*` 里——要走上传换 URL。
- 完整产品的清洗目标是映射到编辑器 schema（段落/表格/列表），而不是保留 Word 样式。

```html
<div id="ed" contenteditable="true">从 Word/Excel 粘贴内容试试</div>
<script>
document.getElementById('ed').addEventListener('paste', (e) => {
  e.preventDefault();
  const dt = e.clipboardData;
  const html = dt.getData('text/html');
  const plain = dt.getData('text/plain');

  // Excel：text/plain 是 TSV（\t 分列 \n 分行）—— 最可靠的数据通道
  if (looksLikeTSV(plain)) return insertTable(parseTSV(plain));

  // Word：text/html 是 mso 样式 + 私有标签的"堆料"，清洗后插入
  if (html) insertNode(cleanOffice(html));
});

function looksLikeTSV(text) {
  const lines = text.replace(/\r/g, '').split('\n').filter(Boolean);
  return lines.length > 1 || lines[0]?.includes('\t');
}
function parseTSV(text) {
  return text.replace(/\r/g, '').split('\n')
    .filter((l) => l.length)
    .map((l) => l.split('\t'));
}
function insertTable(rows) {
  const table = document.createElement('table');
  table.border = 1;
  for (const row of rows) {
    const tr = table.insertRow();
    for (const cell of row) tr.insertCell().textContent = cell;
  }
  insertNode(table);
}

// Word 清洗：剥掉 Office 私有内容，只留结构
function cleanOffice(html) {
  const doc = new DOMParser().parseFromString(html, 'text/html');
  doc.querySelectorAll('style, script').forEach((n) => n.remove());
  [...doc.body.querySelectorAll('*')].forEach((el) => {
    if (el.localName.includes(':')) return el.remove();  // o:p、w:xxx 私有标签
    [...el.attributes].forEach((a) => {
      // mso-* 属性 / class / style 全部剥掉
      if (a.name.startsWith('mso') || a.name === 'class' || a.name === 'style')
        el.removeAttribute(a.name);
    });
  });
  doc.querySelectorAll('img').forEach((img) => img.remove());  // 演示简化
  return doc.body;
}
function insertNode(node) {
  const sel = document.getSelection();
  const r = sel.getRangeAt(0);
  r.deleteContents();
  r.insertNode(node);
  sel.collapseToEnd();
}
// 完整产品做法：保留表格/列表结构 → items 里的 image/* 上传换 src →
// Word 样式（加粗/字号在 span style 里）二次解析映射到编辑器 schema
</script>
```

## 二十七、SVG 工程化
