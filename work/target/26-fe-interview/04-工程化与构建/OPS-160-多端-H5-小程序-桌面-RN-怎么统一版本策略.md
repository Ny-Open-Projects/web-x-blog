---
title: [OPS-160] 多端（H5/小程序/桌面/RN）怎么统一版本策略？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-160：多端（H5/小程序/桌面/RN）怎么统一版本策略？
**答**：
- 版本唯一事实源：monorepo 根 package.json 的 version 是 release train 编号，各端 build 号独立递增（微信审核要求 build 号单调）。
- 各端发布节奏天然不同：H5 随时发、小程序审核制、Electron 走更新通道、RN 热更受 native 壳版本约束——统一的是"迭代编号"而不是"发布日期"。
- 兼容基线取最低版本端：接口与协议按兼容矩阵测试，保证任意版本组合可用。
- 小程序审核是节奏约束项：提前 3 天提审，CI 盯审核状态自动放行发布。
- 版本台账统一可查：任何用户会话能查到其各端版本组合，排障与兼容分析的基础（OPS-165）。

```json
{
  "multi_platform_versioning": {
    "version_source_of_truth": "monorepo 根 package.json version 作为 release train 编号，各端 build 号独立递增",
    "platforms": {
      "h5":        { "version": "1.42.0", "release": "随时发布", "rollback": "版本目录切换（OPS-140）" },
      "mp_weixin": { "version": "1.42.0", "build": 821, "release": "审核制，1-24h 延迟", "rollback": "回退历史线上版本（有审核窗口风险）" },
      "electron":  { "version": "1.42.0", "channel": "stable", "release": "自动更新灰度推送", "rollback": "强制降级通道" },
      "rn_app":    { "version": "1.42.0", "release": "热更 bundle 需匹配 native 壳版本" }
    },
    "rules": [
      "各端不必同天发布，但同一次产品迭代共享同一个 release train 编号",
      "小程序提前 3 天提审，CI 轮询审核状态，通过后自动发布",
      "接口兼容以最低版本端为基准，发布前跑兼容矩阵用例",
      "版本台账统一查询：任意用户会话可查其各端版本组合"
    ]
  }
}
```
