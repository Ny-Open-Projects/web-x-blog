---
title: [H5-152] 受控表单（React/Vue）与原生校验如何协作？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-152：受控表单（React/Vue）与原生校验如何协作？
**答**：
- 两条路线：**完全托管**（novalidate + 自研规则库，UI 可控但要重造规则与无障碍）与**混合**（保留 required/pattern/type 等原生约束，JS 读取 `validity` 渲染自定义 UI）。
- 推荐混合：规则声明在 HTML（可序列化、渐进增强），展示层用 `:user-invalid`/`:user-valid` 伪类渲染错误态，不写 JS 也基本工作。
- 关键 API：`checkValidity()` 汇总校验、`reportValidity()` 触发原生气泡、`setCustomValidity()` 把异步/跨字段校验结果写回原生体系。
- `novalidate` 只是关掉"提交时自动拦截"，validity 状态与伪类依旧工作——这是"托管 UI 但保留原生语义"的开关。

```html
<form id="signup" novalidate>
  <input name="email" type="email" required
         autocomplete="email" placeholder="邮箱">
  <input name="pwd" type="password" required minlength="8"
         autocomplete="new-password" placeholder="密码">
  <p class="err" id="err"></p>
  <button>注册</button>
</form>
<style>
  /* 原生约束仍然生效，样式层用伪类渲染错误态（无 JS 也工作） */
  input:user-invalid { border-color: #ef4444; }
  input:user-valid   { border-color: #10b981; }
</style>
<script>
const form = document.getElementById('signup');
const err = document.getElementById('err');

// 混合模式：规则交给 HTML（required/minlength/type），展示与提交交给 JS
form.addEventListener('submit', (e) => {
  e.preventDefault();                       // novalidate 后提交拦截由我们接管
  if (!form.checkValidity()) {
    const first = form.querySelector(':invalid');
    err.textContent = humanize(first);      // 自定义文案，覆盖浏览器默认气泡
    first.focus();
    return;
  }
  err.textContent = '';
  submit(new FormData(form));
});

// 异步/跨字段校验：结果仍写回原生体系，保持语义与无障碍一致
form.email.addEventListener('change', async (e) => {
  const taken = await checkEmailTaken(e.target.value);
  e.target.setCustomValidity(taken ? '该邮箱已注册' : '');
});

function humanize(input) {
  const v = input.validity;
  if (v.valueMissing) return '请填写' + (input.labels[0]?.textContent ?? '该项');
  if (v.typeMismatch) return '格式不正确';
  if (v.tooShort) return `至少 ${input.minLength} 个字符`;
  return input.validationMessage;           // 兜底用浏览器提供的消息
}
async function checkEmailTaken() { return false; }
function submit() {}
// 要点：novalidate 只关"提交时自动拦截"，validity 状态与伪类依旧工作；
// 完全自研（React 受控 + yup）适用于复杂联动场景，但要自己补无障碍与错误播报
</script>
```
