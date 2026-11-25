---
title: [R19-431] 笔试：手写 useForm（React19 action 风格）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 表单]
type: 笔试题
---

## R19-431：笔试：手写 useForm

**答**：实现 useActionState 风格 hook：① `useForm(action, initialState)` 返回 [state, formAction, isPending]；② formAction 接 FormData 自动传给 action(prev, formData)；③ isPending 由 transition 包裹；④ 错误回传：action 返回 { errors } 时 state 更新（服务端校验错误的展示通道）；⑤ useOptimistic 集成示例（提交乐观显示）。写出实现。

```javascript
function useFormState(action, initialState) {
  const [state, setState] = useState(initialState);
  const [isPending, startTransition] = useTransition();

  const formAction = (formData) => {
    startTransition(async () => {                    // 提交走低优
      try {
        const result = await action(state, formData);
        setState(result ?? state);                   // 服务端结果回传
      } catch (e) {
        setState({ errors: { _global: String(e) } });
      }
    });
  };
  return [state, formAction, isPending];
}

// 完整用法: 注册表单
function Signup() {
  const [state, formAction, isPending] = useFormState(async (prev, fd) => {
    'use server';
    const r = await api.signup(Object.fromEntries(fd));
    return r.errors ?? { ok: true };
  }, { ok: false });

  const [optimisticEmail, addOptimistic] = useOptimistic(state.email ?? '');

  return (
    <form action={formAction}>
      <input name="email" type="email" required />
      <button disabled={isPending}>{isPending ? '提交中...' : '注册'}</button>
      {state.errors?.email && <p role="alert">{state.errors.email}</p>}
    </form>
  );
}
```

**评分点**：
- action(prev, formData) 签名与 state 回传链
- transition 包裹的 isPending 语义
- 错误回传通道（{ errors } 结构）与 role=alert
- useOptimistic 与表单提交的组合
