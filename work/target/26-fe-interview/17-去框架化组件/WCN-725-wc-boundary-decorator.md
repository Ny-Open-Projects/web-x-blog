---
title: [WCN-725] 笔试：手写 WC 错误边界与降级渲染装饰器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-725：笔试：手写 WC 错误边界与降级渲染装饰器

**答**：
- 需求：实现 `withErrorBoundary(ComponentClass, fallbackHtml)`，返回一个新的自定义元素类：对其生命周期回调（connectedCallback 等）与事件处理统一 try/catch，出错时把 shadowRoot 内容替换为 fallbackHtml，并派发 `wc-error` 事件（composed:true）。
- 要点：用 Proxy 或原型方法包装拦截所有以 `on`/`handle` 开头及生命周期方法；防止重复进入降级；边界：fallback 本身出错的兜底。

```javascript
function withErrorBoundary(Base, fallbackHtml) {
  return class extends Base {
    #failed = false;
    _fail(err) {
      if (this.#failed) return;
      this.#failed = true;
      try {
        const root = this.shadowRoot || this.attachShadow({ mode: 'open' });
        root.innerHTML = fallbackHtml;
      } catch (_) { this.textContent = '组件不可用'; }  // fallback  Again 出错兜底
      this.dispatchEvent(new CustomEvent('wc-error', {
        detail: String(err), bubbles: true, composed: true,
      }));
    }
    connectedCallback() {
      try { super.connectedCallback?.(); }
      catch (err) { this._fail(err); }
    }
    // 包装对外事件处理：子类调用 this.emit(...) 时受保护
    emit(name, detail) {
      try { super.emit?.(name, detail); }
      catch (err) { this._fail(err); }
    }
  };
}
class Real extends HTMLElement { connectedCallback() { throw new Error('boom'); } }
const Safe = withErrorBoundary(Real, '<b>降级内容</b>');
customElements.define('ds-safe', Safe);
```

**评分点**：
- 统一包装生命周期与事件处理，异常不外泄（隔离性）。
- 降级渲染幂等（#failed 防重复），并派发 composed 错误事件供上报。
- fallback 自身异常有二次兜底，避免降级路径再崩。
- 返回可注册的自定义元素类，符合 WC 使用方式。
