---
title: [H5-060] pattern 属性怎么用？它和 :invalid 伪类如何联动？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-060：pattern 属性怎么用？它和 :invalid 伪类如何联动？
**答**：
- `pattern` 只作用于 `text/search/tel/url/email/password` 等**文本类** input，值是 JS 正则字面量（**不加斜杠**），隐式锚定全匹配（等价 `^(?:pattern)$`）。
- 校验失败时控件进入 `:invalid`，配合 `:user-invalid`（用户实际交互过才触发）可以避免"页面一打开满屏红"。
- `title` 属性是失败提示的补充文案（部分浏览器在原生气泡中展示），同时给悬停用户解释规则。
- 中文场景注意：pattern 匹配基于整个 value，且 `u` 标志生效，中文类字符类 `[\u4e00-\u9fa5]` 可用。
- 联动链：`required` 先判空 → `pattern` 判格式 → `minlength/maxlength` 判长度 → 自定义 `setCustomValidity` 判业务。

```html
<style>
  /* 未交互时不吓人：user-invalid 只在用户输入过且非法时变红 */
  input:user-invalid {
    border-color: #d33;
    background: #fee;
  }
  input:valid { border-color: #3c3; }
</style>

<form>
  <!-- 4-16 位字母数字下划线用户名：正则不加斜杠 -->
  <label>用户名
    <input name="username" required
           pattern="[A-Za-z0-9_]{4,16}"
           title="4 到 16 位字母、数字或下划线">
  </label>

  <!-- 手机号：允许 +86 前缀 -->
  <label>手机号
    <input name="phone" required
           pattern="(?:\+86)?1[3-9]\d{9}"
           title="请输入 11 位手机号，可带 +86">
  </label>

  <button>提交</button>
</form>

<script>
  // :invalid 也能在 JS 里编程查询，用于提交前预检
  const form = document.querySelector('form');
  form.addEventListener('submit', (e) => {
    const bad = [...form.elements].filter(el => el.matches(':invalid'));
    console.log('非法字段：', bad.map(el => el.name)); // 提交被阻断时触发
    if (bad.length) e.preventDefault();
  });
</script>
```
