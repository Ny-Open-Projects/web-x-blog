---
title: [WCN-018] disconnectedCallback 应该清理哪些资源？有哪些 GC 泄漏陷阱？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-018：disconnectedCallback 应该清理哪些资源？有哪些 GC 泄漏陷阱？

**答**：
- 清理清单：绑在 window/document/其他元素上的监听、setInterval/setTimeout、ResizeObserver/IntersectionObserver/MutationObserver、进行中的 fetch AbortController、全局 store 订阅、外部的 disconnect 回调。
- 陷阱一：闭包持有外部大对象（如整棵列表数据）导致 detached 元素无法回收，把长生命周期引用存在模块级 Map 里最危险，可用 `WeakRef`/`FinalizationRegistry` 兜底调试。
- 陷阱二：事件代理绑在 document 上做"委托"（组件内常见优化），忘了在 disconnected 移除，每次重建组件都叠加一个委托器。
- 陷阱三：`setInterval` 回调里引用了 `this`，元素已移除但定时器仍在跑并持有整个实例——disconnected 必须 clear。
- 陷阱四：第三方库渲染实例（图表、编辑器）挂在自己的 property 上，未调 `instance.destroy()`。
- 追问钩子：可以在 connected/disconnected 配对计数，全部断开后才真正销毁共享资源（多实例共享 observer 模式）。

```javascript
class LazyImage extends HTMLElement {
  #io; #ac;
  connectedCallback() {
    // 共享 observer：类级 Map，所有实例共用一个 IntersectionObserver
    LazyImage.#shared ??= new IntersectionObserver((ents) => {
      for (const en of ents) if (en.isIntersecting) en.target.#load();
    });
    LazyImage.#shared.observe(this);
    this.#ac = new AbortController();
    fetch(this.dataset.meta, { signal: this.#ac.signal }).catch(() => {});
  }
  disconnectedCallback() {
    LazyImage.#shared.unobserve(this);   // 陷阱三的解法：unobserve 而不是留 delegation
    this.#ac.abort();                    // 陷阱一/四的解法
  }
  #load() { this.shadowRoot?.querySelector('img')?.setAttribute('src', this.dataset.src); }
  static #shared;
}
customElements.define('lazy-image', LazyImage);
```
