---
title: [R19-338] 笔试：手写迷你 Flight 流解析器
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-338：笔试：手写迷你 Flight 流解析器
**题**：Flight 流格式：每行一个 JSON 块 `id:json`，块内引用写作 `"$@1"`（指向 id 1）。实现 `parseFlight(stream)`：逐行解析到对象池；引用用 Proxy/getter 延迟解析；返回根对象。要求：先到先渲染（解析完一行立即可用）。

```javascript
function parseFlight(lines) {
  const pool = new Map() // id -> value
  function resolveRef(ref) {
    if (typeof ref === 'string' && ref.startsWith('$@')) {
      const id = ref.slice(2)
      return pool.get(id) // 可能尚未到达 → 延迟 getter
    }
    return ref
  }
  const deepResolve = (v) => {
    if (Array.isArray(v)) return v.map(deepResolve)
    if (v && typeof v === 'object') return Object.fromEntries(
      Object.entries(v).map(([k, val]) => [k, deepResolve(val)])
    )
    return resolveRef(v)
  }
  const root = { value: null }
  for (const line of lines) {
    const [id, json] = line.split(':')
    pool.set(id, deepResolve(JSON.parse(json)))
    if (id === '0') root.value = pool.get('0') // 约定根块
  }
  return root
}
```
**评分点**：
- 行级流式解析（先到先用）。
- 引用标记 `$@id` 解析到对象池。
- 未到达引用的处理（至少说出延迟 getter 思路）。
- 根块约定（id 0）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-4fd2db4c-de0e-4f69-a437-7494116e11f2-cwd'; fi
exit "$__zcode_status"
