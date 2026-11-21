---
title: [R19-084] 如何用 useFieldArray 实现动态表单？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-084：如何用 useFieldArray 实现动态表单？
**答**：
- useFieldArray 管理数组字段：append/remove/move/replace 全套操作，并自动维护 field.id。
- 渲染时 key 必须用 field.id 而不是 index：数组中间删行时，index 作 key 会导致输入串位。
- register 路径用模板串 `experiences.${index}.company`，RHF 自动收集成数组结构。
- 校验同样按路径写规则，也可配 Zod 的 array schema 一次校验整组。

```jsx
import { useFieldArray, useForm } from 'react-hook-form';

function ResumeForm() {
  const { control, register, handleSubmit } = useForm({
    defaultValues: { experiences: [{ company: '', years: 1 }] },
  });
  const { fields, append, remove, move } = useFieldArray({ control, name: 'experiences' });

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {fields.map((field, index) => (
        // key 必须用 field.id：useFieldArray 自动维护的唯一 id，增删不丢输入
        <fieldset key={field.id}>
          <input {...register(`experiences.${index}.company`)} placeholder="公司" />
          <input type="number" {...register(`experiences.${index}.years`)} />
          <button type="button" onClick={() => move(index, index - 1)}>上移</button>
          <button type="button" onClick={() => remove(index)}>删除</button>
        </fieldset>
      ))}
      <button type="button" onClick={() => append({ company: '', years: 1 })}>新增经历</button>
    </form>
  );
}
```
