---
title: [FRP-158] 表单库原理对比：rc-field-form 的依赖收集 vs react-hook-form 的非受控订阅？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-158：表单库原理对比：rc-field-form 的依赖收集 vs react-hook-form 的非受控订阅？

**答**：
- rc-field-form（AntD Form）：每个 Field 注册进 store；Field render 时调用 `getFieldValue`，store 用**类似响应式的依赖收集**记录"该 Field 读过哪些 key"；值变化只通知依赖它的 Field 重渲。
- react-hook-form：input 保持**非受控**（uncontrolled），注册时把 ref 存进 fields 表，输入直接写 DOM + 内部值，**不触发 React 重渲**；订阅走 `watch/subscription` 手动声明。
- 性能取向：rc-field-form 用依赖收集做到"字段级精确更新"但仍是受控（每次键入走 React 调度）；RHF 键入零重渲、提交时从 ref 收集——超大表单场景优势明显。
- 共同点：都以"store 集中管理值"为内核；差异只在"值变化的传播机制"——响应式收集 vs 显式订阅。

```javascript
// 简化实现，帮助理解两种内核
// —— rc-field-form 风格：依赖收集的字段级更新 ——
function createStore() {
  const store = {};
  const watchers = new Map();   // key -> Set<FieldId>
  const fieldDeps = new Map();  // FieldId -> Set<key>（该 Field 读过哪些 key）
  const fieldRerender = new Map();
  let currentField = null;      // 收集目标

  return {
    registerField(id, rerender) { fieldRerender.set(id, rerender); },
    getFieldValue(key) {
      // render 期间调用 -> 收集依赖（类似 track）
      if (currentField) {
        fieldDeps.get(currentField).add(key);
        watchers.has(key) || watchers.set(key, new Set());
        watchers.get(key).add(currentField);
      }
      return store[key];
    },
    setFieldValue(key, value) {
      store[key] = value;
      // 只通知依赖该 key 的 Field —— 字段级精确更新
      (watchers.get(key) || []).forEach(id => fieldRerender.get(id)());
    },
    withField(id, render) {
      fieldDeps.set(id, new Set());
      currentField = id;
      try { return render(); } finally { currentField = null; }
    }
  };
}

// —— react-hook-form 风格：非受控 + 显式订阅 ——
function createRhfStore() {
  const fields = new Map();     // name -> { ref, value }
  const subscribers = new Set();
  return {
    register(name, ref) { fields.set(name, { ref, value: ref.current.value }); },
    // 键入：原生 input 自己维护 value（非受控）—— store 只在提交/watch 时读
    handleSubmit(onValid) {
      const data = {};
      fields.forEach(({ ref }, name) => (data[name] = ref.current.value)); // 从 DOM 收集
      return (e) => { e.preventDefault(); onValid(data); };
    },
    watch(name, cb) { subscribers.add({ name, cb }); },  // 显式订阅才重渲
  };
}
// 差异总结：rc-field-form "读时收集，写时通知"（响应式内核）；
// RHF "写不通知，读从 DOM"（uncontrolled 内核）—— 输入路径完全绕开 React 调度。
```
