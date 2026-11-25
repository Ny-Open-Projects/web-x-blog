---
title: [V3-225] 编译器宏（defineProps/defineEmits）的编译期展开与类型推导是怎么做的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-225：编译器宏的编译期展开与 defineProps 类型推导是怎么做的？
**答**：
- 宏不是函数：编译期整体删除或替换，不会出现在运行时代码里，因此可以在顶层之外约束（如只能在 setup 中调用一次）。
- defineProps 运行时声明：对象字面量直接编译为 props 选项；**类型声明**走编译器类型推导——TS 类型注解转为运行时 props 声明（string→type: String）。
- 推导能力与边界：支持基础类型/字面量联合/可选标记/函数类型，无法解析的复杂类型（条件类型、外部 interface 的深层泛型）退化为 null 并给出编译警告。
- defineEmits/defineExpose/defineOptions/defineSlots 同理：编译期收集签名，注入组件选项。
- 双声明冲突：类型声明与运行时声明不能混用；需要默认值用 withDefaults（或 3.5 响应式解构默认值）。

```vue
<script setup lang="ts">
// 类型声明：编译器把它变成 { msg: { type: String, required: true }, count: Number }
const props = defineProps<{ msg: string; count?: number; cb: (id: number) => void }>();
// defineEmits 的类型编译为 emits: ['change', 'update:modelValue']
const emit = defineEmits<{ change: [val: string]; 'update:modelValue': [v: string] }>();
// 复杂类型退化示例：无法推导 → 仅类型层有效，运行时 null
// const props = defineProps<{ data: Result<ApiResponse> }>()
</script>
<!-- 编译产物（示意）：defineComponent({ props: { msg: {type:String,required:true}, count:Number, cb:Function }, emits: ['change','update:modelValue'], setup(props) {...} }) -->
```
