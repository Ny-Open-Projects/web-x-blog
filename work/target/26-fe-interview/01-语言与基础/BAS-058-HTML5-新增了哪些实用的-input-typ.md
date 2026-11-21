---
title: [BAS-058] HTML5 新增了哪些实用的 input type？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-058：HTML5 新增了哪些实用的 input type？
**答**：
- email、url、number、tel、search：移动端弹对应键盘，email/url 还触发原生格式校验。
- date、time、datetime-local、month：原生日期选择器，省去第三方组件。
- range、color、file：滑块、取色器、多文件上传；配合 min/max/step/pattern/required 做约束校验，非法时浏览器原生拦截提交。

```html
<form>
  <input type="email" required placeholder="邮箱" />
  <input type="number" min="1" max="100" step="1" />
  <input type="date" />
  <input type="range" min="0" max="100" />
  <input type="color" />
  <input type="text" pattern="[0-9]{6}" title="六位数字" />
  <button>提交</button>
</form>
```
