---
title: [HW-089] 手写 WeakMap 实例级缓存——模块级状态不泄漏的优雅写法
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-089：手写 WeakMap 实例级缓存——模块级状态不泄漏的优雅写法
**答**：模块级 Map 存实例状态会阻止实例被 GC（模块生命周期 = 页面生命周期）。WeakMap 以实例为键，实例无引用时缓存自动释放。适用：给第三方类扩展元数据、DOM 节点附加状态、装饰器实现。边界：WeakMap 键必须是对象且不可枚举遍历，需要遍历/导出统计时不能用。

```javascript
const meta = new WeakMap();          // 模块级私有状态

class EventBus {
  constructor() { meta.set(this, { handlers: new Map(), once: new Set() }); }
  on(type, fn) {
    const s = meta.get(this);
    const arr = s.handlers.get(type) || [];
    s.handlers.set(type, arr);
    arr.push(fn);
  }
  once(type, fn) { this.on(type, fn); meta.get(this).once.add(fn); }
  emit(type, payload) {
    const s = meta.get(this);
    for (const fn of s.handlers.get(type) || []) {
      fn(payload);
      if (s.once.has(fn)) {
        const arr = s.handlers.get(type);
        arr.splice(arr.indexOf(fn), 1);      // once 执行后移除
        s.once.delete(fn);
      }
    }
  }
  off(type, fn) {
    const s = meta.get(this);
    const arr = s.handlers.get(type);
    if (arr) { const i = arr.indexOf(fn); if (i > -1) arr.splice(i, 1); s.once.delete(fn); }
  }
}
// 泄漏对照：
// const meta = new Map()  +  meta.set(instance, state)
// => 模块 Map 永久持有 instance，即使业务早已不用（长驻 SPA 泄漏源）
// WeakMap：instance 被 GC 时其 entry 自动消失
```

**评分点**：
- WeakMap vs Map 的生命周期差异说清（模块级状态不阻止实例回收）。
- 键为实例本身，私有状态不能从外部枚举（软私有）。
- once 语义实现正确（执行后移除 + once 集合清理）。
- 能说出 WeakMap 的限制：键必须对象、不可遍历、无 size。
