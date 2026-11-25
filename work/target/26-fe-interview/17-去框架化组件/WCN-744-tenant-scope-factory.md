---
title: [WCN-744] 笔试：手写 tenantScope 的 signal 隔离工厂
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-744：笔试：手写 tenantScope 的 signal 隔离工厂

**答**：
- 需求：实现 `createTenantScope()` 返回 `{ setTenant(id), signal(key, initial), currentTenant() }`。signal 的读写自动落在当前租户的独立存储；setTenant 切换租户互不污染；signal 返回 {get(),set(v)}。
- 要点：用 Map<tenantId, Map<key,value>> 存储；signal 闭包内读写用 currentTenant；边界：未 setTenant 时用默认 'default'，切换后旧租户数据仍保留（可切回）。

```javascript
function createTenantScope() {
  let tenant = 'default';
  const store = new Map();                          // tenant -> Map(key,val)
  function bucket() {
    if (!store.has(tenant)) store.set(tenant, new Map());
    return store.get(tenant);
  }
  return {
    setTenant(id) { tenant = id || 'default'; },
    currentTenant() { return tenant; },
    signal(key, initial) {
      return {
        get() { return bucket().has(key) ? bucket().get(key) : initial; },
        set(v) { bucket().set(key, v); },
      };
    },
  };
}
const scope = createTenantScope();
const cart = scope.signal('cart', []);
cart.set(['a']);
scope.setTenant('t2');
console.log(cart.get());          // [] 新租户
scope.setTenant('default');
console.log(cart.get());          // ['a'] 切回旧租户恢复
```

**评分点**：
- 存储按 tenantId 分区，切换租户数据不串。
- signal 读写自动绑定当前租户，调用方无感。
- 切回旧租户数据保留（合理的隔离语义）。
- 未设置租户时用默认值，具备边界处理。
