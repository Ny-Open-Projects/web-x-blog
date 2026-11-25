---
title: [FRP-064] v-model 在编译后生成了什么代码？不同元素上为什么产物不同？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-064：v-model 在编译后生成了什么代码？不同元素上为什么产物不同？

**答**：
- v-model 是**语法糖**，编译时按目标类型生成三件套：绑定值 + 监听事件 + （原生元素需要的）动态 value/checked 属性。
- 文本输入 `<input v-model="msg">` → `:value="msg"` + `@input="msg = $event.target.value"`；多选框 → `:checked` + `@change`；单选 → `:checked` + `@change`；`select` → `:value` + `@change`（配合 selected 处理）。元素差异源于**取值方式不同**：input 用 `target.value`，checkbox 用 `target.checked` 和 trueValue/falseValue 映射。
- 组件上 `<MyInput v-model="msg">` → `:modelValue="msg"` + `@update:modelValue="msg = $event"`，配合子组件 `defineProps(['modelValue'])` + `emit('update:modelValue', v)`。
- `.lazy/.number/.trim` 修饰符在编译期生成不同的赋值表达式（lazy 把 input 换 change，number 包 `looseToNumber`），纯编译期展开，无运行时成本。

```html
<!-- 简化实验，帮助理解 v-model 的编译产物（vue-template-explorer 输出） -->

<!-- 输入 1：<input v-model="msg" /> -->
<!-- 产物：_createElementVNode("input", {
        value: _ctx.msg,
        onInput: _cache[0] || (_cache[0] = ($event) => ((_ctx.msg) = $event.target.value))
      }, null, 16 /* FULL_PROPS：value 是动态 prop */ ) -->

<!-- 输入 2：<input type="checkbox" v-model="ok" /> -->
<!-- 产物：_createElementVNode("input", {
        type: "checkbox",
        checked: _ctx.ok,
        onChange: _cache[1] || (_cache[1] = ($event) => ((_ctx.ok) = $event.target.checked))
      }) -->

<!-- 输入 3：<MyInput v-model="msg" /> -->
<!-- 产物：_createVNode(_component_MyInput, {
        modelValue: _ctx.msg,
        "onUpdate:modelValue": _cache[2] || (_cache[2] = ($event) => ((_ctx.msg) = $event))
      }, null, 512 /* NEED_PATCH | DYNAMIC_SLOTS 无，模型 prop + 事件 */) -->

<!-- 输入 4：<input v-model.lazy="msg" /> -->
<!-- 产物：onInput 变为 onChange = ($event) => ((_ctx.msg) = $event.target.value) -->
<script type="module">
  // 组件侧等价手写：v-model 展开后的真实契约
  export default {
    props: ['modelValue'],
    emits: ['update:modelValue'],
    template: `<input :value="modelValue" @input="$emit('update:modelValue', $event.target.value)">`,
  };
</script>
```
