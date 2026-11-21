---
title: [H5-160] Range API 全解：创建、定位、删除、复制选区？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-160：Range API 全解：创建、定位、删除、复制选区？
**答**：
- 定位模型：`setStart/setEnd(容器, 偏移)`——偏移对文本节点是"字符位置"，对元素节点是"第几个子节点"，这是理解 Range 的根。
- 内容操作三兄弟：`deleteContents()`（删除区间、保留容器）、`extractContents()`（摘出成 DocumentFragment，剪切）、`cloneContents()`（复制不动原文档）；`insertNode()` 插入后常需 `normalize()` 合并碎文本。
- 与选区联动：`selection.removeAllRanges() + addRange(range)` 设置；`range.collapse()` 折叠成光标。
- 复制富文本到剪贴板：`ClipboardItem` 同时写 text/plain 与 text/html 双格式。

```html
<p id="para">Range API 可以精确描述文档中的一个片段。</p>
<script>
const p = document.getElementById('para');
const textNode = p.firstChild;

// 1) 创建与定位：偏移对文本节点是"字符"，对元素节点是"第几个子节点"
const r = document.createRange();
r.setStart(textNode, 0);        // 段落开头
r.setEnd(textNode, 5);          // 第 5 个字符后
console.log(r.toString());      // 'Range'（offset 5 不含第 6 个字符）

// 2) 选区交互：把 range 设为当前选区
const sel = document.getSelection();
sel.removeAllRanges();
sel.addRange(r);

// 3) 内容操作：deleteContents 清空区间保留容器；extractContents 摘出 fragment
// r.deleteContents();                    // 删除
// const frag = r.extractContents();      // 剪切：frag 可再插入别处
const div = document.createElement('div');
div.appendChild(r.cloneContents());      // 复制：不动原文档
console.log(div.innerHTML);

// 4) 插入节点：insertNode 后 normalize 合并碎文本节点，避免后续偏移错乱
const mark = document.createElement('mark');
mark.textContent = '[插]';
r.insertNode(mark);
p.normalize();

// 5) 复制选区到剪贴板：富文本走 ClipboardItem 双格式
async function copySelectionHTML() {
  const cur = sel.getRangeAt(0);
  const box = document.createElement('div');
  box.appendChild(cur.cloneContents());
  const item = new ClipboardItem({
    'text/plain': new Blob([cur.toString()], { type: 'text/plain' }),
    'text/html': new Blob([box.innerHTML], { type: 'text/html' }),
  });
  await navigator.clipboard.write([item]);
}

// 6) 其它常用：selectNodeContents、collapse 折叠成光标、
//    compareBoundaryPoints/comparePoint 判断"光标是否在某容器内"——编辑器最常用
</script>
```
