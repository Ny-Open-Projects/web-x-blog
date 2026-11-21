---
title: [H5-153] contenteditable 如何用 Selection/Range 实现富文本操作？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-153：contenteditable 如何用 Selection/Range 实现富文本操作？
**答**：
- 读取选区：`document.getSelection()` 可能含多个 Range，编辑器场景取 `getRangeAt(0)`；`collapsed` 表示光标无选中。
- 常用操作：`extractContents()` 摘出片段 + `insertNode()` 插入包裹节点（加粗/高亮/链接），跨元素选区直接 `surroundContents` 会抛错，需先摘出再插入。
- 插入后 `collapseToEnd()` 处理光标，`normalize()` 合并被拆碎的文本节点。
- 输入法安全：`compositionstart ~ compositionend`（中文输入）期间不要改 DOM，否则输入被打断——这是 contenteditable 第一大坑。

```html
<div id="editor" contenteditable="true">选中一些文字试试</div>
<button id="link">把选区变成链接</button>
<button id="hl">高亮选区</button>
<script>
const ed = document.getElementById('editor');
const scheduleSave = (html) => console.log('防抖保存', html.length);

// 1) 读取当前选区：Selection 可能含多个 Range，编辑器取第一个
const sel = () => document.getSelection();
const range = () => (sel().rangeCount ? sel().getRangeAt(0) : null);

document.getElementById('link').onclick = () => {
  const r = range();
  if (!r || r.collapsed) return;
  const a = document.createElement('a');
  a.href = 'https://example.com';
  try {
    r.surroundContents(a);        // 选区跨节点时会抛错
  } catch {
    a.appendChild(r.extractContents());   // 兜底：摘出片段再包裹
    r.insertNode(a);
  }
  sel().removeAllRanges();
};

// 2) 高亮：mark 包裹，跨元素时 extract 再 insert
document.getElementById('hl').onclick = () => {
  const r = range();
  if (!r || r.collapsed) return;
  const mark = document.createElement('mark');
  mark.appendChild(r.extractContents());
  r.insertNode(mark);
  ed.normalize();                 // 合并被拆碎的文本节点
  sel().collapseToEnd();          // 光标移到插入内容之后
};

// 3) 输入法安全：composition 期间不要改 DOM，否则中文输入被打断
ed.addEventListener('compositionstart', () => (ed.dataset.lock = '1'));
ed.addEventListener('compositionend', () => delete ed.dataset.lock);
ed.addEventListener('input', () => {
  if (ed.dataset.lock) return;    // 组合期间只记录不处理
  scheduleSave(ed.innerHTML);
});

// execCommand('bold') 一行搞定但已废弃且行为不可控；
// 现代做法是以上 Range 操作，产品级富文本用 ProseMirror/Lexical 自持数据模型
</script>
```
