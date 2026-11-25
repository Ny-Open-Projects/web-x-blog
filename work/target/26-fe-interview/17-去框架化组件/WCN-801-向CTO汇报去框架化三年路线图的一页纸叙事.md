---
title: [WCN-801] 面试官：你要向 CTO 用「一页纸」汇报去框架化组件三年路线图，怎么讲？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-801：面试官：你要向 CTO 用「一页纸」汇报去框架化组件三年路线图，怎么讲？

**答**：
- 结论先行：高管不关心 Shadow DOM 原理，只关心「降本、提效、控风险」——一页纸必须是「现状痛点 → 三年目标 → 量化收益 → 风险与所需资源」四段式。
- 第一年打地基：搭 token 管线 + 组件契约 + 试点 3 个业务，目标「新组件 100% 走 WC 平台、复用率提升到 40%」；用「重复造轮子工时」换算成省钱数字。
- 第二年扩量：覆盖 50% 存量页面、跨框架宿主统一、建 CI 与监控门禁，用「发布周期从 2 周缩短到 2 天」体现提效。
- 第三年收官：形成平台化治理（SLA、成本分摊、弃用流程），把团队从「写组件」转为「运营平台」。
- 追问钩子：CTO 大概率问「投多少人、什么时候能看到收益」——要给出每阶段的人力与可验证的里程碑，并把风险（浏览器兼容、迁移阻力）主动摆出来，别等被问。

```javascript
// 一页纸叙事的数据骨架：把技术路线翻译成高管关心的 ROI 语言
const roadmap = {
  pain: { duplicatedComponents: 37, avgBuildWeeks: 2, brandInconsistency: '高' },
  stages: [
    { year: 1, goal: '地基+试点', metric: '复用率 40%', saving: '省 12 人月/年' },
    { year: 2, goal: '扩量+门禁', metric: '覆盖 50% 页面', saving: '发布提速 7 倍' },
    { year: 3, goal: '平台化治理', metric: 'SLA 99.9%', saving: '团队转型为平台运营' },
  ],
  ask: { headcount: 4, budget: 'XX 万/年', risk: ['DSD 兼容', '业务迁移阻力'] },
};
function onePager(r) {
  return [
    `【现状】重复组件 ${r.pain.duplicatedComponents} 个，平均交付 ${r.pain.avgBuildWeeks} 周`,
    ...r.stages.map(s => `【第${s.year}年】${s.goal}｜${s.metric}｜${s.saving}`),
    `【所需】${r.ask.headcount} 人 + ${r.ask.budget}，风险:${r.ask.risk.join('/')}`,
  ].join('\n');
}
console.log(onePager(roadmap));
```
