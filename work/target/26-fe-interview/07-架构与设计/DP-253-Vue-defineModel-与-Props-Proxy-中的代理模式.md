---
title: [DP-253] 源码识别：Vue defineModel 与 Props 代理模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-253：源码识别：Vue defineModel 与 Props 代理模式？
**答**:
- 代理模式：defineModel 返回的 ref 是"父子通信的代理"——读走 props、写 emit update:modelValue，双通道被收口为一个代理对象。
- 备忘录（props 浅层响应）：props 是响应式代理但浅层（深层性能差），toRefs 转换是"引用稳定性"处理。
- 命令（事件流）：v-model 展开为 :value + @input 命令对，defineModel 把这对命令封装——识别要点是"代理之下仍是单向数据流 + 事件命令"。
- 识别要点：能说出 defineModel 的守卫（父未传 props 时本地兜底）与"不代理就 muti props"的禁区。

```vue
<!-- 编译期展开 -->
<!-- <Child v-model="title"/> 等价于 -->
<!-- <Child :modelValue="title" @update:modelValue="v => title = v"/> -->
<script setup>
import { customRef } from 'vue';
// defineModel 源码心智：一个双向代理 ref
function useModel(props, name, emit) {
  return customRef((track, trigger) => ({
    get() { track(); return props[name]; },              // 读：props 通道
    set(v) { emit(`update:${name}`, v); trigger(); },    // 写：emit 命令通道
  }));
}
const model = defineModel({ default: '' });              // 守卫：父未绑定时用 default 本地值
model.value = 'x';                                       // → emit('update:modelValue', 'x')
</script>
```
