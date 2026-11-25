---
title: [WCN-499] 笔试：实现元素库升级的灰度 AB（按实例分桶 + 指标对比）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-499：笔试：实现元素库升级的灰度 AB（按实例分桶 + 指标对比）。
**题目**：`rollout(version, ratio)`：实例 id hash < ratio → 新版；指标采集分桶（新版/旧版错误率、mount 时长）；判定：新版指标不劣化（错误率 ≤ 1.2×、时长 ≤ 1.15×）→ 自动扩量。

```javascript
function canary(metrics, { errT = 1.2, msT = 1.15 } = {}) {
  const neo = metrics.new, old = metrics.old;
  const errOk = neo.errRate <= old.errRate * errT;
  const msOk = neo.mountP95 <= old.mountP95 * msT;
  if (!errOk || !msOk) return { action: 'shrink', reason: !errOk ? '错误率劣化' : '时长劣化' };
  return { action: 'expand',
    nextRatio: Math.min(1, metrics.ratio * 2) };   // 翻倍扩量
}

```

**评分点**：
- 分桶确定性（hash 实例 id）。
- 双桶指标采集（tag 同 version 区分）。
- 自动扩量判定（双阈值）。
- 劣化自动缩量（回滚语义）。
