---
title: [H5-058] input 的 form 属性有什么用？什么场景必须跨表单关联？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-058：input 的 form 属性有什么用？什么场景必须跨表单关联？
**答**：
- `form` 属性让**游离于 form 标签之外**的控件归属某个表单：提交、校验、reset 全部纳入该表单。
- 典型场景：模态框里的提交按钮在 `dialog` 中、表格每行有独立按钮、布局被设计拆散的表单（表头一条、表尾一条）。
- 支持该属性的控件：`input`、`select`、`textarea`、`button`、`output`、`fieldset` 等；`form="formId"` 写 id。
- 提交时游离控件的数据**会**一起序列化；`formmethod/formaction` 还能在按钮级覆盖表单行为。
- 代价：DOM 关系与逻辑关系分离，代码可读性下降，务必加注释或让控件物理上靠近。

```html
<form id="order" action="/api/order" method="post">
  <input name="sku" required placeholder="商品编号">
  <!-- 下面的提交按钮在 dialog 里，通过 form 属性关联 -->
  <button type="submit" form="order">提交订单</button>
</form>

<!-- 游离输入框：不在 form 标签内，但数据会随 #order 提交 -->
<label for="remark">备注（物理上位于页面底部）</label>
<input id="remark" name="remark" form="order">

<dialog id="confirm-box">
  <p>确认提交该订单？</p>
  <!-- 按钮级覆盖：这个按钮以 GET 提到预览接口 -->
  <button type="submit" form="order" formmethod="get"
          formaction="/api/order/preview">预览</button>
  <button type="button" onclick="document.getElementById('confirm-box').close()">
    取消
  </button>
</dialog>
```
