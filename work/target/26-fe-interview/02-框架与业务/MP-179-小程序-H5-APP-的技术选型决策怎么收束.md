---
title: [MP-179] 小程序、H5、APP 的技术选型决策怎么收束？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-179：小程序、H5、APP 的技术选型决策怎么收束？
**答**：
- **小程序**：微信/支付宝生态内获客与转化（支付/分享/扫码入口），无需安装、迭代快，但受平台管控（包体/审核/API 限制）。
- **H5**：完全开放分发（任意链接可传播）、无审核，但能力弱（支付/推送/性能）且留存差；适合活动页/内容页外链投放。
- **App**：能力上限最高（推送/后台/硬件），留存与品牌最强，但获客成本高、双端维护重。
- 决策模型：按"获客场景 × 能力需求 × 留存诉求"三维打分；常见组合=小程序主阵地 + H5 做分享落地 + App 承接高价值用户。

```yaml
# 技术选型决策矩阵
decision-matrix:
  dimensions: [获客场景, 平台能力, 留存诉求, 迭代速度, 维护成本]
  scores:
    miniprogram: { acquire: 5, capability: 3, retention: 4, speed: 5, cost: 4 }
    h5:          { acquire: 4, capability: 2, retention: 2, speed: 5, cost: 4 }
    app:         { acquire: 2, capability: 5, retention: 5, speed: 3, cost: 2 }
  rules:
    - "生态内交易与裂变 → 小程序优先"
    - "站外投放落地页 → H5，可跳小程序"
    - "高频重度使用与硬件能力 → App"
    - "组合形态：小程序主业务 H5 引流 App 承接核心用户"
```
