---
title: [H5-013] datalist 是什么？和 select 有什么区别？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-013：datalist 是什么？和 select 有什么区别？
**答**：
- `datalist` 给 input 提供候选建议列表，用户既能选也能自由输入（select 只能选）；值仍是字符串。
- 常配合 `autocomplete` 关闭浏览器自带的自动填充，避免两套提示叠加。
- 适合"常见值提示 + 允许自定义"的场景（城市、标签）；选项多时体验一般，大数据量建议虚拟列表组件。

```html
<label for="city">所在城市</label>
<!-- input 绑定 datalist 的 id，输入时浮出候选 -->
<input id="city" name="city" list="city-list" autocomplete="off" />
<datalist id="city-list">
  <option value="北京"></option>
  <option value="上海"></option>
  <option value="杭州"></option>
</datalist>

<!-- 与 select 的核心差异：input 保留自由输入能力 -->
<label for="city2">自由输入版</label>
<input id="city2" name="city2" list="city-list" />
<!-- 用户可以输入"深圳"这样的列表外值 -->
```
