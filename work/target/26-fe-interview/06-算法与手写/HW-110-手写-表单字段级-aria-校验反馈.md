---
title: [HW-110] 手写无障碍表单校验反馈——aria-invalid、aria-describedby 与错误播报
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：表单校验的无障碍三件套：① `aria-invalid="true"` 标记错误字段；② `aria-describedby` 指向错误消息元素（读屏软件读到字段描述+错误）；③ 错误消息用 `role="alert"`（或 aria-live="polite"）让读屏主动播报；④ focus 管理——提交失败聚焦第一个错误字段。

```javascript
function applyFieldError(input, msg) {
  input.setAttribute('aria-invalid', 'true');
  let errEl = document.getElementById(input.getAttribute('aria-describedby') || '');
  if (!errEl) {                                     // 动态创建错误元素
    errEl = document.createElement('p');
    errEl.id = `${input.id || input.name}-error`;
    errEl.className = 'field-error';
    errEl.setAttribute('role', 'alert');            // 读屏主动播报
    input.insertAdjacentElement('afterend', errEl);
    input.setAttribute('aria-describedby', errEl.id);
  }
  errEl.textContent = msg;
  input.setAttribute('aria-live', 'polite');
}
function clearFieldError(input) {
  input.removeAttribute('aria-invalid');
  const errEl = document.getElementById(input.getAttribute('aria-describedby') || '');
  if (errEl) errEl.textContent = '';                // 清内容但不删节点（aria-describedby 引用保持）
}
function focusFirstError(formEl) {
  const first = formEl.querySelector('[aria-invalid="true"]');
  if (first) { first.focus(); first.scrollIntoView({ block: 'center' }); }
}
// 提交流程：
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const errs = validate(form);                      // { name: '必填', ... }
  for (const [name, msg] of Object.entries(errs)) applyFieldError(form.elements[name], msg);
  for (const el of form.querySelectorAll('[aria-invalid="true"]')) clearFieldError(el); // 先清旧错
  Object.entries(errs).forEach(([n, m]) => applyFieldError(form.elements[n], m));
  if (Object.keys(errs).length) focusFirstError(form); else form.submit();
});
```

**评分点**：
- aria-invalid / aria-describedby / role=alert 三件套语义正确（读屏可感知）。
- 先清后设防旧错误残留；错误节点复用（不重复创建）。
- focusFirstError：提交失败聚焦第一个错误并滚动到视口。
- 不依赖 color-only 错误提示（有文本 + aria）的意识。
