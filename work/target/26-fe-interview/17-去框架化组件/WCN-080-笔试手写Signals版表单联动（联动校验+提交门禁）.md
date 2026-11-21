---
title: [WCN-080] 笔试：手写 Signals 版表单联动（字段联动 + 提交门禁）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-080：笔试：手写 Signals 版表单联动

**题目**：注册表单场景：字段 `username/password/confirm/agree` 均为 signal；① confirm 仅在 password 触发过 blur 后开始校验（touched signal）；② 错误信息 computed：confirm 与 password 不一致显示文案；③ `canSubmit` computed：全部无错且 agree 为 true；④ 用户名异步查重（防抖 signal 输入）；⑤ 提交按钮 disabled 绑定 canSubmit。

**答**：

```javascript
import { createSignal, computed, effect } from './mini.js';
import { debouncedSignal } from './w74.js';

export function createSignupForm() {
  const [username, setUsername] = createSignal('');
  const [password, setPassword] = createSignal('');
  const [confirm, setConfirm] = createSignal('');
  const [agree, setAgree] = createSignal(false);
  const [pwTouched, setPwTouched] = createSignal(false);

  // 字段级 computed：细粒度错误提示
  const pwError = computed(() =>
    pwTouched() && password().length < 8 ? '密码至少 8 位' : '');
  const confirmError = computed(() =>
    pwTouched() && confirm() !== password() ? '两次输入不一致' : '');

  // 异步查重：防抖 signal 驱动（复用 WCN-074）
  const debouncedName = debouncedSignal(username, 400);
  const [taken, setTaken] = createSignal(false);
  effect(() => {
    const name = debouncedName();
    if (!name) { setTaken(false); return; }
    fetch(`/api/user/exists?name=${encodeURIComponent(name)}`)
      .then((r) => r.json()).then(({ exists }) => setTaken(exists));
  });
  const nameError = computed(() => taken() ? '用户名已被占用' : '');

  // 提交门禁：所有错误为空 + 勾选协议
  const canSubmit = computed(() =>
    !pwError() && !confirmError() && !nameError() && agree() && password().length > 0);

  return {
    username, setUsername, password, setPassword, confirm, setConfirm,
    agree, setAgree, setPwTouched,
    pwError, confirmError, nameError, canSubmit,
  };
}
// UI 侧：effect(() => btn.disabled = !form.canSubmit()); 无 diff 直改
```

**评分点**：
- touched 语义：blur 前不显示校验（用户体验口径）。
- computed 链分层：字段错误 → canSubmit，相等短路避免无谓联动。
- 异步查重走防抖 signal，竞态由 resource/seq 处理（答出思路即可）。
- canSubmit 汇聚所有 computed 结果，按钮直绑（无重渲染）。
