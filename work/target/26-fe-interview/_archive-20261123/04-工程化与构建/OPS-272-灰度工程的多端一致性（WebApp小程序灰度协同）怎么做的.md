---
title: [OPS-272] 多端灰度协同（Web/App/小程序同一功能同步灰度）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-272：多端灰度协同怎么做的？
**答**：
- 同步挑战：Web 秒级灰度、App 商店天级、小程序审核天级——同一功能三端灰度进度天然错位，跨端体验不一致（Web 有新功能 App 没有）。
- 协同策略：功能级统一 flag（服务端下发，各端 SDK 消费同一决策）——用户维度统一（同用户跨端同分组），端内节奏独立（Web 先验证 App 跟随，SCN-OPS-211）。
- 端能力差异：App 灰度依赖商店放量（不可精细控）——App 端用功能 flag 补偿（版本已发布但功能 flag 未开）。
- 跨端一致性验收：核心旅程跨端行为一致（Web 开了 App 没开的用户提示/降级路径）。
- 追问钩子：为什么跨端灰度要「用户维度统一、节奏独立」——用户维度统一保证实验/体验一致（同用户跨端看到同一版本功能，数据归因干净）；节奏独立承认端发布机制差异（Web 秒级/App 天级）——统一决策源 + 各端消费节奏，是机制差异与体验一致的最优解。

```javascript
// 服务端统一 flag 决策（用户维度）
const decision = flagEngine.evaluateForUser(userId, 'checkout-v2');   // 跨端同决策
// 各端消费
web: { applyImmediate: decision.on },                  // 秒级
app: { applyWhen: storeRamp.includes(appVersion) && decision.on },    // 商店节奏
mini: { applyWhen: miniReleased && decision.on },
// 端差异提示
!appHasFeature && webHasFeature && show('请在 App 最新版体验');
```
