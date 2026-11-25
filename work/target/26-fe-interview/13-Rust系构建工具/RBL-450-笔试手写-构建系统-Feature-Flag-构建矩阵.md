---
title: [RBL-450] 笔试：手写 Feature Flag 构建矩阵
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-450：手写 Feature Flag 构建矩阵
**答**：实现 `expandBuildMatrix(flags, configs)`：1) flags：`{ f1: [true, false], f2: ['a', 'b'] }`；2) 笛卡尔积展开：所有组合 × 所有环境配置 → 构建矩阵（但禁止全展开——组合爆炸）；3) 约束过滤：`{ requires: { f2: ['a'] } }`——f1=true 需要 f2=a（非法组合剔除）；4) 命名规则：产物目录按 flag 组合命名（f1t-f2a）；5) 去重优化：相同 DefinePlugin 组合的产物只构建一次（结果复用）；6) 输出矩阵（含每个组合的 envHash 与产物复用关系）。

```javascript
export function expandBuildMatrix(flags, configs, { constraints = {} } = {}) {
  const keys = Object.keys(flags)
  const combos = []
  // 笛卡尔积
  let acc = [{}]
  for (const k of keys) {
    const next = []
    for (const base of acc)
      for (const v of flags[k]) {
        const combo = { ...base, [k]: v }
        if (satisfies(combo, constraints)) next.push(combo)    // 约束过滤在展开时进行（剪枝）
      }
    acc = next
  }
  // 组合 × 环境 + 去重
  const matrix = [], seen = new Map()
  for (const combo of acc) {
    for (const env of Object.keys(configs)) {
      const defineKey = stableKey(combo)
      if (seen.has(defineKey)) { matrix.push({ ...combo, env, reuseOf: seen.get(defineKey) }); continue }
      const id = `${keys.map((k) => `${k}${String(combo[k]).slice(0, 1)}`).join('-')}-${env}`
      seen.set(defineKey, id)
      matrix.push({ id, ...combo, env, defines: comboToDefines(combo) })
    }
  }
  return matrix
}

function satisfies(combo, constraints) {
  return Object.entries(constraints).every(([flag, allowed]) =>
    !combo[flag] || allowed.includes(combo[flag]))
}
function comboToDefines(combo) {
  return Object.fromEntries(Object.entries(combo).map(([k, v]) => [`__FLAG_${k.toUpperCase()}__`, JSON.stringify(v)]))
}
function stableKey(o) { return JSON.stringify(Object.entries(o).sort()) }
```
**评分点**：
- 展开时剪枝（约束过滤在笛卡尔积过程中做——非法组合不进后续层）
- 产物复用去重（同 DefinePlugin 组合只构建一次——矩阵爆炸治理核心）
- 命名规则（flag 组合可读命名——产物可定位）
- 组合爆炸意识（全展开 x^N——答案要体现对规模的控制）
