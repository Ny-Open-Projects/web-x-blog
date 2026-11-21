---
title: [ARC-571] Cookie 合规与同意管理（GDPR 式）的前端架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-571：Cookie 合规与同意管理
**答**:
- 合同框架：Cookie 分级（必要：登录/会话——免同意；功能：偏好设置；分析：埋点/广告——需同意），同意状态驱动技术脚本加载（未同意分析 cookie → 埋点 SDK 不初始化——同意不仅是弹窗，是数据流开关）。
- 同意管理架构：CMP（同意管理平台）配置（分类/文案/版本）→ 端上同意组件（首次访问展示，可随时改——设置入口常在）→ 同意状态存储（cookie 版本化：政策更新需重新同意）→ 全局 gate（API：consent.check('analytics') 决定加载与上报）。
- 采集联动：埋点 SDK 按同意分级初始化（ARC-154 隐私架构的执行层）、已有数据在撤回同意后的处理（删除请求 NODE-443 联动）。
- 技术细节：必要 cookie 的 SameSite/Domain 最小化（ARC-560）、第三方 cookie 依赖的替代（浏览器逐步禁三方 cookie——用户识别改第一方上下文/替代 ID 方案的前瞻）。
- 演练与审计：同意状态与实际采集行为的一致性审计（说没同意就不采——自动巡检：同意关闭后是否仍有分析上报）。
```javascript
// 同意 gate
consent.init({ policyVersion: 3 });
if (consent.granted('analytics')) initTracker();                 // 同意驱动初始化
track = consent.granted('analytics') ? track : noop;             // 全局 gate
// 巡检：模拟未同意会话 → 断言无 analytics 上报（一致性验证）
```
