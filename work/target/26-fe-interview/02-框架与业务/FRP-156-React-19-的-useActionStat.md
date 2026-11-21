---
title: [FRP-156] React 19 的 useActionState 与 useFormStatus 的实现原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-156：React 19 的 useActionState 与 useFormStatus 的实现原理是什么？

**答**：
- `useActionState(action, initialState)` 内部是 **reducer + pending 标记**的组合：提交时 React 包一层 wrapper action——先置 pending、把 prevState 作为第一参传给 action、返回值 setState。
- 它就是 `useReducer` + `useTransition` 的语法糖：`[state, dispatch, isPending]`，dispatch 由表单 submit/按钮 formAction 触发。
- `useFormStatus` 是 **Context 订阅**：`<form>` 内部把 `{ pending, data }` 放进 form 专属 context，子组件用 hook 读取——所以必须在 form **内部**使用才有效。
- 渐进增强：表单 action 在 JS 加载前也能提交（服务端处理），hydrate 后自动升级为客户端路径——action 引用是序列化的。

```javascript
// 简化实现，帮助理解 useActionState / useFormStatus
function useActionState(action, initialState) {
  const [state, setState] = useState(initialState);
  const [isPending, startTransition] = useTransition();

  // 包一层：这是"action 变成状态更新"的核心
  const wrappedAction = async (payload) => {
    startTransition(async () => {
      const result = await action(state, payload); // prevState 作为第一参！
      setState(result);                            // 返回值成为新 state
    });
  };
  return [state, wrappedAction, isPending];
}

// 表单集成：
// <form action={wrappedAction}> 提交时 React 调 wrappedAction(FormData)
// 服务端版（'use server' 函数）：同一包装逻辑跑在服务端，state 经序列化返回

function useFormStatus() {
  // form 组件在提交时更新 context；这里只是消费
  const status = useContext(FormStatusContext);
  if (status === null) throw new Error('useFormStatus 必须在 <form> 内使用');
  return status; // { pending, data } —— data 是提交中的 FormData
}

// —— form 侧的简化实现 ——
const FormStatusContext = createContext(null);
function Form({ action, children }) {
  const [status, setStatus] = useState({ pending: false, data: null });
  const submit = async (formData) => {
    setStatus({ pending: true, data: formData });   // 子组件立刻能读到 pending
    await action(formData);
    setStatus({ pending: false, data: null });
  };
  return (
    <FormStatusContext.Provider value={status}>
      <form action={submit}>{children}</form>
    </FormStatusContext.Provider>
  );
}

// 组合使用：
// <form action={formAction}>
//   <SubmitButton />   内部 useFormStatus().pending -> 按钮自动禁用
// </form>
```
