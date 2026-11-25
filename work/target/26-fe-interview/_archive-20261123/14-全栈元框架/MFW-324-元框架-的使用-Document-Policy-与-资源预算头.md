---
title: [MFW-324] 资源预算头与文档策略（服务端约束客户端）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-324：资源预算头

**答**:
- 思路：服务端随 HTML 下发「预算声明」（Speculation-Rules 预取规则 / Resource Hints / 实验性文档策略）——把性能策略从约定变成协议
- Speculation Rules：预取/预渲染候选路由列表（构建期由导航图生成——高概率下一跳自动 prerender，LCP 近零）——与 Link prefetch 互补（可带 eagerness 分级）
- 资源提示表：preload 关键、preconnect 第三方域、modulepreload 路由 chunk——由构建 manifest 自动注入（手写必漏）
- 约束验收：预取预算（每页 ≤3 prerender——带宽与服务器成本守恒），命中率进 RUM 回看调参

```javascript
// 构建期生成 speculation rules（导航图 top 下一跳）
const rules = { prerender: [{ where: { href_matches: ['/checkout', '/cart'] }, eagerness: 'moderate' }] }
// 注入 <script type="speculationrules"> —— LCP 近零的正式协议
```
