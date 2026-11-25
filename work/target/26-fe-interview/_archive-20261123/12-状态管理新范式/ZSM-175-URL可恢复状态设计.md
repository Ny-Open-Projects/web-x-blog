---
title: [ZSM-175] 「刷新后一切还原」的 URL 可恢复状态怎么设计？复杂筛选对象怎么在 URL 里无损往返？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-175：「刷新后一切还原」的 URL 可恢复状态怎么设计？复杂筛选对象怎么在 URL 里无损往返？
**答**：
- 设计目标：把「用户可分享/回退的状态子集」定义为 URL schema，其余状态从它派生；还原路径 = 解析 URL → 填充表单草稿 → 驱动缓存取数，全链路无隐藏默认值。
- 复杂对象编码三选一：扁平 kv（?status=paid&tags=a,b——首选，可读可 SEO）、JSON base64（?f=eyJh…——复杂结构兜底，可读性差）、压缩短码（服务端存快照发短链——超长筛选场景）。编码函数要可逆且字段顺序稳定。
- 无损往返要点：parse 与 stringify 互为逆运算（写单测锁死）、默认值只在 parse 侧补全不在 stringify 侧写入（保持 URL 干净）、数组用固定分隔符并转义。
- 面试要点：给出「URL 是可恢复状态的 API」的定位，顺带提 history.replaceState 防止每敲一个字符压一条历史。

```javascript
// schema 化的 URL 编解码：parse/stringify 互逆
const FILTERS = {
  kw:    { type: 'string', def: '' },
  page:  { type: 'number', def: 1 },
  status:{ type: 'enum',   def: 'all', values: ['all','paid','refund'] },
  tags:  { type: 'list',   def: [] },
}

export function parseFilters(sp) {
  const f = {}
  for (const [k, s] of Object.entries(FILTERS)) {
    const raw = sp.get(k)
    f[k] = raw === null ? s.def
      : s.type === 'number' ? Number(raw)
      : s.type === 'list'   ? raw.split(',').filter(Boolean)
      : raw
  }
  return f
}

export function stringifyFilters(f) {
  const sp = new URLSearchParams()
  for (const [k, s] of Object.entries(FILTERS)) {
    const v = Array.isArray(f[k]) ? f[k].join(',') : String(f[k])
    if (v !== String(s.def)) sp.set(k, v)      // 默认值不写入，保持 URL 干净
  }
  return sp
}

// 表单输入用 replaceState 防历史爆炸
useEffect(() => {
  const t = setTimeout(() => history.replaceState(null, '', '?' + stringifyFilters(draft)),
    300)
  return () => clearTimeout(t)
}, [draft])
```
