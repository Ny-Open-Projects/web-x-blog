---
title: [MFW-055] useActionState 怎么做表单提交与错误回显？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-055：useActionState 怎么做表单提交与错误回显？
**答**：
- 签名：`const [state, formAction, pending] = useActionState(fn, initialState)`，fn 变成 `(prevState, formData) => next`，上一个返回值会回传，因此服务端校验失败时能带错误信息回来直接渲染。
- 服务端返回结构建议固定为 `{ ok, errors, values }`，错误对象按字段组织，客户端逐字段显示；同时回填用户已填的值避免全清空。
- 与 useFormStatus 组合：状态用 useActionState 管，按钮 pending 用 useFormStatus 管，各司其职。
- 注意错误不要直接 throw 到客户端（生产环境会被脱敏），业务错误走返回值。

```tsx
'use client';
import { useActionState } from 'react';
import { submitProfile } from './actions';

type State = {
  ok: boolean;
  errors: Record<string, string>;
  values: Record<string, string>;
};
const initial: State = { ok: false, errors: {}, values: {} };

export default function ProfileForm() {
  const [state, formAction, pending] = useActionState(submitProfile, initial);
  return (
    <form action={formAction}>
      <input name="nickname" defaultValue={state.values.nickname} />
      {state.errors.nickname && <p>{state.errors.nickname}</p>}

      <input name="email" defaultValue={state.values.email} />
      {state.errors.email && <p>{state.errors.email}</p>}

      <button disabled={pending}>{pending ? '保存中…' : '保存'}</button>
      {state.ok && <p>已保存</p>}
    </form>
  );
}
```

```ts
// actions.ts
'use server';
export async function submitProfile(prev: State, fd: FormData): Promise<State> {
  const values = { nickname: String(fd.get('nickname') ?? ''), email: String(fd.get('email') ?? '') };
  const errors: Record<string, string> = {};
  if (!values.nickname.trim()) errors.nickname = '昵称不能为空';
  if (!/^[\w.]+@\w+\.\w+$/.test(values.email)) errors.email = '邮箱格式不正确';
  if (Object.keys(errors).length) return { ok: false, errors, values }; // 回显+回填
  await db.user.update({ where: { id: (await auth()).userId }, data: values });
  return { ok: true, errors: {}, values };
}
```
