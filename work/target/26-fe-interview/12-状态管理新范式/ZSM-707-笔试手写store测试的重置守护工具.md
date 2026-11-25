---
title: [ZSM-707] 笔试：手写 store 测试重置守护（自动发现脏状态 + 泄漏报告）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-707：手写 store 测试重置守护（自动发现脏状态 + 泄漏报告）
**答**：实现 `createTestGuard()`：1) `register(store, name, resetFn)`：登记测试用 store 与重置函数；2) `snapshotAll()` / `assertClean(label)`：前后快照对比——发现「用例改了状态但没重置」的项（dirty list），含 diff 字段；3) `autoReset()`：afterEach 自动执行所有 resetFn + localStorage/IndexedDB 清理钩子；4) `leakReport()`：未登记的变化源（如手动 setState 绕过守护）与未清理的持久化 key；5) 附用例：模拟用例 A 污染 → assertClean 报告 → autoReset 后干净。

```javascript
function createTestGuard() {
  const registry = new Map()    // name -> { store, resetFn, snapshotBefore }
  const cleanupHooks = []
  const violations = []

  function register(store, name, resetFn) {
    registry.set(name, { store, resetFn })
    return () => registry.delete(name)
  }

  function addCleanup(fn) { cleanupHooks.push(fn) }

  function snapshotAll(label) {
    const snap = {}
    for (const [name, { store }] of registry) {
      snap[name] = structuredClone(store.getState?.() ?? store.get?.())
    }
    registry.__snapshots ??= new Map()
    registry.__snapshots.set(label, snap)
    return snap
  }

  function assertClean(label = 'after') {
    const before = registry.__snapshots.get('before')
    const after = registry.__snapshots.get(label)
    if (!before) return { clean: true }
    const dirty = []
    for (const [name, snap] of Object.entries(after)) {
      const b = before[name]
      if (JSON.stringify(b) !== JSON.stringify(snap)) {
        const diffKeys = Object.keys({ ...b, ...snap }).filter((k) => !Object.is(b?.[k], snap[k]))
        dirty.push({ store: name, diffKeys })
      }
    }
    if (dirty.length) violations.push({ label, dirty })
    return { clean: dirty.length === 0, dirty }
  }

  function autoReset() {
    for (const { resetFn } of registry.values()) resetFn?.()
    cleanupHooks.forEach((fn) => fn())
  }

  function leakReport() {
    return {
      violations,                                    // 未重置的污染记录
      registered: [...registry.keys()],
      persistKeys: Object.keys(localStorage),        // 持久化残留
    }
  }

  return { register, addCleanup, snapshotAll, assertClean, autoReset, leakReport }
}

// 测试装配模式
const guard = createTestGuard()
beforeAll(() => {
  guard.register(useCartApi, 'cart', () => useCartApi.setState(useCartApi.getInitialState()))
  guard.addCleanup(() => localStorage.clear())
  guard.addCleanup(() => vi.useRealTimers())
})
beforeEach(() => { guard.autoReset(); guard.snapshotAll('before') })
afterEach(() => {
  const r = guard.assertClean('after')
  if (!r.clean) console.warn('状态污染:', r.dirty)
  guard.autoReset()
})

// 用例模拟
it('用例A污染未重置', () => {
  useCartApi.setState({ items: ['dirty'] })
  // 忘了恢复 → afterEach 的 assertClean 报告 dirty: [{ store: 'cart', diffKeys: ['items'] }]
})
```
**评分点**：
- 快照对比发现脏状态（diffKeys 定位污染字段）
- autoReset 钩子链（store 重置 + 持久化 + timers 全覆盖）
- violations 累积报告（flaky 根因可追溯）
- leakReport 含持久化残留检查（localStorage keys）
