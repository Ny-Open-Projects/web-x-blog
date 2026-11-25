---
title: [AGT-613] Agent 新版本（新提示词/新模型）灰度时，可观测怎么支撑放量决策？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-613：Agent 新版本（新提示词/新模型）灰度时，可观测怎么支撑放量决策

**答**：
- 灰度看板对比组：实验组 vs 对照组在完成率/采纳率/成本/延迟四维实时对比 + 置信区间（样本小的时候不要被噪声骗），达标才放量。
- 每个灰度批次绑定版本指纹（promptVer+modelVer+工具清单哈希），回滚时按指纹精确定位受影响会话。
- 灰度期间强制全采 trace（平时采样），放量决策要有数据可依；放量后回到常规采样。

```javascript
function canaryDashboard(exp) {
  return compare(exp.treat, exp.ctrl, [
    'taskDoneRate', 'adoptionRate', 'costPerTask', 'p95Latency',
  ]).map(m => ({ ...m,
    ci: wilsonCI(m.treat),           // 小样本置信区间
    verdict: m.ci.lower > m.ctrl ? 'pass' : m.ci.upper < m.ctrl ? 'fail' : 'pending',
  }));
}
// 版本指纹：回滚时精确定位
const fp = hash([promptVer, modelVer, toolListHash].join('|'));
```

