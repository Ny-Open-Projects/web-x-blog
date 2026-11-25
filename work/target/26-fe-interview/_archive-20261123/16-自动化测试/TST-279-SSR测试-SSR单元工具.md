---
title: [TST-279] SSR 测试的常用工具组合与各自定位？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-279：SSR 测试的常用工具组合与各自定位？
**答**：
- renderToString/hydration API：底层一致性测试。
- testing-library + jsdom：组件层双端行为。
- Playwright：真实水合/流式/交互时序（唯一能测真水合的工具）。
- miniflare/wrangler dev：边缘运行时。
- Lighthouse CI：水合性能预算门禁。

```javascript
const toolbox = {
  consistency: 'renderToString vs render + jsdom',
  runtime: 'Playwright（真水合/流式时序）',
  edge: 'miniflare',
  perf: 'Lighthouse CI（TBT/TTI 预算）',
};
r
```
