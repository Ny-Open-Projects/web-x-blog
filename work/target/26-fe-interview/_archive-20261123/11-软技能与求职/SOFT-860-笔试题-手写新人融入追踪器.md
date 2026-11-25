---
title: [SOFT-860] 手写 onboardingTracker：新人 30 天融入的里程碑追踪（信息包/首任务/孤立信号/关系牵引）、预警？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-860：手写 onboardingTracker：新人 30 天融入的里程碑追踪（信息包/首任务/孤立信号/关系牵引）、预警

**需求与边界**：
- 实现 onboardingTracker(newcomer)。
- 边界要求：① 30 天里程碑：W1 信息包+首任务设计（SOFT-843）/W2 关系牵引（介绍协作方+跨团队同行）/W4 独立交付验证；② 孤立信号检测：协作数据（被@次数/发言次数/评审参与）低于新人基线→预警（SOFT-806）；③ 每里程碑有 mentor 动作与验收；④ 30 天总评估输出。

**答**：
```javascript
function onboardingTracker(n, { today = Date.now() } = {}) {
  const start = n.startAt;
  const day = Math.round((today - start) / 864e5);
  const MILESTONES = [
    { w: 1, action: '信息包（地图/术语/公约 SOFT-843）+首任务设计（跳一跳够到）',
      verify: '首任务开工且新人能复述目标（SOFT-585校准）' },
    { w: 2, action: '关系牵引：介绍关键协作方+首次跨团队同行',
      verify: '与≥3个协作对象建立联系' },
    { w: 4, action: '独立交付验证', verify: '首个完整交付完成（SOFT-638）' },
  ];
  const milestones = MILESTONES.map(m => ({
    ...m, due: new Date(start + m.w * 7 * 864e5).toISOString().slice(0, 10),
    status: day >= m.w * 7 ? (n.completed?.includes(m.w) ? 'done' : '⚠️逾期') : '待办' }));
  const baseline = n.peerBaseline ?? { mentions: 5, speech: 3 };
  const isolated = (n.collab?.mentions ?? 99) < baseline.mentions * 0.5
    || (n.collab?.speech ?? 99) < baseline.speech * 0.5;
  return { milestones, day,
    isolation: isolated
      ? { alert: '孤立信号：协作数据低于新人基线50%——'
          + '立即1:1+关系牵引加强（SOFT-806/843）' }
      : null,
    note: '前30天体验决定留存与投入（SOFT-638）——
      融入是杠杆最高的团队投资' };
}
```

**评分点**:
- 30 天里程碑带 mentor 动作与验收（SOFT-843 责任清单工具化）。
- 孤立信号检测（协作数据 vs 新人基线 50%——SOFT-806 落地）。
- 逾期状态显式标注（里程碑不烂尾）。

