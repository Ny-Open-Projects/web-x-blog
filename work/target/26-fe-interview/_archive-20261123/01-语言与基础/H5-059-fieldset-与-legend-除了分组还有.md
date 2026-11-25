---
title: [H5-059] fieldset 与 legend 除了分组还有哪些实战价值？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-059：fieldset 与 legend 除了分组还有哪些实战价值？
**答**：
- `fieldset` 给一组相关控件建立语义分组，`legend` 是分组的**唯一标题**，读屏进入分组时会先播报 legend，比 div + h3 强。
- 超实用副作用：**禁用整个分组**——`fieldset disabled` 后内部全部控件不可交互、不参与提交、不被 tab 到，一行搞定"地址类型切换"。
- 单选按钮组天然适合 fieldset：读屏用户能听到"支付方式"这个上下文，而不是一串孤立的 radio。
- fieldset 参与 form 关联（也有 form 属性），且可嵌套；legend 内放链接等流内容合法但建议保持纯文本。
- 样式上 fieldset 默认边框可 `border: 0` 重置，legend 借 `float: left` 等技巧可实现"穿越边框"效果。

```html
<form>
  <!-- 单选组：legend 提供提问上下文 -->
  <fieldset>
    <legend>支付方式</legend>
    <label><input type="radio" name="pay" value="wx" checked>微信</label>
    <label><input type="radio" name="pay" value="alipay">支付宝</label>
  </fieldset>

  <!-- 一键禁用整组：发票信息未启用 -->
  <fieldset disabled>
    <legend>发票信息（暂不可用）</legend>
    <input name="invoice-title" placeholder="发票抬头">
    <input name="invoice-no" placeholder="税号">
  </fieldset>

  <!-- JS 动态启停：切配送方式时整组可用性联动 -->
  <button type="button" id="toggle-invoice">启用发票填写</button>
</form>

<script>
  document.getElementById('toggle-invoice').addEventListener('click', (e) => {
    const fs = e.currentTarget.previousElementSibling;
    fs.disabled = !fs.disabled;                 // 整组控件同时启用/禁用
  });
</script>
```
