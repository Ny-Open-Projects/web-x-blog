---
title: [ZSM-427] 笔试：手写可撤销的表单草稿管理器（自动保存 + 撤销 + 恢复）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-427：手写可撤销的表单草稿管理器
**答**：实现 `createDraftManager(formId)`：1) `set(field, value)` 更新草稿（内存），debounce 1s 持久化到 storage；2) 撤销栈：按字段分组（同字段 800ms 内合并为一步）；3) `undo()` 撤销上一步（跨字段），`reset()` 清空草稿与历史；4) `restore()` 启动时从 storage 恢复（损坏/版本不符丢弃）；5) `submit()` 成功后清草稿与历史；6) undo 边界返回 changed 标志。

```javascript
export function createDraftManager(formId, storage) {
  let draft = {}, undoStack = [], curGroup = null, timer = null
  let lastKey = '', lastTime = 0
  const KEY = `draft:${formId}:v2`

  function persist() { clearTimeout(timer); timer = setTimeout(() =>
    storage.set(KEY, { v: 2, draft, at: Date.now() }), 1000) }

  function set(field, value) {
    const now = Date.now()
    const merge = field === lastKey && now - lastTime < 800 && curGroup
    if (!merge) { undoStack.push({ field, prev: draft[field] }); if (undoStack.length > 50) undoStack.shift() }
    curGroup = field
    draft = { ...draft, [field]: value }
    lastKey = field; lastTime = now
    persist()
  }

  function undo() {
    const step = undoStack.pop()
    if (!step) return { changed: false }
    draft = { ...draft, [step.field]: step.prev }
    persist()
    return { changed: true, field: step.field }
  }

  function restore() {
    try {
      const saved = storage.get(KEY)
      if (saved?.v === 2) draft = saved.draft          // 版本校验
      else storage.remove(KEY)                          // 丢弃损坏
    } catch { storage.remove(KEY) }
    return draft
  }

  function submit() { clearTimeout(timer); storage.remove(KEY); draft = {}; undoStack = [] }
  function reset() { Object.keys(draft).forEach((f) => set(f, undefined)); submit() }
  return { set, undo, restore, submit, reset, getDraft: () => draft }
}
```
**评分点**：
- 字段分组合并（同字段快速输入一步撤销）+ 栈上限
- 持久化 debounce + 版本校验 + 损坏丢弃（restore 永不抛错）
- submit 成功清草稿与历史（数据一致）；undo 边界 changed 标志
- reset 复用 submit 的清理路径（避免两套清理逻辑漂移）
