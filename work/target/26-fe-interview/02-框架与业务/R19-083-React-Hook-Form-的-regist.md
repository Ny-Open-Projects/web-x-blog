---
title: [R19-083] React Hook Form 的 register、setValue、watch 怎么取舍？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-083：React Hook Form 的 register、setValue、watch 怎么取舍？
**答**：
- register 走非受控：输入值存在 DOM 里，每次敲键不触发 React 重渲染，这是 RHF 性能好的根本原因。
- watch 全量订阅会让本组件随每次输入重渲染，只在确实需要联动展示（如字数统计）时局部使用。
- 编程改值用 setValue，第三参控制是否触发校验（shouldValidate）与脏检查（shouldDirty）。
- 校验时机 mode: onBlur / onChange / onSubmit 按业务选，中后台推荐 onBlur 减少无效报错。

```jsx
import { useForm } from 'react-hook-form';

function ProfileForm() {
  const { register, setValue, watch, handleSubmit, formState } = useForm({
    defaultValues: { nickname: '', bio: '' },
    mode: 'onBlur',                       // 校验时机前移，减少无效请求
  });

  // watch 只订阅 bio：本组件会随 bio 输入重渲染，其他字段不受影响
  const bio = watch('bio');

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* register 走非受控：输入不触发 React 重渲染，大表单首选 */}
      <input {...register('nickname', { required: '昵称必填', maxLength: 20 })} />
      {formState.errors.nickname && <span>{formState.errors.nickname.message}</span>}

      <textarea {...register('bio')} />
      <span>{bio?.length ?? 0}/200</span>  {/* 字数联动，局部代价可接受 */}

      {/* 编程改值用 setValue，第二参控制是否触发校验与脏检查 */}
      <button type="button" onClick={() => setValue('bio', '默认简介', { shouldValidate: true })}>
        使用模板
      </button>
    </form>
  );
}
```
