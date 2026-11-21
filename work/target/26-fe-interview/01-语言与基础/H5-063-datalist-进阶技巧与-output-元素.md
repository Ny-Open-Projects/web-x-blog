---
title: [H5-063] datalist 进阶技巧与 output 元素各自适合什么场景？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-063：datalist 进阶技巧与 output 元素各自适合什么场景？
**答**：
- `datalist` 是"**可输入的 select**"：input 保留自由输入，下拉只做候选提示；`select` 则强制取值。候选可来自 JS 动态生成。
- 实战：给候选加描述时部分浏览器支持 `label` 属性（显示为辅助文本）；数值/日期类型 input 配 datalist 可给刻度建议。
- `output` 承载**计算结果或用户操作的结果**，自带 `for` 属性声明参与计算的控件 id；读屏将其当结果区域播报。
- output 默认 `display: inline` 且是 live region 角色，JS 改 value（textContent）无需额外 aria-live。
- 两者搭配常见于"滑块选值 + 实时回显"或"输入拼音候选 + 计算结果"的组合。

```html
<form id="calc">
  <!-- datalist：输入色值候选，允许自由输入 -->
  <label>主题色
    <input list="palette" name="color" value="#1677ff">
  </label>
  <datalist id="palette">
    <option value="#1677ff" label="品牌蓝"></option>
    <option value="#52c41a" label="成功绿"></option>
    <option value="#fa8c16" label="警示橙"></option>
  </datalist>

  <!-- 滑块 + output 实时回显计算结果 -->
  <label>数量
    <input type="range" name="qty" min="1" max="10" value="1">
  </label>
  <label>单价
    <input type="number" name="price" value="9.9" min="0" step="0.1">
  </label>
  <output name="total" for="qty price">9.90</output>

  <button>下单</button>
</form>

<script>
  const form = document.getElementById('calc');
  const update = () => {
    const qty = form.elements.qty.valueAsNumber;
    const price = form.elements.price.valueAsNumber;
    form.elements.total.value = (qty * price).toFixed(2); // output 用 value 赋值
  };
  form.addEventListener('input', update);

  // datalist 候选动态化：搜索联想
  fetch('/api/hot-colors')
    .then(r => r.json())
    .then(list => {
      const dl = document.getElementById('palette');
      dl.replaceChildren(...list.map(c => new Option(c.name, c.hex)));
    });
</script>
```
