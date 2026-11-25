---
title: [TST-270] SSR 应用的测试金字塔如何搭（对比纯 SPA）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-270：SSR 应用的测试金字塔如何搭（对比纯 SPA）？
**答**：
- 底层新增：双端渲染一致性单测 + SSR 快照（renderToString 输出）——SSR 特有底座。
- 中层：路由级集成测试（fetch mock + SSR 渲染整页断言）。
- 顶层：E2E 加 hydration/流式专项（mismatch 检测开着跑全站）。
- 与 SPA 差异：SSR 的「服务端正确性」必须独立验证——浏览器测不到服务端 HTML。

```javascript
const pyramidSSR = {
  L1: '双端一致性单测 + SSR 快照（新增）',
  L2: '路由级 SSR 集成（mock fetch + 整页断言）',
  L3: 'E2E + hydration mismatch 全站巡检（dev 模式告警）',
};
r
```
