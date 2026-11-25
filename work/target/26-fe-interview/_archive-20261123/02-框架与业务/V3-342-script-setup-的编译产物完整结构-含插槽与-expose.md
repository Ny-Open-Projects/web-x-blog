---
title: [V3-342] script setup 的完整编译产物结构是怎样的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-342：script setup 的完整编译产物结构是怎样的？
**答**：
- 产物骨架：`export default { props: ..., emits: ..., setup(__props, { expose, emit, slots, attrs }) { ... return () => render } }`。
- 顶层变量自动 return 给模板：编译器收集模板中引用的标识符，生成 `return { a, b, handleClick }`，未用的不暴露。
- defineProps → `__props` + props 类型声明；defineEmits → emit 函数；defineExpose → exposed 对象；defineModel 展开为 prop + emit('update:xxx')。
- 闭包成本：顶层 import 的组件、组合式函数都在 setup 闭包内，模板绑定零开销访问（不像 Options API 需要 this 代理）。
- 父链调试：产物中 `__isScriptSetup: true` 标记，devtools 据此展示 setup 绑定。
```javascript
export default {
  props: { title: String },
  setup(__props) {
    const msg = ref('hi')
    return { msg, __props }
    // render 由独立编译产物提供
  }
}
```
