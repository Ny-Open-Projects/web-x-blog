---
title: [WCN-392] 元素内部的功能开关（灰度元素新行为）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-392：元素内部的功能开关（灰度元素新行为）？
**答**：
- 开关注入：全局配置（window.DS_FLAGS）+ per-element property 覆盖。
- 灰度：新行为按元素实例百分比（实例 id hash）分桶。
- 回退：开关一键回旧行为（新旧实现同元素内共存一版本）。
- 清理：灰度全量后移除旧分支（版本化清理）。

```javascript
const flags = window.DS_FLAGS?.['goods-card'] ?? hash(instanceId) < rollout;  // 分桶
render(flags ? newBehavior : legacy);
r
```
