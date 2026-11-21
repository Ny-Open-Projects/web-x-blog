---
title: [WCN-034] WC 如何做单元测试？jsdom 对 Shadow DOM 的限制与绕过方式？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-034：WC 如何做单元测试？jsdom 对 Shadow DOM 的限制与绕过方式？

**答**：
- jsdom 支持基本 customElements 与 attachShadow，但局限多：不支持 `ElementInternals`、Constructable Stylesheets 部分 API、`composedPath` 行为简化、没有真实布局（offsetWidth 恒为 0）。
- 主流方案：Vitest + jsdom 覆盖逻辑类测试；交互/样式相关用 Playwright 真浏览器测试（推荐 WC 项目双轨）。
- `:defined` 等待：define 是异步升级，测试里要 `await customElements.whenDefined(tag)` 或 `await updateComplete`（Lit 的周期 Promise）。
- closed shadow 无法查询：测试期统一用 open，或组件暴露 `__testRoot` 之类的测试钩子；不要在测试里 hack `attachShadow` 原型。
- 事件断言：监听 composed 事件需绑在 document/host 上；`element.click()` 不会自动冒出影子树中未 composed 的事件。

```javascript
// Vitest 单测示例
import { describe, it, expect, beforeEach } from 'vitest';
import './quantity-picker.js';

describe('quantity-picker', () => {
  let el;
  beforeEach(async () => {
    el = document.createElement('quantity-picker');
    document.body.append(el);
    await customElements.whenDefined('quantity-picker');
    el.shadowRoot // open 模式可直接查
  });
  it('点击 + 时数量增加并派发 composed 事件', async () => {
    const events = [];
    document.addEventListener('quantity-change', (e) => events.push(e.detail.value));
    el.shadowRoot.querySelector('button[data-d="1"]').click();
    await Promise.resolve();
    expect(events).toEqual([2]);
    expect(el.value).toBe(2);
  });
});
```
