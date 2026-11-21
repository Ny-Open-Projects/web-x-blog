---
title: [TS-132] defineEmits 的类型签名怎么写？事件名与 payload 如何联动？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-132：defineEmits 的类型签名怎么写？事件名与 payload 如何联动？
**答**：
- 写法一：调用签名（经典，全 3.x 兼容），一个事件一条 `(e: "name", payload: T): void`。
- 写法二：命名元组语法（Vue 3.3+），`change: [value: string]`，更简洁、编辑器提示更友好。
- emit 调用点事件名、参数个数、参数类型全部联动校验，写错直接编译报错。

```typescript
// 写法一：调用签名
const emit = defineEmits<{
  (e: "change", value: string): void;
  (e: "submit", payload: { id: number; ok: boolean }): void;
  (e: "update:modelValue", v: string): void;
}>();

emit("change", "a");
// emit("change", 1);  // 报错：payload 必须是 string
// emit("nope");       // 报错：事件名不在允许范围内

// 写法二：命名元组语法（Vue 3.3+）
const emit2 = defineEmits<{
  change: [value: string];
  submit: [payload: { id: number; ok: boolean }];
}>();
emit2("submit", { id: 1, ok: true });
```
