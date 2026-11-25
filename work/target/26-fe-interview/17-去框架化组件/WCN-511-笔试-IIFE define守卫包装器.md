---
title: [WCN-511] 笔试：实现 UMD/IIFE 元素 bundle 的「define 守卫 + 全局命名空间隔离」包装器。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-511：笔试：实现 UMD/IIFE 元素 bundle 的「define 守卫 + 全局命名空间隔离」包装器。

**答**：
- 结论：包装器用 IIFE 隔离作用域，只在全局挂单一命名空间对象，并做 define 幂等与冲突告警。
- 命名空间隔离避免多份 bundle 互相覆盖全局对象（合并而非替换）。
- define 守卫：先 get，存在时比对版本，仅同版本静默复用，异版本告警。
- 追问：如何支持多份 bundle 加载时选择「最新胜出」而非「先到先得」？

```javascript
(function (global, factory) {
  const NS = '__DS__';
  if (!global[NS]) global[NS] = { version: '0', comps: {} };          // 合并而非覆盖
  const ns = global[NS];
  const api = factory();
  if (cmp(api.version, ns.version) > 0) ns.version = api.version;    // 最新胜出
  Object.assign(ns.comps, api.comps);
  Object.entries(api.comps).forEach(([tag, Cls]) => {
    const cur = customElements.get(tag);
    if (cur) {
      if (cur.__v !== api.version) console.warn(`[DS] ${tag} 冲突: ${cur.__v} vs ${api.version}`);
      return;
    }
    Cls.__v = api.version; customElements.define(tag, Cls);
  });
  function cmp(a, b) { return a.localeCompare(b, undefined, { numeric: true }); }
})(window, () => ({ version: '3.1.0', comps: { 'ds-btn': class extends HTMLElement {} } }));
```

**评分点**：
- IIFE 作用域隔离 + 全局单一命名空间
- 多 bundle 合并与最新胜出
- define 幂等守卫
- 异版本冲突告警
