---
title: [WCN-952] 微前端用 WC 做边界，还是 iframe / Module Federation：隔离与体验怎么取舍
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-952：微前端用 WC 做边界，还是 iframe / Module Federation：隔离与体验怎么取舍

**答**：
- 结论先行：三种边界隔离强度递增、体验递减——WC 是「DOM 级共享，弱隔离」、Module Federation 是「模块级共享，中隔离」、iframe 是「进程级强隔离」。
- WC 边界：共享一套 DOM/CSS 变量/路由，体验最自然（同页无缝），但全局污染、样式冲突、JS 全局变量共享风险靠约定治理。
- MF 边界：共享依赖（单例 React）省体积、版本协商灵活，但仍是同一 JS realm，运行时错误可能互相影响。
- iframe 边界：真隔离（独立 realm/安全域），适合不可信第三方或强合规隔离，代价是通信复杂、体验割裂、SEO 差。
- 追问钩子：面试官问「同一个页面既有可信子应用又有第三方插件怎么选」——答：可信的用 WC/MF 保体验，第三方不可信用 iframe 沙箱（sandbox 属性 + postMessage），分层隔离。

```javascript
// 边界选型评分：隔离 vs 体验
const dims = ['isolate', 'ux', 'seo', 'complexity'];
function pick(weights) {
  const opts = {
    wc:   { isolate: 2, ux: 9, seo: 8, complexity: 3 },
    mf:   { isolate: 5, ux: 8, seo: 7, complexity: 5 },
    iframe:{ isolate: 10, ux: 3, seo: 2, complexity: 8 },
  };
  return Object.entries(opts)
    .map(([k, v]) => [k, dims.reduce((s, d) => s + v[d] * (weights[d] || 0), 0)])
    .sort((a, b) => b[1] - a[1])[0][0];
}
console.log(pick({ ux: 2, seo: 1 }));            // wc（重体验）
console.log(pick({ isolate: 3, complexity: -1 })); // iframe（重隔离）
```
