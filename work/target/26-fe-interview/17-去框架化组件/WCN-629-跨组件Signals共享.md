---
title: [WCN-629] 跨组件共享 Signal 时，如何避免全局单例带来的耦合与测试污染？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-629：跨组件共享 Signal 时，如何避免全局单例带来的耦合与测试污染？

**答**：
- 结论：用「依赖注入式作用域（Scoped Signal）」替代模块级全局单例；在应用/子树根部提供实例，子组件通过 context 获取。
- 做法：providers 用 WeakMap<Host, SignalStore> 关联 DOM 子树；测试时给每个用例新建 store 并自动销毁，互不污染。
- 追问钩子：微前端多实例怎么办？每个微应用自己的 root 持有一份 store，天然隔离——考察对「作用域即隔离边界」的理解。

```javascript
const stores = new WeakMap();
function provide(root, store) { stores.set(root, store); }
function inject(root) {
  let r = root;
  while (r) {
    if (stores.has(r)) return stores.get(r);
    r = r.parentNode || r.host;
  }
  throw new Error('No signal provider found');
}
// 应用根部提供，子树内任意组件可 inject（沿 DOM/host 链向上找）
const appRoot = document.getElementById('app');
provide(appRoot, { cart: signal(0), user: signal(null) });
class DsCart extends HTMLElement {
  connectedCallback() {
    const { cart } = inject(this);
    effect(() => { this.textContent = `购物车 ${cart.get()}`; });
  }
}
```
