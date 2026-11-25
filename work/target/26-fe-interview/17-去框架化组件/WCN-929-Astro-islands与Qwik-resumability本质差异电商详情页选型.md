---
title: [WCN-929] Astro islands 与 Qwik resumability 本质差异：电商详情页怎么选
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-929：Astro islands 与 Qwik resumability 本质差异：电商详情页怎么选

**答**：
- 结论先行：Astro islands 是「选择性水合」——只对标记的岛下载并执行 JS；Qwik resumability 是「零水合」——序列化状态与监听器位置，用户交互时才惰性恢复对应逻辑。
- 机制差异：Astro 每个岛有独立运行时与水合入口，未标记区域纯静态；Qwik 全局只有一个恢复器，点击时按 `on:click` 序列化的 URL 动态 import 处理器。
- 成本曲线：Astro 首屏 JS = 各岛运行时之和，岛多则累积；Qwik 首屏 JS 近乎恒定（只恢复器），但每次交互有 import 延迟（首交互感知）。
- 电商详情页选型：内容重、转化路径集中于加购/SKU → Astro islands 足够且生态成熟；超长页、交互点极多且追求极致首屏 → Qwik 更优但需接受框架绑定与调试成本。
- 追问钩子：面试官问「能结合吗」——答：理念上可（Astro 集成 Qwik 岛），但双重运行时抵消收益，工程上通常二选一。

```javascript
// Astro：选择性水合（客户端指令决定何时水合）
// <BuyBox client:visible />  仅进入视口才水合
// <Header client:load />      立即水合
// Qwik：序列化监听器位置，交互才恢复
// <button on:click={addToCart}>加购</button>
// 产物：on:click="./chunk/addToCart.js#addToCart"
function qwikResume() {
  document.addEventListener('click', async e => {
    const url = e.target.getAttribute('on:click-url');
    if (!url) return;                       // 无 JS 时原生行为兜底
    const { handler } = await import(url); // 交互时才下载执行
    handler(e);
  });
}
qwikResume();
```
