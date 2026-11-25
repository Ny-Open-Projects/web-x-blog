---
title: [WCN-060] 笔试：手写一个 WC 依赖注入容器（DI-lite：token 注册 + 影子树内请求解析）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-060：笔试：手写一个 WC 依赖注入容器

**题目**：实现 `Container`：① `provide(token, factory, { singleton })` 注册依赖，token 为字符串/Symbol；② `inject(el, token)` 在元素所在的"根容器"解析依赖（沿 DOM 向上找挂了 container 的祖先，找不到用全局默认容器）；③ singleton 缓存实例，非 singleton 每次新建；④ 支持循环依赖检测（解析栈中重复 token 抛错）；⑤ 组件 disconnected 时对声明了 dispose 的实例调用清理。

**答**：

```javascript
const globalContainer = new WeakRefContainer();

class Container {
  #reg = new Map();      // token -> { factory, singleton, inst, disposers }
  #resolving = new Set(); // 循环依赖检测
  provide(token, factory, { singleton = true, dispose } = {}) {
    this.#reg.set(token, { factory, singleton, inst: undefined, dispose });
  }
  resolve(el, token) {
    // 沿 DOM 向上找宿主容器（requestContext 思路的落库版）
    const owner = closestContainer(el) ?? globalContainer.deref() ?? this;
    return owner.#get(token);
  }
  #get(token) {
    const entry = this.#reg.get(token);
    if (!entry) throw new Error(`no provider for ${String(token)}`);
    if (this.#resolving.has(token)) throw new Error(`circular dependency: ${String(token)}`);
    if (entry.singleton && entry.inst !== undefined) return entry.inst;
    this.#resolving.add(token);
    try {
      const inst = entry.factory((t) => this.#get(t)); // factory 可再注入
      if (entry.singleton) {
        entry.inst = inst;
        if (entry.dispose) (globalThis.__disposers ??= new WeakMap()).set(inst, entry.dispose);
      }
      return inst;
    } finally { this.#resolving.delete(token); }
  }
}
function closestContainer(el) {
  let n = el;
  while ((n = n.parentElement ?? n.getRootNode().host)) {
    if (n.__container) return n.__container;
  }
  return null;
}

// 用法
const CTX_API = Symbol('api');
const c = new Container();
c.provide(CTX_API, () => ({ getUser: () => fetch('/me').then((r) => r.json()) }));
class ProfileCard extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' });
    this.api = c.resolve(this, CTX_API);
    this.api.getUser().then((u) => this.shadowRoot.textContent = u.name);
  }
}
customElements.define('profile-card', ProfileCard);
```

**评分点**：
- singleton 缓存与解析栈防循环依赖（`#resolving` 的 try/finally 复位）。
- 沿 DOM/影子树 host 链向上查找最近容器（context 思路）。
- token 支持 Symbol（避免字符串冲突）；缺失 provider 报错信息带 token 名。
- factory 支持嵌套注入；dispose 生命周期留有挂点。
