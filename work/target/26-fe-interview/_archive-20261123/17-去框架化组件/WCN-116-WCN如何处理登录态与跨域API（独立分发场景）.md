---
title: [WCN-116] WCN 独立分发给第三方时如何处理登录态与跨域 API？postMessage vs Cookie vs token 注入？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-116：WCN 独立分发给第三方时如何处理登录态与跨域 API？

**答**：
- 场景：组件 SDK 嵌入客户站点（不同域），组件需调自家 API——天然跨域，且不能复用客户站点的 Cookie/登录态。
- token 注入模式：初始化时传签名 token（`<x-chat api-key="..." user-token="...">` 或 property），组件内部 fetch 带 Authorization 头；短期 token 由客户后端向组件服务端换取（避免长期密钥泄露在前端）。
- postMessage 模式：组件内嵌 iframe 走自家域，业务 API 调用收进 iframe，宿主与 iframe 用 postMessage 通信（适合强信任隔离 + 独立会话）；这是"WC 壳 + iframe 芯"混合架构。
- Cookie 模式：API 域设置 `SameSite=None; Secure` 跨站 Cookie + CORS 允许客户域来源；受第三方 Cookie 限制（Safari ITP 屏蔽）已不可靠，只做兜底。
- 事件与数据出口：组件内用户数据不得写 localStorage 污染客户域；对外只通过 CustomEvent 上报最小必要信息（PII 脱敏）。

```javascript
class AcmeChat extends HTMLElement {
  static observedAttributes = ['api-key', 'region'];
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = '<div id="app"></div>';
    this.#ac = new AbortController();
  }
  async #fetch(path) {
    const key = this.getAttribute('api-key');
    if (!key) throw new Error('missing api-key');
    const res = await fetch(`https://api.acme.com/v1/${path}`, {
      headers: { Authorization: `Bearer ${key}` },
      signal: this.#ac.signal,
    });
    if (!res.ok) throw new Error(`acme api ${res.status}`);
    return res.json();
  }
  #ac;
  disconnectedCallback() { this.#ac.abort(); }
}
customElements.define('acme-chat', AcmeChat);
```
