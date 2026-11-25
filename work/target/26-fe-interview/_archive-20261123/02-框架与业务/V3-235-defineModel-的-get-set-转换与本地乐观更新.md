---
title: [V3-235] defineModel 的 get/set 转换与本地乐观更新机制是怎样的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-235：defineModel 的 get/set 转换与本地乐观更新机制是怎样的？
**答**：
- get/set 钩子：`defineModel({ get: (v) => v ?? '', set: (v) => v.trim() })`——读时兜底、写时规整，转换发生在子组件本地。
- 本地乐观更新：set 时先 emit，同时把本地值临时改为新值，让子组件 UI 立即响应；父组件下一次 props 同步时以父值为准覆盖。
- 意义：解决"父组件异步保存时输入框回跳"问题——乐观值让输入连续，父拒绝时可校正回来。
- 边界：如果父组件永不回传（单向数据流被破坏），本地值与父值长期不一致；受控表单建议父组件恒同步。
- 修饰符：`v-model.capitalize` 会被编译进 modifiers prop，defineModel 返回值带 `.modifiers`，可在 get/set 里读取实现自定义修饰符。

```javascript
// 自定义修饰符 capitalize + 乐观更新
const model = defineModel({
  set: (v, modifiers) => modifiers.capitalize ? v.charAt(0).toUpperCase() + v.slice(1) : v,
  get: (v) => v ?? '',
});
// 父：<Child v-model.capitalize="name" />
// 子输入 'abc' → set 收到 { capitalize: true } → emit('update:name', 'Abc') + 本地立即显示 'Abc'
// 父组件异步保存失败重置 name='' → props 回传 '' → 子组件被校正为空（乐观值生命周期结束）
```
