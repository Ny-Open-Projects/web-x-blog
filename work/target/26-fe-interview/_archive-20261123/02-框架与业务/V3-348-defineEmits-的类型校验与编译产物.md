---
title: [V3-348] defineEmits 的类型校验与编译产物是怎样的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-348：defineEmits 的类型校验与编译产物是怎样的？
**答**：
- 三种写法：运行时数组 `defineEmits(['change'])`、对象校验 `defineEmits({ change: (v) => typeof v === 'number' })`、类型声明 `defineEmits<{ change: [value: number] }>()`。
- 类型声明式是首选：vue-tsc 把 emit 调用纳入类型检查，父组件监听 `@change` 的回调参数也获得精确类型。
- 编译产物：emits 选项进入组件定义；运行时对象式校验器会 warning 不匹配的 payload（仅 dev）。
- emits 声明影响 attrs 透传：声明过的事件不会出现在 $attrs 里，未声明的自定义事件会留在 attrs 被 inheritAttrs 透传——「声明了但没触发」时注意别重复监听。
- 校验器性能：高频事件（scroll/input）建议类型声明 + 运行时不校验。
```javascript
const emit = defineEmits<{ change: [value: number]; reset: [] }>()
emit('change', 1) // 类型安全
```
