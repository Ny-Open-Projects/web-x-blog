---
title: [ZSM-539] 长表单（百字段级）的 dirty 追踪怎么做到低成本
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-539：长表单（百字段级）的 dirty 追踪怎么做到低成本

**答**：
- 朴素做法的问题：每次输入对「初始值 vs 当前值」全量深比较（JSON.stringify 或递归 diff），百字段 × 高频输入 = 每键一次 O(n) 比较，还要防 stringify 顺序不稳的误判。
- 低成本方案：**事件驱动的 Set 标记**——字段 onChange 时把 key 加进 `dirtyFields: Set`，dirty 判定就是 `set.size > 0`（O(1)）。用户手动改回原值是否还算脏？产品语义定：一般「动过就算脏」，严格语义可对单字段做一次小比较后从 Set 删除。
- 与持久化的配合：dirtyFields 要随草稿一起持久化，恢复草稿时还原，否则「刷新后明明有改动却不提示保存」。
- 派生切分：`isDirty`（整体）、`dirtyCount`（进度条）、`isFieldDirty(field)`（单字段红点）三个出口，分别订阅 Set.size 与 has(field)——粒度拆开避免一处改动全员重渲。
- 追问钩子：服务端预填字段（默认值异步到达）不算脏——初始化写入要在 hydrate 之后、且用「替换初始值」的方式写，不经过 onChange 路径。

```javascript
const useFormDirty = create((set, get) => ({
  values: {},
  initialValues: {},
  dirtyFields: new Set(),

  init(values) {
    set({ values, initialValues: values, dirtyFields: new Set() }) // 预填不算脏
  },

  setField(key, value) {
    const { values, initialValues } = get()
    const next = { ...values, [key]: value }
    // 严格语义：改回原值就摘掉脏标（一次单字段比较，O(1)）
    const isDirty = value !== initialValues[key]
    const dirty = new Set(get().dirtyFields)
    isDirty ? dirty.add(key) : dirty.delete(key)
    set({ values: next, dirtyFields: dirty })
  },

  resetToSaved() {
    const { initialValues } = get()
    set({ values: initialValues, dirtyFields: new Set() })
  },
}))

// 派生出口（粒度分离）
const isDirty = (s) => s.dirtyFields.size > 0                 // O(1)
const dirtyCount = (s) => s.dirtyFields.size
// 单字段红点：只订阅自己
const useFieldDirty = (key) => useFormDirty((s) => s.dirtyFields.has(key))
```
