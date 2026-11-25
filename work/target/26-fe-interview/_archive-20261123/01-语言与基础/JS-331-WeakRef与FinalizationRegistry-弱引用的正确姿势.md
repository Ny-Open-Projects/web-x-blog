---
title: [JS-331] WeakRef 与 FinalizationRegistry：弱引用的正确姿势
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, V8]
type: 面试题
---

## JS-331：WeakRef 与 FinalizationRegistry：弱引用的正确姿势

**答**：
- WeakRef：创建对象的弱引用，不阻止 GC 回收——deref() 时若对象已被回收返回 undefined；生命周期由 GC 决定，不能用于「保证存在」的关键逻辑
- FinalizationRegistry：对象被回收后收到回调（cleanup token 关联）——但回调时机不确定、可能永不触发，只能用于诊断/缓存清理这类「尽力而为」场景
- 典型场景：DOM 元素关联元数据缓存（WeakRef + WeakMap 组合）、镜像/离线渲染资源释放追踪
- 限制与红线：不能注册「回收前」回调（没有 resurrect 机会）、cleanup 回调里不能再创建强引用死对象、浏览器生产慎用（API 稳定但行为不可控）
- 更稳的替代：显式 dispose 协议（Symbol.dispose / try-with-resources 提案）——「确定的生命周期管理」优于「依赖 GC 时机」

```javascript
const cache = new Map();        // key: 弱引用
const fr = new FinalizationRegistry((key) => cache.delete(key));

function cacheMeta(el, meta) {
  const ref = new WeakRef(el);
  cache.set(el.dataset.id, { ref, meta });
  fr.register(el, el.dataset.id);          // 回收时清缓存
}
function getMeta(id) {
  const e = cache.get(id);
  const el = e?.ref.deref();
  return el ? e.meta : (cache.delete(id), null);  // 已回收 → 清理
}
```
