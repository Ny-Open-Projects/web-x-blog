---
title: [WCN-643] 微前端多租户场景下，如何保证各应用的 Signal 互不污染？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-643：微前端多租户场景下，如何保证各应用的 Signal 互不污染？

**答**：
- 结论：以「应用根容器」为隔离边界，每租户一份 signal 注册表与 effect 集合；全局只保留跨租户的只读广播通道。
- 做法：TenantContext 用 WeakMap<root, Registry>；所有 signal/effect 在租户作用域内创建；卸载时批量 dispose 该租户全部 effect。
- 追问钩子：租户间要共享登录态怎么办？通过单一可信源（如 auth signal）向下广播，而非互相写对方 store——考察隔离与共享的平衡。

```javascript
class TenantScope {
  constructor(root) { this.root = root; this.effects = new Set(); this.store = new Map(); }
  signal(key, value) {
    const s = signal(value);
    this.store.set(key, s);
    return s;
  }
  effect(fn) {
    const d = effect(fn);
    this.effects.add(d);
    return d;
  }
  dispose() {
    this.effects.forEach(d => d());
    this.effects.clear(); this.store.clear();
  }
}
const registry = new WeakMap();
function scopeOf(root) {
  if (!registry.has(root)) registry.set(root, new TenantScope(root));
  return registry.get(root);
}
const tenantA = scopeOf(document.getElementById('app-a'));
tenantA.signal('cart', 0);
// tenantA.dispose() 时该应用全部 effect 被清理，不影响 app-b
```
