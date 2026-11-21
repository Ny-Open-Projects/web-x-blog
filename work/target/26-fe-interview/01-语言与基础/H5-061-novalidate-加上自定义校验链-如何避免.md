---
title: [H5-061] novalidate 加上自定义校验链，如何避免原生气泡"抢戏"？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-061：novalidate 加上自定义校验链，如何避免原生气泡"抢戏"？
**答**：
- `novalidate`（写在 form 上）只关掉**提交时的自动校验与气泡**，不删控件上的约束属性——`validity` 状态和 `:invalid` 样式照常工作。
- 标准链路：监听 `submit` → `e.preventDefault()` 永远接管 → 逐字段跑业务校验 → 自己渲染错误 → 全过才真正提交。
- 错误展示与 a11y：给控件设 `aria-invalid="true"`，错误文本节点用 `aria-describedby` 关联，焦点移到第一个错误字段。
- 逐字段也可以不 novalidate、只在 `invalid` 事件里 `e.preventDefault()` 抑制气泡（form 级监听，capture 冒泡均可）。
- 取舍：完全接管（UI 统一、可控性强）vs 半接管（保留原生能力，仅改文案）。

```html
<form id="signup" novalidate>
  <label>邮箱 <input name="email" type="email" required></label>
  <p class="err" data-err-for="email"></p>

  <label>密码 <input name="pwd" type="password" required minlength="8"></label>
  <p class="err" data-err-for="pwd"></p>

  <button>注册</button>
</form>

<script>
  const form = document.getElementById('signup');
  const rules = {
    email: v => !v ? '邮箱必填'
      : (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v) ? '邮箱格式不正确' : ''),
    pwd: v => v.length < 8 ? '密码至少 8 位' : '',
  };

  function validateField(input) {
    const msg = rules[input.name](input.value);
    const errEl = form.querySelector(`[data-err-for="${input.name}"]`);
    errEl.textContent = msg;
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    input.setAttribute('aria-describedby', errEl.id ||= `err-${input.name}`);
    return !msg;
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();                            // novalidate 下完全接管
    const inputs = [...form.elements].filter(el => rules[el.name]);
    const ok = inputs.map(validateField).every(Boolean);
    if (ok) return fetch('/api/signup', { method: 'POST', body: new FormData(form) });
    inputs.find(i => i.matches('[aria-invalid="true"]')).focus(); // 聚焦第一个错误
  });

  // 失焦即时校验，输入时清除错误
  form.addEventListener('blur', e => rules[e.target.name] && validateField(e.target), true);
  form.addEventListener('input', e => {
    if (e.target.getAttribute('aria-invalid') === 'true') validateField(e.target);
  });
</script>
```
