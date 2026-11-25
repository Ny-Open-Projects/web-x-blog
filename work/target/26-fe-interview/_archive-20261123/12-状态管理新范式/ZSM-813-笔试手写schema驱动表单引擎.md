---
title: [ZSM-813] 笔试：手写 schema 驱动表单引擎（动态字段 + 依赖图重建 + 漂移防御）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-813：手写 schema 驱动表单引擎（动态字段 + 依赖图重建 + 漂移防御）
**需求**：实现 `createSchemaForm(schema)`：1) `applySchema(next)`：字段增删——重建依赖图（环检测）、清理孤儿值、元状态按 version 键控清理；2) `setValue(key, v)`：值更新 + 沿新 schema 的 deps 联动重算（visibleWhen/compute）；3) `visibleFields()`：派生可见字段（visibleWhen 求值）；4) `submit()`：schemaVersion 漂移防御（409 重拉）；5) 附用例：schema v3→v4 删字段后值清理与联动。

```javascript
function createSchemaForm(schema) {
  let current = schema
  let values = {}
  const meta = new Map()        // `${version}:${key}` -> { touched, error }
  const listeners = new Set()

  function buildEngine(fields) {
    // 依赖图：deps + 环检测
    const deps = new Map(fields.map((f) => [f.key, f.deps ?? []]))
    const color = new Map()
    function dfs(k, stack) {
      color.set(k, 1); stack.push(k)
      for (const d of deps.get(k) ?? []) {
        if (color.get(d) === 1) throw new Error(`schema 依赖成环: ${[...stack.slice(stack.indexOf(d)), d].join('→')}`)
        if (!color.get(d)) dfs(d, stack)
      }
      stack.pop(); color.set(k, 2)
    }
    fields.forEach((f) => { if (!color.get(f.key)) dfs(f.key, []) })
    return { deps, byKey: new Map(fields.map((f) => [f.key, f])) }
  }

  let engine = buildEngine(current.fields)

  function applySchema(next) {
    // 环检测（会 throw）
    engine = buildEngine(next.fields)
    // 孤儿值清理
    const validKeys = new Set(next.fields.map((f) => f.key))
    values = Object.fromEntries(Object.entries(values).filter(([k]) => validKeys.has(k)))
    // 元状态按 version 键控清理
    for (const [key] of meta) {
      if (!key.startsWith(`v${next.version}:`)) meta.delete(key)
    }
    current = next
    recomputeAll()
    notify()
  }

  function recomputeAll() {
    // 拓扑序联动：visibleWhen / compute
    const order = topo(current.fields)
    for (const f of order) {
      const conf = engine.byKey.get(f.key)
      if (conf.visibleWhen && !conf.visibleWhen(values)) delete values[f.key]
      if (conf.compute) {
        const r = conf.compute(values)
        if (r !== undefined) values[f.key] = r
      }
    }
  }

  function topo(fields) {
    const indeg = new Map(fields.map((f) => [f.key, (f.deps ?? []).length]))
    const q = fields.filter((f) => (f.deps ?? []).length === 0).map((f) => f.key)
    const out = []
    while (q.length) {
      const k = q.shift()
      out.push(engine.byKey.get(k))
      for (const f of fields) {
        if ((f.deps ?? []).includes(k) && --indeg.get(f.key) === 0) q.push(f.key)
      }
    }
    return out
  }

  function setValue(key, v) {
    values[key] = v
    const mk = `v${current.version}:${key}`
    meta.set(mk, { ...(meta.get(mk) ?? {}), touched: true })
    // 联动重算：只重算下游
    const downstream = current.fields.filter((f) => (f.deps ?? []).includes(key))
    for (const f of downstream) {
      if (f.visibleWhen && !f.visibleWhen(values)) delete values[f.key]
      if (f.compute) values[f.key] = f.compute(values)
    }
    notify()
  }

  function visibleFields() {
    return current.fields.filter((f) => !f.visibleWhen || f.visibleWhen(values))
  }

  async function submit() {
    const res = await api.submit({ values, schemaVersion: current.version })
    if (res.status === 409) {
      const next = await api.getSchema()       // 漂移：重拉 schema
      applySchema(next)
      throw new Error('SCHEMA_DRIFTED')        // UI 提示重新确认
    }
    return res
  }

  function notify() { listeners.forEach((fn) => fn({ values: { ...values }, visible: visibleFields().map((f) => f.key) })) }

  return { setValue, applySchema, visibleFields, submit, subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)), get values() { return { ...values } } }
}

// 用例：v3 → v4（删 plan，payment 联动消失）
const v3 = { version: 3, fields: [
  { key: 'name', type: 'string', deps: [] },
  { key: 'plan', type: 'enum', deps: ['name'] },
  { key: 'payment', type: 'string', deps: ['plan'], visibleWhen: (v) => v.plan === 'pro' },
] }
const form = createSchemaForm(v3)
form.setValue('name', '张三')
form.setValue('plan', 'pro')
form.setValue('payment', 'alipay')
console.log(form.visibleFields().map((f) => f.key))   // ['name','plan','payment']

const v4 = { version: 4, fields: [
  { key: 'name', type: 'string', deps: [] },
] }
form.applySchema(v4)
console.log(form.values)                               // { name: '张三' }：plan/payment 孤儿清理
console.log(form.visibleFields().map((f) => f.key))    // ['name']
```
**评分点**：
- schema 切换三清理（孤儿值/元状态键控/引擎重建+环检测）
- 拓扑序联动（visibleWhen/compute 按下游重算）
- 提交 409 漂移防御（重拉 schema + applySchema + 抛出提示）
- 元状态按 `version:key` 键控（版本切换自动失效）
