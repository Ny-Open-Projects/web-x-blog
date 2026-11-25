---
title: [V3-458] v-model 编译产物：不同元素的不同展开
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-458：v-model 编译产物：不同元素的不同展开

**答**：
- v-model 是编译宏糖：按目标元素类型展开为「value 绑定 + 事件监听」——input:text → value+input 事件；checkbox/radio → checked+change；select → value+change
- 组件上的 v-model：展开为 `modelValue prop + onUpdate:modelValue 事件`，支持 `v-model:title` 参数（Vue3 支持多 v-model）——自定义修饰符传 modelModifiers prop
- 修饰符编译：.lazy 换事件（input→change）、.number 强转（编译进事件处理器）、.trim 截空格——都在 codegen 时内联进 handler，运行时零额外开销
- v-model 表达式必须是可写引用（左值）：直接编译期校验「v-model value must be a valid JavaScript target reference」——v-model="list[i]" 这类索引合法，v-model="a + b" 直接报错
- 深水点：原生元素 v-model 的 type 检测在编译期（tag + type 属性静态可判），动态 type（:type 动态绑定）退化到运行时判断（vModelDynamic helper）

```javascript
// <input v-model.trim="msg"> 编译产物
_withDirectives(_createElementVNode('input', {
  'onUpdate:modelValue': $event => ((_ctx.msg) = $event)
}, null, 512 /* NEED_PATCH */), [
  [_vModelText, _ctx.msg, void 0, { trim: true }]   // 修饰符通过指令参数传递
])
```
