---
title: [AGT-677] 评测通过的新提示词上线后，线上如何验证并回写评测体系？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-677：评测通过的新提示词上线后，线上如何验证并回写评测体系

**答**：
- 上线即实验：新提示词灰度上线自动挂 AB 分流（会话级粘性），线上指标（采纳率/负反馈/轮次）与离线分数双轨观察，任一恶化即回滚。
- 回写机制：灰度期样本自动回流（正例进回归集、负例进失败库+归因），灰度结论写进提示词版本档案——下一个人能看到"v14 线上采纳率 -3% 被回滚"的完整故事。
- 线上离线偏差跟踪：每个版本的「离线分数变化 vs 线上指标变化」散点记录，长期偏差大的评测维度要重修判据。

```javascript
async function promptCanary(vNew) {
  const exp = abAssign({ key: `prompt-${vNew}`, sticky: 'session' });
  const metrics = await watch(exp, ['adoption', 'dislikeRate', 'turns'],
    { autoRollback: true });
  await reflux(exp.samples);                      // 样本回写
  archive(vNew, { offline: vNew.evalScore, online: metrics,
    verdict: metrics.pass ? 'promoted' : 'rolled_back' });
  trackAlignment(vNew.evalDelta, metrics.delta);  // 偏差散点
}
```

