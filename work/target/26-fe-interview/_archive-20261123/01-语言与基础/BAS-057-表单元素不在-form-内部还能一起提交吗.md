---
title: [BAS-057] 表单元素不在 form 内部还能一起提交吗？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-057：表单元素不在 form 内部还能一起提交吗？
**答**：
- 可以：给表单元素加 `form="formId"` 属性即可关联任意表单，突破 DOM 嵌套结构限制。
- button/input 还支持 formaction、formmethod、formtarget，覆盖对应 form 属性，实现一个表单提交到不同接口。
- 弹窗、组件库场景常用：DOM 结构上分离，逻辑上仍是同一个表单。

```html
<form id="search" action="/search" method="get">
  <input name="q" />
</form>
<!-- 逻辑上属于 search 表单，但 DOM 在表单外面 -->
<input form="search" name="page" value="1" />
<button form="search" formmethod="post" formaction="/advanced">高级搜索</button>
```
