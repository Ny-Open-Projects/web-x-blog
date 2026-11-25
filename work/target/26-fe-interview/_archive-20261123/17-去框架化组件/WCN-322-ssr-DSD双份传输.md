---
title: [WCN-322] DSD 的模板内容与客户端实现里的模板「双份」问题如何治理？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-322：DSD 的模板内容与客户端实现里的模板「双份」问题如何治理？
**答**：
- 问题：HTML 下发 DSD 模板 + JS bundle 里又有同款模板字符串——传输与解析双倍。
- 策略 1：客户端 hydrate 模式复用 DOM（模板已实例化），bundle 中模板可摇树（构建期标记）。
- 策略 2：SSR 传「数据」不传「完整模板」，客户端模板由 bundle 提供（牺牲首屏）。
- 度量：DSD 页面 HTML 体积预算（模板占比 < 40%），超标走策略 2。

```javascript
// 构建期：SSR 入口的元素实现摇掉模板（hydrate-only 构建）
export const hydrateGoodsCard = /* @__PURE__ */ hydrateOnly(GoodsCard);
// bundle 中不含 template 字符串，DOM 已由 DSD 提供
r
```
