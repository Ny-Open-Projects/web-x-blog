---
title: [WCN-337] DSD 内容的视口裁剪（长列表 SSR 只渲染可视区）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-337：DSD 内容的视口裁剪（长列表 SSR 只渲染可视区）？
**答**：
- SSR 也不知道视口——按「首屏预算」渲染前 N 项 DSD + 其余占位（占位高度估算防 CLS）。
- 占位协议：data-total-count + data-item-height → 客户端水合虚拟列表接管。
- 风险：估算高度偏差 → CLS；策略：服务端精确测高（渲染时统计）下传。
- 适用：详情页相关推荐等「首屏可控 + 尾部可截断」列表。

```javascript
<ds-list data-total-count="200" data-item-height="88">
  <template shadowrootmode="open"><!-- 前 10 项 DSD --></template>
</ds-list>
<!-- 客户端接管后挂虚拟列表，用元数据还原剩余项 -->
r
```
