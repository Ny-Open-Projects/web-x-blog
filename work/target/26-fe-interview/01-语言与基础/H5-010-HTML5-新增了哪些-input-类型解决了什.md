---
title: [H5-010] HTML5 新增了哪些 input 类型？解决了什么问题？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-010：HTML5 新增了哪些 input 类型？解决了什么问题？
**答**：
- `email`、`url`、`tel`、`number`、`range`、`date/time/month`、`color`、`search` 等。
- 收益一：移动端自动唤起对应键盘（email 出 @、tel 出数字拨号盘）；收益二：原生格式校验。
- `number` 配 `min/max/step` 约束，`range` 原生滑杆，`color` 原生取色器，减少 JS 与第三方组件。
- 兼容性兜底：不识别的类型默认按 text 渲染，不会报错。

```html
<form>
  <!-- 移动端唤起邮箱键盘并校验格式 -->
  <input type="email" name="email" placeholder="邮箱" required />

  <!-- 数字约束：1~10 步进 0.5，非法值提交时被浏览器拦截 -->
  <input type="number" name="rating" min="1" max="10" step="0.5" />

  <!-- 原生滑杆与取色器 -->
  <input type="range" name="volume" min="0" max="100" value="50" />
  <input type="color" name="theme" value="#3367d6" />

  <!-- 原生日期选择，替代大部分第三方日历 -->
  <input type="date" name="birthday" min="1900-01-01" />

  <button type="submit">提交</button>
</form>
```
