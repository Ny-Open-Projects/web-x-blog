---
title: [AV-118] 自建 SFU 还是直接用云服务（TRTC/Agora）？怎么决策？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-118：自建 SFU 还是直接用云服务（TRTC/Agora）？怎么决策？（高频）
**答**：
- 云服务买"结果"：弱网对抗、全球节点、回声消除全打包，按分钟计费，上线快、SLA 有保障。
- 自建买"控制权"：成本随规模摊薄、数据不出内网、深度定制，但要养传输协议/SFU/运维团队。
- 经验阈值：日活几千、无特殊合规要求 → 云服务；日活十万级以上 RTC 成本占比高 → 评估自建或混合。
- 混合策略：核心业务用云服务保稳，海外/灰度流量自建；云服务做保底链路，防止自建故障全灭。
- 评估维度：全球节点、弱网算法、多端 SDK 成熟度、计费模式、SLA 与账单透明度、数据合规。

```typescript
// 选型评分模型：把决策变成可复算的表格
interface Option {
  name: string;
  monthlyCost: (minutes: number) => number;
  controlScore: number;  // 控制权 1-9
  speedScore: number;    // 上线速度 1-9
  opsCost: number;       // 运维负担 1-9
}
function evaluate(options: Option[], monthlyMinutes: number) {
  return options.map((o) => {
    const cost = o.monthlyCost(monthlyMinutes);
    return { name: o.name, cost, score: (o.controlScore + o.speedScore) * 0.4 - o.opsCost * 0.2 - cost / 1e5 };
  }).sort((a, b) => b.score - a.score);
}
const cloud: Option = { name: 'TRTC', monthlyCost: (m) => m * 9.9, controlScore: 3, speedScore: 9, opsCost: 2 };
const selfHosted: Option = { name: '自建mediasoup', monthlyCost: () => 30000, controlScore: 9, speedScore: 4, opsCost: 7 };
// console.log(evaluate([cloud, selfHosted], 5_000_000)); // 月 500 万分钟量级 自建开始占优
```
