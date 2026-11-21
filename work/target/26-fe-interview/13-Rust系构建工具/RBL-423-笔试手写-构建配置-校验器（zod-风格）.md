---
title: [RBL-423] 笔试：手写构建配置校验器（schema + did-you-mean）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-423：手写构建配置校验器
**需求**：实现 `createConfigValidator(schema)`：1) schema 声明式：`{ field: { type: 'string'|'number'|'bool'|'enum'|'object'|'array', required, values, children } }`；2) validate(config)：逐字段校验 → 错误列表 { path, code: 'unknown'|'type'|'required'|'value', message }；3) unknown 字段给 did-you-mean（编辑距离最近字段建议）；4) 嵌套递归校验（children）；5) 输出人类可读报告（路径精确 + 修复示例）；6) strict 模式（unknown 报错）与 loose（警告）。

```javascript
function editDistance(a, b) {
  const dp = Array.from({ length: a.length + 1 }, (_, i) => [i, ...Array(b.length).fill(0)])
  for (let j = 0; j <= b.length; j++) dp[0][j] = j
  for (let i = 1; i <= a.length; i++)
    for (let j = 1; j <= b.length; j++)
      dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1))
  return dp[a.length][b.length]
}

function suggest(unknown, candidates) {
  return candidates.sort((x, y) => editDistance(unknown, x) - editDistance(unknown, y))[0]
}

export function createConfigValidator(schema, { strict = true } = {}) {
  function validate(config, path = '', errors = []) {
    for (const [key, value] of Object.entries(config)) {
      const rule = schema[key]
      const p = path ? `${path}.${key}` : key
      if (!rule) {
        const s = suggest(key, Object.keys(schema))
        const msg = `unknown option "${p}"${s ? ` — did you mean "${s}"?` : ''}`
        strict ? errors.push({ path: p, code: 'unknown', message: msg })
               : console.warn(msg)
        continue
      }
      if (rule.required && (value === undefined)) { errors.push({ path: p, code: 'required' }); continue }
      if (value === undefined) continue
      const typeOk = rule.type === 'array' ? Array.isArray(value)
        : rule.type === 'enum' ? typeof value === 'string' : typeof value === rule.type
      if (!typeOk) { errors.push({ path: p, code: 'type', message: `expected ${rule.type}, got ${typeof value}` }); continue }
      if (rule.type === 'enum' && !rule.values.includes(value))
        errors.push({ path: p, code: 'value', message: `expected one of [${rule.values.join(', ')}], got "${value}"` })
      if (rule.type === 'object' && rule.children) validate(value, p, errors)
    }
    for (const [key, rule] of Object.entries(schema))
      if (rule.required && config[key] === undefined)
        errors.push({ path: path ? `${path}.${key}` : key, code: 'required', message: `"${key}" is required` })
    return errors
  }
  return { validate }
}
```
**评分点**：
- 四类错误码（unknown/type/required/value）全覆盖
- did-you-mean 编辑距离建议（unknown 字段最常见痛点）
- strict/loose 双模式（unknown 警告向前兼容——配置演进策略）
- 递归嵌套 + 报告路径精确
