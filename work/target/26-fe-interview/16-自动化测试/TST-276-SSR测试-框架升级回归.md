---
title: [TST-276] SSR 框架大版本升级（Next 14→15）的回归测试方案？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-276：SSR 框架大版本升级（Next 14→15）的回归测试方案？
**答**：
- 快照对照：升级前后对全站关键页面 SSR HTML 做「语义 diff」（忽略时间戳/随机 id）。
- RSC payload 格式变化关注：客户端导航行为回归（升级后 flight 格式可能变化）。
- 分阶段：先并行部署新版本子域，自动化双跑对比再切流。
- 升级专项清单：hydration/流式/缓存/SEO 四类断言全绿才切。

```javascript
// 升级双跑对比
for (const path of criticalPaths) {
  const [a, b] = await Promise.all([fetch(v14Host + path), fetch(v15Host + path)]);
  expect(semanticDiff(a, b)).toEqual([]);   // 忽略 _rsc 随机 id
}
r
```
