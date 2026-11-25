---
title: [WCN-743] 多租户 SaaS 中切换租户时，如何防止 signal 状态串租户？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-743：多租户 SaaS 中切换租户时，如何防止 signal 状态串租户？

**答**：
- 结论：把租户维度做成 signal 的「作用域」——所有业务 signal 挂在 tenantScope 下，切换租户时整体重建/隔离存储，避免上一个租户的残留数据被误读。
- 关键：任何异步回调在写 signal 前校验当前 tenantId 是否仍是发起时的租户（epoch 思路），否则丢弃；缓存按租户分区（key 前缀 tenantId）。
- 追问钩子：切换瞬间正在进行的请求返回了旧租户数据怎么办？考察「作废 + 丢弃 + 重新请求」。

```javascript
const tenantId = signal('t1');
const store = new Map();                    // tenantId -> state
function scopeSignal(key, initial) {
  return {
    get value() {
      const t = tenantId.value;
      if (!store.has(t)) store.set(t, {});
      return store.get(t)[key] ?? initial;
    },
    set value(v) {
      const t = tenantId.value;
      if (!store.has(t)) store.set(t, {});
      store.get(t)[key] = v;
    },
  };
}
const cart = scopeSignal('cart', []);
cart.value = ['item1'];
tenantId.value = 't2';
console.log(cart.value);   // [] —— 不串租户
```
