---
title: [RBL-408] 笔试：手写构建配置 merge 策略（数组/函数/环境覆盖）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-408：手写构建配置 merge 策略
**答**：实现 `mergeConfig(base, override)`：1) 普通对象深合并；2) 数组策略可配：concat（拼接）/replace（覆盖）/mergeById（按 name/id 去重合并——插件数组合并）；3) 函数值：override 函数接收 base 结果执行（链式定制）；4) 特殊键规则（plugins/rules 用 mergeById，output 用 replace）；5) 循环引用安全；6) 不可变（不修改两个输入）。

```javascript
const ARRAY_STRATEGY = { plugins: 'mergeById', module: { rules: 'mergeById' }, output: 'replace' }

function isPlainObj(v) {
  return v !== null && typeof v === 'object' && !Array.isArray(v)
    && !(v instanceof Date) && !(v instanceof RegExp)
}

export function mergeConfig(base, override, strategies = ARRAY_STRATEGY) {
  if (typeof override === 'function') return override(base)          // 函数链式
  if (Array.isArray(base) || Array.isArray(override)) {
    const strategy = typeof strategies === 'string' ? strategies : 'concat'
    if (strategy === 'replace') return structuredClone(override)
    if (strategy === 'mergeById') {
      const seen = new Map()
      for (const item of [...(base ?? []), ...(override ?? [])]) {
        const key = item?.name ?? item?.id ?? item?.test?.toString() ?? JSON.stringify(item)
        seen.set(key, seen.has(key) ? mergeConfig(seen.get(key), item, {}) : structuredClone(item))
      }
      return [...seen.values()]
    }
    return [...(base ?? []), ...(override ?? [])]
  }
  if (isPlainObj(base) && isPlainObj(override)) {
    const out = structuredClone(base)
    for (const [k, v] of Object.entries(override)) {
      const sub = typeof strategies === 'object' ? strategies[k] : undefined
      out[k] = mergeConfig(base[k], v, sub ?? (isPlainObj(v) ? strategies : 'replace'))
    }
    return out
  }
  return structuredClone(override ?? base)                           // 标量覆盖
}
```
**评分点**：
- 三种数组策略语义正确（mergeById 按 name/id/test 键去重合并——插件合并核心）
- 函数值链式（override 是函数时接收 base 执行）
- 不可变（structuredClone 输入不改）；循环引用由 clone 兜底
- 策略按键下钻（plugins/rules 特殊，标量 replace）
