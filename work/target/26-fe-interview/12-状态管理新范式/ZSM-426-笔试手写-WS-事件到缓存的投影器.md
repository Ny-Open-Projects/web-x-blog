---
title: [ZSM-426] 笔试：手写 WS 事件到缓存的投影器（upsert/删除/排序）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-426：手写 WS 事件到缓存的投影器
**答**：实现 `createProjector(queryClient)`：1) `register(domain, handlers)`：为业务域注册投影规则（created/updated/deleted 事件 → 缓存操作）；2) `handle(event)`：按 event.domain 路由，幂等（event.id 去重，已处理跳过）；3) created/updated → setQueryData upsert 到列表缓存（含排序字段重排）；4) deleted → 列表缓存移除 + 详情缓存移除；5) 未注册域的事件计入 unknown 计数不处理；6) 处理失败不炸订阅循环（隔离 try-catch）。

```javascript
export function createProjector(qc) {
  const rules = new Map()
  const seen = new Set()         // event.id 去重

  function register(domain, handlers) { rules.set(domain, handlers) }

  function handle(ev) {
    if (seen.has(ev.id)) return                       // 幂等
    seen.add(ev.id)
    if (seen.size > 1000) seen.clear()                // 防膨胀（简化版）
    const rule = rules.get(ev.domain)
    if (!rule) { unknowns++; return }
    try {
      if (ev.type === 'deleted') {
        qc.setQueryData(['list', ev.domain], (old) => old?.filter((x) => x.id !== ev.data.id))
        qc.removeQueries({ queryKey: [ev.domain, ev.data.id] })       // 详情移除
      } else {
        qc.setQueryData(['list', ev.domain], (old) => {
          if (!old) return old
          const others = old.filter((x) => x.id !== ev.data.id)
          const merged = [...others, ev.data]
          return rule.sort ? merged.sort(rule.sort) : merged          // 重排
        })
      }
    } catch (e) { report('projector_error', e) }      // 隔离
  }

  let unknowns = 0
  return { register, handle, stats: () => ({ unknowns }) }
}
```
**评分点**：
- 事件幂等（id 去重）——WS 重连补发安全
- upsert + 排序重排（列表投影不止追加）；deleted 同时处理列表与详情缓存
- 未注册域计数不炸（协议演进安全）；处理异常隔离
- 缓存不存在（old undefined）时保持 undefined 不凭空造列表
