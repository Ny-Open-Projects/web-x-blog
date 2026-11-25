---
title: [WCN-924] Islands 之间状态怎么传：静态岛向水合岛共享数据而不引入全局 store
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-924：Islands 之间状态怎么传：静态岛向水合岛共享数据而不引入全局 store

**答**：
- 结论先行：islands 的核心约束是「每个岛独立水合」，跨岛共享应走「数据下沉到 DOM」而非 JS 全局 store——把共享数据序列化进父级 data-* 或 script 标签，各岛读取。
- 常用协议：服务端把共享状态写进 `<script type="application/json" id="__DATA__">`，hydration 时各岛解析自己需要的 slice；或用自定义事件 `ds-state-sync` 在岛间广播变更。
- 静态→水合：静态岛不含 JS，它的数据本就在 SSR HTML 里；水合岛要从 DOM/属性读取初始状态，不要假设别人「推送」给它。
- 避免耦合：若两个岛频繁同步，说明切分错误，应合并为一个岛——islands 边界应落在状态无关处。
- 追问钩子：面试官问「共享状态变了怎么让多个岛同步」——答：用 BroadcastChannel 或 CustomEvent 广播 + 各岛订阅，但更根本的是重新审视是否切分过细。

```javascript
// SSR 输出：共享数据下沉到 DOM（以字符串注入模拟）
document.body.insertAdjacentHTML('afterbegin', `
<script type="application/json" id="__SHARED__">{"skuId":9527,"price":199}</script>
<ds-price data-slice="price"></ds-price>
<ds-cart data-slice="skuId"></ds-cart>`);
const shared = JSON.parse(document.getElementById('__SHARED__').textContent);
document.querySelectorAll('[data-slice]').forEach(el => {
  const key = el.dataset.slice;
  el.setAttribute('value', shared[key]); // 各岛读自己的 slice，无需全局 store
});
// 岛间变更用事件广播：
document.addEventListener('ds-price-change', e =>
  console.log('cart 同步价格', e.detail));
// 变更方：
document.dispatchEvent(new CustomEvent('ds-price-change', { detail: 199 }));
```
