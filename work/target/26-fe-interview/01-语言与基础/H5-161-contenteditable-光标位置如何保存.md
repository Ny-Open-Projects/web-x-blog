---
title: [H5-161] contenteditable 光标位置如何保存与恢复？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-161：contenteditable 光标位置如何保存与恢复？
**答**：
- 光标 = (容器节点, 偏移)。框架重渲染会重建 DOM，直接保存 Range 引用会失效——要**序列化成"树路径 + 偏移"**：从容器向上收集到根的子节点索引路径。
- 恢复：按路径重新定位容器 → `setStart/setEnd` → `removeAllRanges + addRange`；路径失效（DOM 被改）时返回 null 让调用方降级到"光标落开头/结尾"。
- 简易方案：同文档未重渲染时直接保存 Range 对象引用即可，编辑器内核（未走框架 vdom）常用这招。
- 红线：`compositionstart ~ end`（输入法组合）期间禁止恢复选区，否则中文输入被打断。

```html
<div id="ed" contenteditable="true">编辑后焦点离开再回来，光标应复原</div>
<script>
const ed = document.getElementById('ed');

// 光标位置 = (容器, 偏移)。框架重渲染会重建 DOM 节点，
// 保存 Range 引用会失效 —— 序列化成"树路径 + 偏移"
function serializePos(node, root) {
  const path = [];
  let cur = node;
  while (cur !== root) {
    const parent = cur.parentNode;
    path.unshift([...parent.childNodes].indexOf(cur));
    cur = parent;
  }
  return path;
}
function deserializePos(path, root) {
  let cur = root;
  for (const i of path) {
    cur = cur.childNodes[i];
    if (!cur) return null;      // 路径失效（DOM 被改）：调用方降级处理
  }
  return cur;
}

function saveSelection(root) {
  const sel = document.getSelection();
  if (!sel.rangeCount || !root.contains(sel.anchorNode)) return null;
  const r = sel.getRangeAt(0);
  return {
    startPath: serializePos(r.startContainer, root),
    startOffset: r.startOffset,
    endPath: serializePos(r.endContainer, root),
    endOffset: r.endOffset,
  };
}

function restoreSelection(root, saved) {
  if (!saved) return;
  const s = deserializePos(saved.startPath, root);
  const e = deserializePos(saved.endPath, root);
  if (!s || !e) return;
  const r = document.createRange();
  r.setStart(s, saved.startOffset);
  r.setEnd(e, saved.endOffset);
  const sel = document.getSelection();
  sel.removeAllRanges();
  sel.addRange(r);
}

// 用法：输入前存，重渲染后恢复（框架场景在 effect/nextTick 里恢复）
let saved = null;
ed.addEventListener('beforeinput', () => { saved = saveSelection(ed); });
// ...重新渲染 innerHTML 之后：
// restoreSelection(ed, saved);

// 注意事项：
// 1) compositionstart~end（中文输入法）期间禁止恢复选区，否则输入被打断
// 2) 未重渲染的简单场景可直接保存 Range 对象引用
// 3) 富文本框架里这一步由内核自动处理（模型 → 视图映射）
</script>
```
