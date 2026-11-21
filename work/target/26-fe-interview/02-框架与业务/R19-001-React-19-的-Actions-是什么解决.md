---
title: [R19-001] React 19 的 Actions 是什么？解决了什么问题？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-001：React 19 的 Actions 是什么？解决了什么问题？
**答**：
- Actions 是 React 19 对"数据变更"的一揽子声明式方案，覆盖表单提交、pending 状态、错误处理与乐观更新。
- 传统写法需要手动维护 isSubmitting、error 等状态；Actions 让 React 自动跟踪异步函数的执行过程。
- 表单可以直接把异步函数传给 `action` prop，提交成功后 React 会自动重置非受控表单。
- 配套 API：useActionState、useFormStatus、useOptimistic。

```jsx
function UpdateNameForm() {
  const [isPending, startTransition] = useTransition();

  const handleSubmit = (formData) => {
    // 把异步函数放进 startTransition 即构成一个 Action
    startTransition(async () => {
      const error = await updateName(formData.get('name'));
      if (error) {
        alert(error);
        return;
      }
      // 成功后 React 自动重置表单，无需手动清空输入框
    });
  };

  return (
    <form action={handleSubmit}>
      <input name="name" disabled={isPending} />
      <button disabled={isPending}>{isPending ? '更新中' : '更新'}</button>
    </form>
  );
}
```
