---
title: [WCN-186] 笔试：手写 WC 组件的降级渲染器（错误边界 + 超时降级 + 重试上限）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-186：笔试：手写 WC 组件的降级渲染器

**题目**：实现 `<wc-safe impl="heavy-table">`：① 动态加载 impl 指定的组件（超时 5s 算失败）；② 成功后替换自身内容渲染真实组件（属性透传）；③ 失败渲染 fallback slot 内容；④ 指数退避重试（最多 3 次：1s/2s/4s）；⑤ 重试期间渲染加载态；⑥ 全部失败派发 `wc-fallback` 事件（含错误）供宿主上报。

**答**：

```javascript
class WcSafe extends HTMLElement {
  static observedAttributes = ['impl', 'timeout'];
  #attempt = 0;
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>.loading{padding:16px;color:#6b7280}</style>
        <div class="loading" part="loading">加载中…</div><slot name="fallback" hidden></slot>
        <div part="mount"></div>`;
    }
    this.#try();
  }
  async #try() {
    const impl = this.getAttribute('impl');
    const timeout = Number(this.getAttribute('timeout')) | 0 || 5000;
    try {
      const loaded = Promise.race([
        import(/* @vite-ignore */ `./components/${impl}.js`),
        new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), timeout)),
      ]);
      await loaded;
      // 挂载真实组件：属性透传
      const real = document.createElement(impl);
      for (const a of this.attributes) {
        if (a.name !== 'impl' && a.name !== 'timeout') real.setAttribute(a.name, a.value);
      }
      this.shadowRoot.querySelector('[part=mount]').replaceChildren(real);
      this.shadowRoot.querySelector('.loading').remove();
    } catch (e) {
      this.#attempt++;
      if (this.#attempt <= 3) {                       // 指数退避重试
        this.shadowRoot.querySelector('.loading').textContent =
          `加载失败，${2 ** (this.#attempt - 1)}s 后重试(${this.#attempt}/3)`;
        setTimeout(() => this.#try(), 1000 * 2 ** (this.#attempt - 1));
      } else {
        this.shadowRoot.querySelector('.loading').remove();
        const fb = this.shadowRoot.querySelector('slot[name=fallback]');
        fb.hidden = false;                            // 显示 fallback slot
        this.dispatchEvent(new CustomEvent('wc-fallback', {
          bubbles: true, composed: true, detail: { impl, attempts: this.#attempt, error: e.message },
        }));
      }
    }
  }
}
customElements.define('wc-safe', WcSafe);
// 用法：<wc-safe impl="heavy-table"><div slot="fallback">图表暂不可用</div></wc-safe>
```

**评分点**：
- 超时竞速（Promise.race）判定加载失败，不只是 catch。
- 指数退避 1/2/4s，上限 3 次，重试期间进度提示。
- 成功路径属性透传（impl/timeout 排除）。
- 失败终态：显示宿主 fallback slot + wc-fallback 事件（含错误详情供上报）。
