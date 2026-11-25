---
title: [V3-471] 编译宏展开机制：defineProps/defineEmits 的类型到运行时
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-471：编译宏展开机制：defineProps/defineEmits 的类型到运行时

**答**：
- 宏的本质：编译期特判的「伪函数」——compileScript 识别这些调用并整体替换为运行时结构，宏不在产物中残留
- defineProps 运行时声明：对象字面量直接作为 props 选项；类型声明 `{ props: { msg: String } }` 用 TS 类型生成——类型声明走「类型 → 运行时 props」编译转换，复杂类型（联合/工具类型）需要外部 .d.ts 支持（纯本地解析）
- defineEmits 类型：`defineEmits<{ (e: 'change', v: string): void }>()` 编译为 emits 数组/对象——运行时只是校验声明，类型纯编译期
- defineExpose：编译为 `exposed` 对象——script setup 组件默认全封闭，expose 白名单控制 template ref 可见性
- 位置限制：宏必须在顶层、不可在条件分支/函数内——编译器位置校验（这与普通函数调用的根本区别）

```vue
<script setup lang="ts">
interface Props { msg: string; count?: number }
const props = defineProps<Props>();   // → props: { msg: String, count: Number }
const emit = defineEmits<{ (e: 'update', v: number): void }>();
// → emits: ['update']
defineExpose({ reset });              // → exposed: ['reset']
</script>
```
