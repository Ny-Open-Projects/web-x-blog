---
title: [WCN-323] 局部水合（islands）与 DSD 元素的结合方式？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-323：局部水合（islands）与 DSD 元素的结合方式？
**答**：
- 静态内容全量 SSR（元素 DSD 直出），交互岛屿按需水合（客户端进入视口/交互才加载实现）。
- 元素层实现「水合点」协议：data-hydrate="visible|idle|interaction" 声明时机。
- 水合前交互：DSD 静态内容可看，交互事件由「根级委托暂存」到水合完成后回放（或直接提示）。
- 成本核算：岛屿化节省的 JS vs 委托层复杂度——高交互密度页面收益小。

```javascript
<ds-chart data-hydrate="visible" src="/api/chart">
  <template shadowrootmode="open"><div class="skeleton"></div></template>
</ds-chart>
<!-- 进入视口才 import 实现并水合 -->
r
```
