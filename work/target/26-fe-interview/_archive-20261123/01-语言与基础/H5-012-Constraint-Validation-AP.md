---
title: [H5-012] Constraint Validation API 如何实现自定义校验规则？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-012：Constraint Validation API 如何实现自定义校验规则？
**答**：
- 核心方法：`el.validity` 状态对象、`el.setCustomValidity(msg)` 设置自定义错误（非空串即视为非法）、`el.checkValidity()` 触发校验。
- 自定义规则套路：监听 input/change，业务校验不通过就 `setCustomValidity('错误原因')`，通过则 `setCustomValidity('')` 清除。
- 好处：复用原生提交拦截与 `:invalid` 样式体系；比完全自研校验库轻。
- 异步校验（重名检查）时先置 pending 消息防止提交，结果回来再更新。

```html
<form id="reg" novalidate>
  <input name="username" required minlength="4" />
  <button type="submit">提交</button>
  <p id="error" role="alert"></p>
</form>

<script>
  const form = document.getElementById('reg');
  const username = form.elements.username;
  const errorEl = document.getElementById('error');

  // 自定义规则：不能包含 admin 字样
  username.addEventListener('input', () => {
    if (username.value.includes('admin')) {
      username.setCustomValidity('用户名不能包含 admin'); // 非空 => validity.valid 为 false
    } else {
      username.setCustomValidity(''); // 必须显式清空，否则一直非法
    }
    errorEl.textContent = username.validationMessage;
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (username.checkValidity()) {
      console.log('提交:', username.value);
    }
  });

  // validity 对象细分了失败原因，可用于精细化提示
  console.log(username.validity.valueMissing); // required 未填时为 true
</script>
```
