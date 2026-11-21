---
title: [ZSM-461] 笔试：手写乐观 UI 状态投影器（确认/回滚/超时三态）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-461：手写乐观 UI 状态投影器
**需求**：实现 `createProjection(store)`：1) `apply(item, optimisticPatch)`：返回投影句柄——store 中该条目立即生效并带 `_opt: true` 标记；2) `handle.confirm(serverItem)`：以服务端值覆盖并清除标记；3) `handle.rollback()`：恢复投影前快照；4) `handle.expire(ms)`：超时未确认自动回滚并触发 onExpire 回调（可重试提示）；5) 同一条目多次 apply：新投影覆盖旧投影（旧句柄失效）；6) `isOptimistic(id)` 查询。

```javascript
export function createProjection(store) {
  const actives = new Map()   // id → handle

  function apply(id, optimisticPatch, { onExpire } = {}) {
    actives.get(id)?.expireNow()                        // 旧投影失效
    const prev = structuredClone(store.getState().items.get(id))
    store.setState((s) => ({
      items: new Map(s.items).set(id, { ...prev, ...optimisticPatch, _opt: true }),
    }))
    let timer = null
    const handle = {
      confirm(serverItem) {
        clearTimeout(timer); actives.delete(id)
        store.setState((s) => ({ items: new Map(s.items).set(id, { ...serverItem, _opt: false }) }))
      },
      rollback() {
        clearTimeout(timer); actives.delete(id)
        store.setState((s) => ({ items: new Map(s.items).set(id, prev) }))
      },
      expire(ms) {
        timer = setTimeout(() => { if (actives.get(id) === handle) { handle.rollback(); onExpire?.() } }, ms)
      },
      expireNow() { clearTimeout(timer); this.rollback() },
    }
    actives.set(id, handle)
    return handle
  }

  return { apply, isOptimistic: (id) => !!store.getState().items.get(id)?._opt }
}
```
**评分点**：
- 三态生命周期完整（apply 立即生效 → confirm 覆盖 / rollback 恢复 / expire 超时自动回滚）
- 旧投影失效语义（同条目重复 apply：旧句柄 expireNow，防双计时器）
- prev 快照在 apply 时捕获（rollback 语义精确）
- _opt 标记进 store 驱动 UI（透明度/动画），confirm 清标记
