---
title: [ZSM-416] 笔试：手写 URL 状态编解码器（紧凑/可逆/版本化）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-416：手写 URL 状态编解码器
**需求**：实现 `encodeState(state)` / `decodeState(search)`：1) 支持字段：字符串/数字/布尔/数组/枚举（白名单外丢弃）；2) 编码为 search 参数：短键映射（{ keyword: 'q', page: 'p' }）、数组用逗号、布尔用 '1'/'0'；3) 解码时字段白名单校验：未知键忽略、类型不符回默认、数组元素过滤非法值；4) 解码永不抛错（非法输入回默认态）；5) 支持版本参数 `_v` 便于未来字段演进。

```javascript
const SPEC = {
  q: { key: 'keyword', type: 'string', max: 100, def: '' },
  p: { key: 'page', type: 'number', min: 1, max: 999, def: 1 },
  f: { key: 'filters', type: 'array', items: 'string', def: [] },
  s: { key: 'sort', type: 'enum', values: ['price', 'time'], def: 'time' },
  b: { key: 'onlyStock', type: 'bool', def: false },
}

export function encodeState(state) {
  const p = new URLSearchParams()
  p.set('_v', '1')
  for (const [short, spec] of Object.entries(SPEC)) {
    const v = state[spec.key]
    if (v === spec.def) continue                              // 默认值不编码（URL 短）
    if (spec.type === 'array') p.set(short, v.join(','))
    else if (spec.type === 'bool') p.set(short, v ? '1' : '0')
    else p.set(short, String(v))
  }
  return p
}

export function decodeState(search) {
  const p = new URLSearchParams(search)
  const out = {}
  for (const spec of Object.values(SPEC)) {
    const raw = p.get(Object.keys(SPEC).find((k) => SPEC[k] === spec) ?? '')
    let v = spec.def
    if (raw !== null) {
      try {
        if (spec.type === 'string') v = raw.slice(0, spec.max)
        if (spec.type === 'number') v = Math.min(Math.max(Number(raw) || spec.def, spec.min), spec.max)
        if (spec.type === 'array') v = raw.split(',').filter((x) => x.length <= 50).slice(0, 20)
        if (spec.type === 'enum') v = spec.values.includes(raw) ? raw : spec.def
        if (spec.type === 'bool') v = raw === '1'
      } catch { /* 保持默认 */ }
    }
    out[spec.key] = v
  }
  return out
}
```
**评分点**：
- 解码永不抛错（try + 白名单 + 默认值三重兜底），非法 URL 不炸页面
- 类型与范围校验（min/max/长度截断/数组元素过滤）——URL 是不可信输入
- 默认值不编码（URL 紧凑）；短键映射
- 版本参数预留（演进不破坏旧链接）
