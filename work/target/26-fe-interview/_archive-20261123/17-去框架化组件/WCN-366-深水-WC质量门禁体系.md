---
title: [WCN-366] 元素库的「合并门禁 vs 发布门禁」双层设计？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-366：元素库的「合并门禁 vs 发布门禁」双层设计？
**答**：
- 合并门禁：行为测试/类型/lint/a11y axe——快、准、阻塞。
- 发布门禁：多浏览器矩阵/视觉快照/SSR DSD 快照/性能预算/文档 demo——全量慢速。
- 发布门禁在合并后异步跑（跑完才允许 publish）。
- 门禁豁免：hotfix 逃生通道（审计留痕 + 事后补跑）。

```javascript
const gates = {
  merge: ['behavior', 'types', 'lint', 'axe'],
  release: ['matrix', 'visual', 'dsd-snapshot', 'perf-budget', 'docs-demo'],
  escape: 'hotfix 留痕 + 事后补跑',
};
r
```
