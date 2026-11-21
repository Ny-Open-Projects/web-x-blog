---
title: [H5-158] execCommand 为什么废弃？现代替代路径是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-158：execCommand 为什么废弃？现代替代路径是什么？
**答**：
- execCommand 是"浏览器内置编辑命令"（bold/insertHTML/undo），无规范、跨浏览器行为不一致、不可定制数据模型，已被标记 deprecated（短期仍可用）。
- 它唯一的价值：免费获得**原生 undo/redo 栈**（尤其 `insertText`），过渡期轻量场景仍划算。
- 现代替代 1：小需求——Range/Selection 手工操作 + 自己管理 undo；替代 2：产品级——ProseMirror/Slate/Lexical 这类"自持文档模型"编辑器，DOM 只是投影，协作/撤销建立在模型上。
- 面试口径：只做"能打字+少量样式"用 execCommand/Range 够用；要 schema、协同、版本必须自持模型。

```html
<div id="ed" contenteditable="true">execCommand 的定位与现代替代</div>
<script>
// execCommand：浏览器内置编辑命令，无标准、行为不一致、不可扩展（已废弃但短期可用）
const ed = document.getElementById('ed');

// 仍可用的场景（过渡期）：纯文本/轻量编辑 —— 免费获得原生 undo 栈
function insertText(text) {
  document.execCommand('insertText', false, text);   // 保留原生 undo/redo！
}

// 现代替代 1：Range/Selection 手工操作 + 自己管理历史
const undoStack = [];
function boldByRange() {
  const sel = document.getSelection();
  const r = sel.getRangeAt(0);
  const b = document.createElement('strong');
  b.appendChild(r.extractContents());
  r.insertNode(b);
  sel.collapseToEnd();
  undoStack.push({ type: 'wrap', node: b });   // 自己记历史
}

// 现代替代 2：数据模型优先的编辑器（ProseMirror / Slate / Lexical）
// 共同思想：文档是受 schema 约束的数据结构，DOM 只是投影；
// 变更走事务（transaction），协作（OT/CRDT）建立在模型而非 DOM 上
const modelDoc = {
  type: 'doc',
  content: [
    { type: 'paragraph',
      content: [{ type: 'text', text: 'hello', marks: [{ type: 'strong' }] }] },
  ],
};
// 加粗 = 模型上的 mark 操作 —— 可序列化、可协作、可做版本 diff

// 面试口径：
// 1) 轻量编辑 → execCommand/Range 够用，记住它是遗产 API
// 2) 要 schema/协同/版本 → 必须自持模型编辑器
// 3) 中间态：contenteditable=false 嵌入块（@提及、卡片）用 Range 逻辑单独处理
</script>
```
