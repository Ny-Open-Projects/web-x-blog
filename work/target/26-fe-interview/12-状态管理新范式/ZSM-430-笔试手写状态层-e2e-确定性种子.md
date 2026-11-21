---
title: [ZSM-430] 笔试：手写确定性状态种子（E2E 稳定数据构造器）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-430：手写确定性状态种子
**需求**：实现 `seedStore(store, spec)`：1) spec 声明式：`{ items: { count: 30, template: {...}, ids: 'seq' } }`；2) id 确定性：`seq` 模式生成 `id_0001..`（可复现）；3) 随机字段用可种子化 PRNG（mulberry32，seed 相同输出相同）；4) 时间字段基于固定基准时间 + 偏移（不依赖 Date.now）；5) 深度合并 template（数组字段按 count 展开）；6) 返回注入后的 store（链式）。

```javascript
function mulberry32(seed) {
  return () => {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

export function seedStore(store, spec, { seed = 42, baseTime = 1730000000000 } = {}) {
  const rand = mulberry32(seed)
  const out = {}
  for (const [key, cfg] of Object.entries(spec)) {
    out[key] = Array.from({ length: cfg.count }, (_, i) => {
      const item = deepMerge(structuredClone(cfg.template ?? {}), {})
      for (const [f, rule] of Object.entries(cfg.fields ?? {})) {
        if (rule === 'seq') item[f] = `${f}_${String(i + 1).padStart(4, '0')}`        // 确定性 id
        else if (rule?.rand) item[f] = rule.pick[Math.floor(rand() * rule.pick.length)]
        else if (rule?.time) item[f] = new Date(baseTime + i * rule.time).toISOString()
      }
      return item
    })
  }
  store.setState(out)
  return store
}

function deepMerge(t, s) {
  for (const [k, v] of Object.entries(s))
    t[k] = v && typeof v === 'object' && !Array.isArray(v) ? deepMerge(t[k] ?? {}, v) : v
  return t
}
// E2E 断言稳定：seed 相同 → id/随机/时间全部可复现
```
**评分点**：
- 三类确定性来源：seq id、可种子 PRNG（mulberry32 正确实现）、固定基准时间
- 不使用 Date.now/Math.random（不可复现即失格）
- template 深合并保留声明字段；count 展开正确
- 同 seed 断言稳定（E2E 选择器/文本可预期）
