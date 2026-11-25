---
title: [WCN-417] 笔试：实现元素树的信号 context（provider/consumer）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-417：笔试：实现元素树的信号 context（provider/consumer）。
**题目**：`provide(ctx)` 元素提供上下文信号；consumer 沿 composedPath 向上查找最近 provider。查找到的 ctx 信号可直接订阅。

```javascript
class DsProvider extends HTMLElement {
  locale = signal('zh');        // 上下文信号
}
function consume(el, key) {
  const ev = new Event('_dslookup', { composed: true });
  el.dispatchEvent(ev);
  const p = ev.composedPath().find(n => n instanceof HTMLElement && n[key] instanceof Object);
  if (!p) throw new Error(`[${el.tagName}] 未找到 provider: ${key}`);
  return p[key];
}
const locale = consume(this, 'locale');
effect(() => this._render(locale.get()));

```

**评分点**：
- 查找：临时事件（不冒泡）的 composedPath 遍历祖先。
- 返回 provider 的 ctx（信号对象）——consumer 建立订阅。
- 跨 shadow 正确（composedPath 天然穿透）。
- 未找到 provider 的报错信息（含 consumer tag）。
