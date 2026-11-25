---
title: [R19-364] React19 表单体系：form action 与 useActionState
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 表单]
type: 面试题
---

## R19-364：React19 表单体系：form action 与 useActionState

**答**：
- form action 三态：client 函数（onSubmit 语义）、server fn（RPC）、URL（原生渐进增强）——React 19 统一封装：自动 FormData 序列化 + pending 管理
- useActionState(actionFn, initialState)：包装 action——返回 [state, formAction, isPending]；state 是上次 action 的返回值（服务端校验错误回传的通道）
- useOptimistic：表单内的乐观值（提交即刻显示，server 返回后校正）——pending 期间 UI 先行动作，与 useActionState 组合成完整乐观表单
- formStatus/useFormStatus：嵌套在 form 内的组件读取提交状态（submit 按钮 pending/disabled）——无需 prop 钻取
- 深水点：action 的封装 dispatch——React 用 hidden field 注入 action id（no-JS 场景仍可 POST 到服务器路由），这是渐进增强的实现细节

```jsx
function Signup() {
  const [state, formAction, isPending] = useActionState(async (prev, fd) => {
    const r = await signupAction(fd);            // server fn
    return r.errors ?? { ok: true };
  }, { ok: false });
  return (
    <form action={formAction}>
      <input name="email" type="email" required />
      <SubmitBtn />                               {/* useFormStatus 读 pending */}
      {state.errors && <p>{state.errors.email}</p>}
    </form>
  );
}
```
