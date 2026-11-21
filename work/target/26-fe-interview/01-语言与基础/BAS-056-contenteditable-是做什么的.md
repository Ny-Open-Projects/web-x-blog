---
title: [BAS-056] contenteditable 是做什么的？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-056：contenteditable 是做什么的？
**答**：
- 让任意元素变成可编辑区域：`contenteditable="true"` 开启，是富文本编辑器的底层能力。
- 配合 Selection/Range API 实现加粗、插入内容等编辑操作（老的 document.execCommand 已废弃但仍在用）。
- 可编辑元素的子元素默认一起可编辑，用 `contenteditable="false"` 局部锁定（如 @提及标签、嵌入卡片）。

```html
<div contenteditable="true" id="editor">
  这里可以编辑 <span contenteditable="false">@某人</span> 锁定的提及不可改
</div>
<script>
  document.getElementById('editor').focus();
  console.log(document.activeElement.isContentEditable); // true
</script>
```
