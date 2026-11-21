---
title: [DP-277] 源码识别：React Hook Form 源码中的非受控订阅模型？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-277：源码识别：React Hook Form 源码中的非受控订阅模型？
**答**:
- 非受控收集：RHF 默认不接管 input value（uncontrolled，ref 收集）——React 状态树与表单数据解耦，性能核心（对比 DP-212 受控模型）。
- 观察者（按需订阅）：useFormState({ name }) 精确订阅指定字段状态，字段错误变化只重渲染订阅者。
- 备忘录：错误/校验结果缓存（字段未变不重校验），dirty/touched 集合位图式维护。
- 识别要点：能说清"非受控 + 订阅"为什么快——输入不打 React 状态，只有提交/校验时读 DOM。

```tsx
// React Hook Form 心智模型
const { register, handleSubmit, formState } = useForm();   // 注册器
<form onSubmit={handleSubmit(onValid)}>
  <input {...register('email', { required: true })}/>       // 非受控：ref 注册进 store
  <input {...register('age', { valueAsNumber: true })}/>
</form>
// 内部 store：
class RHFStore {
  fields = new Map();        // name → { ref, rules }
  errors = new Map();
  subscribe(name, cb) { /* 字段级订阅 */ }
  async validateField(name) {
    if (this.errors.has(name) && !this.isDirty(name)) return this.errors.get(name);  // 备忘录
    const ref = this.fields.get(name).ref;   // 读 DOM（非受控核心）
    const err = runRules(ref.value, this.fields.get(name).rules);
    this.errors.set(name, err); this.notify(name);   // 只通知订阅该字段的组件
  }
}
```
