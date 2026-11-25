---
title: [H5-015] label、fieldset 这些"不起眼"的表单元素为什么重要？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-015：label、fieldset 这些"不起眼"的表单元素为什么重要？
**答**：
- `label` 的 for 关联 input 后：点击文字聚焦输入框、读屏朗读控件名称，是 a11y 的基本盘；点击 label 会触发关联控件。
- `fieldset` + `legend` 给一组控件提供分组标题（如单选组），读屏用户可感知分组语义。
- 复选框用 `label` 包裹可以扩大点击热区，移动端体验明显更好。
- 隐藏 label 的场景必须保留可访问名称（如 `aria-label`），不能只留 placeholder。

```html
<!-- label 显式关联：for 与 input 的 id 对应 -->
<label for="email">邮箱</label>
<input id="email" name="email" type="email" />

<!-- label 隐式包裹：整块都可点击，移动端友好 -->
<label>
  <input type="checkbox" name="agree" />
  我已阅读并同意用户协议
</label>

<!-- fieldset 给一组单选提供分组语义 -->
<fieldset>
  <legend>支付方式</legend>
  <label><input type="radio" name="pay" value="wx" checked /> 微信支付</label>
  <label><input type="radio" name="pay" value="ali" /> 支付宝</label>
</fieldset>

<!-- 反例：没有 label，读屏只能念出"编辑框"，用户不知道该填什么 -->
<!-- <input type="text" placeholder="手机号" /> -->
```

## 三、媒体：audio 与 video
