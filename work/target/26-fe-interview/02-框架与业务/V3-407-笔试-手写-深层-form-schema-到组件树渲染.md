---
title: [V3-407] 笔试：手写 schema 表单引擎的渲染核心（动态组件树 + 联动）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-407：笔试：手写 schema 表单引擎的渲染核心（动态组件树 + 联动）
**题**：给定 schema 数组 `[{ field, type: 'input'|'select', label, visibleWhen: (v) => boolean, rules } ]`，实现 `renderSchema(schema, model)` 的核心函数：按 visibleWhen 过滤生成渲染列表；model 变化重算可见性（computed）；校验只针对可见字段。

```javascript
function useFormEngine(schema, model) {
  const visibleFields = computed(() =>
    schema.filter(f => !f.visibleWhen || f.visibleWhen(model.value))
  )
  const errors = reactive({})
  function validateField(f) {
    const v = model.value[f.field]
    for (const rule of f.rules || []) {
      if (rule.required && (v === undefined || v === '')) return rule.message || `${f.label}必填`
      if (rule.pattern && !rule.pattern.test(String(v ?? ''))) return rule.message
    }
    delete errors[f.field]
    return null
  }
  function validate() {
    let ok = true
    visibleFields.value.forEach(f => {          // 只校验可见字段
      const err = validateField(f)
      if (err) { errors[f.field] = err; ok = false }
    })
    return ok
  }
  return { visibleFields, errors, validate }
}
```
**评分点**：
- visibleWhen 用 computed 派生（响应式联动）。
- 校验范围 = 可见字段集合（隐藏字段不校验——高频细节）。
- rules 遍历短路返回首个错误。
- errors 用对象按字段存，便于表单局部展示。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-2a2b2e1e-1514-4d56-8f6e-0795d05a6df2-cwd'; fi
exit "$__zcode_status"
