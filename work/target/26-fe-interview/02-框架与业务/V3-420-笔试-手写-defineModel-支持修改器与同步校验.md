---
title: [V3-420] 笔试：手写 defineModel 完整版（默认值 + 修饰符 + 校验 emit）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-420：笔试：手写 defineModel 完整版（默认值 + 修饰符 + 校验 emit）
**题**：实现 `useModelEnhanced(props, emit, key, opts)`：opts 含 default、validate(value)（非法值不 emit 且返回 false）、modifiers（number/trim/lazy 不处理 lazy，因 lazy 是事件层）；未绑定时读写本地副本（本地态），绑定后写走 emit。

```javascript
function useModelEnhanced(props, emit, key = 'modelValue', opts = {}) {
  const local = ref(opts.default)
  const isBound = computed(() => props[key] !== undefined)
  const mods = computed(() => props[`${key}Modifiers`] || {})
  const transform = (v) => {
    if (mods.value.trim && typeof v === 'string') v = v.trim()
    if (mods.value.number) { const n = parseFloat(v); if (!Number.isNaN(n)) v = n }
    return v
  }
  const model = computed({
    get() {
      const v = isBound.value ? props[key] : local.value
      return v === undefined ? opts.default : v
    },
    set(nv) {
      nv = transform(nv)
      if (opts.validate && !opts.validate(nv)) return false // 非法值不透传
      if (!isBound.value) { local.value = nv; return }      // 本地态
      if (Object.is(nv, props[key])) return
      emit(`update:${key}`, nv)
    }
  })
  return model
}
// 使用：const value = useModelEnhanced(props, emit, 'modelValue', { default: 0, validate: v => v >= 0 })
```
**评分点**：
- isBound 区分「父组件未绑定 → 本地态」与「绑定 → emit」两种模式。
- validate 不通过直接拦截（不 emit 也不写本地）。
- 修饰符 transform 支持 trim/number。
- 同值短路。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-a161f6e5-9fc3-45c0-8354-8389b03b676a-cwd'; fi
exit "$__zcode_status"
