---
title: [V3-355] 手写：实现 mini defineModel 运行时（prop + emit + 修饰符）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-355：手写：实现 mini defineModel 运行时（prop + emit + 修饰符）
**题**：实现 `createModel(props, emit, key)` 返回可写 ref：读 props[key]，写时 emit(`update:key`)；支持修饰符对象 `props[key+'Modifiers']` 中的 number/trim 转换；父组件未传值时返回 options.default。边界：同值写入不 emit。

```javascript
function createModel(props, emit, key = 'modelValue', options = {}) {
  const mods = props[key + 'Modifiers'] || {}
  const transform = (v) => {
    if (mods.trim && typeof v === 'string') v = v.trim()
    if (mods.number) { const n = parseFloat(v); v = Number.isNaN(n) ? v : n }
    return v
  }
  return computed({
    get() {
      const v = props[key]
      return v === undefined ? options.default : v
    },
    set(nv) {
      nv = transform(nv)
      if (Object.is(nv, props[key])) return // 同值短路
      emit(`update:${key}`, nv)
    }
  })
}
// 组件内：const model = createModel(props, emit, 'modelValue', { default: '' })
```
**评分点**：
- 读走 props、写走 emit，单向数据流不破坏。
- 修饰符从 props 读取并正确实现 number 的 NaN 保留原值边界。
- 同值短路（Object.is）防止父组件无谓更新。
- default 仅在 undefined 时生效。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-0277eb85-dab0-4d98-b75a-53c5cd2f42d3-cwd'; fi
exit "$__zcode_status"
