---
title: [SCN-732] SLA 看板的跨团队指标归属与争议怎么治理？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-732：跨团队指标归属怎么治理？
**答**：
- 归属矩阵：每个指标唯一 owner 团队 + 责任范围（代码归因能力）；「接口成功率」这类跨端指标明确主 owner（网关团队）与协同方。
- 争议裁决：指标争议（口径/阈值/归属）走固定流程——证据（口径卡+数据）→ 双方陈述 → 架构委员会裁决 → 口径卡更新；裁决记录沉淀。
- 共担指标设计：全链路指标（如支付成功率）不拆给单团队考核，用「主责 + 协同」模式，避免多方博弈互相甩锅。
- 指标健康度：owner 长期缺位（无响应告警/不参加评审）的指标挂「无主」标记并升级管理层。
- 追问钩子：为什么接口成功率不能同时考核前端和后端——双考核导致双方在口径上博弈（前端说接口慢、后端说前端埋点错），主责制让裁决路径唯一。

```javascript
const ownership = {
  'api.core.success_rate': { owner: 'gateway-team', collaborators: ['web-team', 'app-team'] },
  dispute: async (metric, claim) => {
    const record = await evidence(metric);           // 口径卡+数据
    const ruling = await archCommittee.review({ metric, claim, record });
    await registry.update(metric, ruling);           // 裁决进口径卡
    return ruling;
  },
  orphanCheck: (metric) => !metric.ownerResponding && flagOrphan(metric),
};
```
