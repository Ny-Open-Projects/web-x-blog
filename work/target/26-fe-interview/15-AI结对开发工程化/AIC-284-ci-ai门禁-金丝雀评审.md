---
title: [AIC-284] 新的评审提示词/模型上线怕翻车，如何做「评审金丝雀」发布？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-284：新的评审提示词/模型上线怕翻车，如何做「评审金丝雀」发布？
**答**：
- 灰度范围：先只跑 5% PR（低风险模块），新旧版本并行评审但只有旧版本结果生效。
- 对比指标：误报率、采纳率、评审耗时、漏放（人审补充发现）对比。
- 影子评审双跑两周，指标不劣化才逐步放量；劣化自动回退旧版。
- 保留对照期数据用于复盘提示词改动的影响。

```javascript
async function shadowReview(pr: PR) {
  const [stable, canary] = await Promise.all([reviewV1(pr), reviewV2(pr)]);
  log('canary-compare', { pr: pr.id, stable, canary }); // 只记录不生效
  return pr.isInCanary(0.05) ? stable : stable;          // 一律返回 stable
}
r
```
