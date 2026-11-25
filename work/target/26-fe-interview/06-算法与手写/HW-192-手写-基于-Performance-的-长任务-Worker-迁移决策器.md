---
title: [HW-192] 手写 Worker 迁移决策器——采集热点函数耗时，自动判断"值得迁移"并生成迁移报告？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-192：手写 Worker 迁移决策器——采集热点函数耗时，自动判断"值得迁移"并生成迁移报告？
**答**：PER-386 判定公式的自动化：采集候选函数的耗时与参数序列化体积 → 计算"数据/计算比"与净收益 → 输出迁移建议报告（值得迁移/不值得/需改造数据常驻）→ 迁移后实测对照验证预测。

```javascript
function migrationScore({ fnTimeMs, payloadKB, transferable = false }) {
  const cloneMs = transferable ? 1 : payloadKB / 100;     // 每百 KB 约 1ms clone（经验系数，实测校准）
  const roundTrip = cloneMs * 2;                          // 传过去 + 传回来
  const netGain = fnTimeMs - roundTrip - 1;               // -1ms 调度开销
  const ratio = payloadKB / fnTimeMs;                     // 数据/计算比
  if (netGain <= 0) return { verdict: 'skip', reason: `通信成本(${roundTrip}ms)吃掉收益`, ratio };
  if (ratio > 100) return { verdict: 'resident',          // 数据常驻模式（PER-386）
    reason: `数据/计算比 ${ratio}KB/ms 过高 → 数据常驻 Worker，只传指令` };
  return { verdict: 'migrate', reason: `净收益 ${Math.round(netGain)}ms/次`, netGain };
}
// 采集（PER-298 热点排行喂入）：
// const report = hotFunctions.map((f) => ({
//   name: f.name, ...migrationScore({ fnTimeMs: f.selfMs, payloadKB: estimatePayload(f) }),
// })).sort((a, b) => (b.netGain ?? 0) - (a.netGain ?? 0));
// 输出：迁移优先级排行 + 每项 verdict/reason —— 迁移决策从"感觉"变"公式"
// 验证：迁移后实测端到端耗时 vs 预测 —— 偏差 > 30% 时校准 clone 系数
```

**评分点**：
- 迁移评分公式（净收益 = fnTime - 2×clone - 调度）与三分支 verdict——本题核心。
- 数据/计算比触发"数据常驻"建议（PER-386 联动）。
- 采集来源（热点排行）与迁移后验证校准系数。
- transferable 时 clone≈0 的分支处理。
