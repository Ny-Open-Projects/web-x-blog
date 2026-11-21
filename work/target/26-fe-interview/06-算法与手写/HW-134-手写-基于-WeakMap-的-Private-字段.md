---
title: [HW-134] 手写 WeakMap 私有字段模式——真私有（不可枚举不可枚举遍历）与 #private 字段的取舍
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：JS 私有三种方案：命名约定 `_x`（假私有）、WeakMap（真私有：外部拿不到映射、实例回收自动清理）、`#field`（语言级真私有）。WeakMap 版本适合"需要模块级函数操作私有状态"或"给第三方类附加私有数据"场景；`#field` 是现代首选。

```javascript
const _state = new WeakMap();                 // 模块外无法访问映射本身

class Session {
  constructor(token) {
    _state.set(this, { token, expiresAt: Date.now() + 3600e3 });
  }
  get token() { return _state.get(this).token; }
  isExpired() { return _state.get(this).expiresAt < Date.now(); }
  refresh() { const s = _state.get(this); s.expiresAt = Date.now() + 3600e3; }
}
// 真私有验证：Object.keys(new Session('t')) => []（不可枚举）
// JSON.stringify(session) => '{}'（序列化不泄漏）
// 第三方类附加私有数据（无源码修改权限）：
const handlers = new WeakMap();
function listen(el, fn) { handlers.set(el, fn); el.addEventListener('click', fn); }
function detach(el) { const fn = handlers.get(el); if (fn) el.removeEventListener('click', fn); }
// el 被 GC 时 WeakMap entry 自动消失 —— 无泄漏
// 现代首选：#field（语言级，编译器强制），WeakMap 用于"模块函数化私有"与"外部附加"
```

**评分点**：
- WeakMap 私有的三验证：不可枚举/序列化不泄漏/实例回收自动清理。
- "给第三方类/外部对象附加私有数据"这一独有场景（#field 做不到）。
- 与 #field 的取舍：语言级强制 vs 模块函数化私有。
- 命名约定是假私有（可被遍历/修改）的认知。
