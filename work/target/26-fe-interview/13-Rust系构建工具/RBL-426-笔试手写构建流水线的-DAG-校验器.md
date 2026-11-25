---
title: [RBL-426] 笔试：手写构建流水线 DAG 校验器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-426：手写构建流水线 DAG 校验器
**答**：实现 `validatePipeline(stages)`：1) stages：`{ id, needs: string[], outputs: string[], inputs: string[] }`；2) 检查：环（needs 成环拒绝）、缺失引用（needs/inputs 引用不存在的 stage/产物）、产物唯一性（同一产物两个 stage 产出——冲突）、输入就绪（inputs 必须来自 needs 的 outputs——隐式依赖检测）；3) 返回 { ok, errors: [{code, detail}] }；4) 输出拓扑序（合法时给出执行顺序建议）；5) 错误码风格（DAG_CYCLE/DAG_MISSING/DAG_CONFLICT/DAG_IMPLICIT）。

```javascript
export function validatePipeline(stages) {
  const byId = new Map(stages.map((s) => [s.id, s]))
  const errors = []
  const produced = new Map()                          // output → stage

  for (const s of stages) {
    for (const n of s.needs) if (!byId.has(n)) errors.push({ code: 'DAG_MISSING', detail: `${s.id} needs unknown stage ${n}` })
    for (const o of s.outputs)
      if (produced.has(o)) errors.push({ code: 'DAG_CONFLICT', detail: `output "${o}" produced by ${produced.get(o)} and ${s.id}` })
      else produced.set(o, s.id)
  }
  for (const s of stages)
    for (const i of s.inputs ?? [])
      if (!produced.has(i)) errors.push({ code: 'DAG_MISSING', detail: `${s.id} input "${i}" produced by nobody` })
      else if (!s.needs.includes(produced.get(i).id))
        errors.push({ code: 'DAG_IMPLICIT', detail: `${s.id} uses "${i}" from ${produced.get(i).id} but doesn't declare need` })

  // 环检测 + 拓扑序
  const order = [], state = new Map()
  const dfs = (id) => {
    const s = state.get(id) ?? 0
    if (s === 1) { errors.push({ code: 'DAG_CYCLE', detail: `cycle at ${id}` }); return }
    if (s === 2) return
    state.set(id, 1)
    for (const n of byId.get(id).needs ?? []) dfs(n)
    state.set(id, 2)
    order.push(id)
  }
  stages.forEach((s) => dfs(s.id))

  return { ok: errors.length === 0, errors, topoOrder: order }
}
```
**评分点**：
- 四类检查齐备（环/缺失/产物冲突/隐式依赖——隐式依赖是最常见漏检）
- 产物唯一性（两 stage 产同一产物 = 竞态写）
- 隐式依赖检测（用了某产物但没声明 needs——CI yaml 常见 bug）
- 拓扑序输出（合法时给出执行顺序——校验器兼顾可用性）
