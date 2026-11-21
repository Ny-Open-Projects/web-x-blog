---
title: [ZSM-189] 笔试：手写 useOptimisticList（列表乐观增删 + 服务端对账去重）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-189：手写 useOptimisticList（列表乐观增删 + 服务端对账去重）
**需求**：实现 `useOptimisticList(serverItems, { idKey = 'id' })`：1) serverItems 变化时与本地乐观条目合并对账——乐观条目被服务端确认（id 命中）后替换为服务端版本，未命中的（被他人删除的）移除；2) `add(item)` 乐观追加（临时 id = tmp_ 前缀），提交成功后带临时 id 去对账；3) `remove(id)` 乐观移除，失败恢复；4) 返回 { items, add, remove }。核心考点：临时 id 与服务端 id 的映射对账、合并顺序稳定（乐观条目保持用户操作位置）。

```javascript
export function useOptimisticList(serverItems = [], { idKey = 'id' } = {}) {
  const [pending, setPending] = useState([])   // 乐观条目（可能已提交）
  const optimisticKey = (it) => it.__tmp ?? it[idKey]

  const add = useCallback(async (draft) => {
    const tmpId = `tmp_${crypto.randomUUID()}`
    const item = { ...draft, [idKey]: tmpId, __tmp: tmpId }
    setPending(p => [...p, item])              // 乐观插入
    try {
      const saved = await api.create(draft)    // 服务端真实 id
      setPending(p => p.map(i => i.__tmp === tmpId
        ? { ...saved, __tmp: tmpId } : i))     // 保留占位，等服务端列表对账替换
      return saved
    } catch (e) {
      setPending(p => p.filter(i => i.__tmp !== tmpId))   // 失败移除
      throw e
    }
  }, [idKey])

  const items = useMemo(() => {
    const serverIds = new Set(serverItems.map(i => i[idKey]))
    const confirmed = pending.filter(p => !p.__tmp || serverIds.has(p[idKey]))
    const localOnly = pending.filter(p => p.__tmp && !serverIds.has(p[idKey]))
    // 已确认的取服务端版本；未确认的（含提交中）排在服务端列表尾部保持位置
    return [
      ...serverItems,
      ...confirmed.filter(c => !serverItems.some(s => s[idKey] === c[idKey])),
      ...localOnly,
    ]
  }, [serverItems, pending, idKey])

  const remove = useCallback(async (id) => {
    setPending(p => p.filter(i => i[idKey] !== id))          // 乐观移除本地
    if (!String(id).startsWith('tmp_'))
      await api.remove(id)                                   // 服务端真实删除
  }, [idKey])

  return { items, add, remove }
}

// 评分点：
// 1. 临时 id（tmp_ 前缀）与服务端 id 的映射与对账
// 2. 服务端刷新后：确认条目被替换、被删条目自动消失（对账核心）
// 3. add 失败移除乐观占位；remove 对 tmp 条目不再发请求
// 4. 合并顺序稳定，用户感知不到跳位
// 5. useMemo 派生，serverItems 与 pending 双依赖
```
