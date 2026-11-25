---
title: [WCN-631] 在复杂表单场景中如何用 Signals 做字段联动与校验？相较受控组件有何优劣？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-631：在复杂表单场景中如何用 Signals 做字段联动与校验？相较受控组件有何优劣？

**答**：
- 结论：Signals 把每个字段建成独立 signal，联动规则用 effect 监听依赖字段，校验结果也存 signal——天然细粒度，改一个字段不重渲染整表。
- 做法：字段 signal + computed 派生校验错误 + effect 处理跨字段联动（如「确认密码」依赖「密码」）。
- 追问钩子：与受控组件比劣势在哪？调试时数据流更分散（无单一 state 快照），需要配套的 devtools 才能观测——考察客观利弊。

```javascript
const form = {
  pwd: signal(''),
  confirm: signal(''),
};
const confirmError = computed(() => {
  const a = form.pwd.get(), b = form.confirm.get();
  return a === b ? '' : '两次密码不一致';
});
const canSubmit = computed(() =>
  form.pwd.get().length >= 8 && !confirmError.get());
effect(() => {
  const err = confirmError.get();
  document.querySelector('#err').textContent = err;
});
effect(() => {
  document.querySelector('#submit').disabled = !canSubmit.get();
});
form.confirm.set('1234'); // 只更新错误提示与提交按钮，其他字段无感
```
