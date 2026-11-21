---
title: [AV-188] 音视频 SDK 的版本升级策略怎么做？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-188：音视频 SDK 的版本升级策略怎么做？（高频）
**答**：
- 风险特征：媒体栈横跨浏览器内核行为、native SDK、信令协议三层，任何一层不兼容都是线上事故。
- 策略：语义化版本 + 协议版本协商（信令握手带 protocolVersion，新旧共存期双向兼容）。
- 灰度机制：按流量灰度（1%→10%→100%），灰度期对比 QoE 基线（首帧/卡顿/建连成功率），劣化自动暂停。
- 兼容层：SDK 内置 adapter（旧协议转新协议）；服务端支持 N-1 版本；强制升级只在破坏性变更且给足迁移期。
- 回滚预案：CDN 保留版本化旧版文件，客户端版本可由配置下发指定——回滚 = 改配置。

```json
{
  "sdk-release-policy": {
    "versioning": "semver 加信令 protocolVersion 协商",
    "server-compat": "支持 N-1 版本",
    "canary": { "ramp": [1, 5, 25, 100], "gate": "首帧与建连成功率劣化超2%自动暂停放量" },
    "rollback": { "mechanism": "配置下发指定版本", "assets": "CDN 版本化路径永久保留旧版" },
    "breaking-change": "提前60天公告 双端兼容期 提供数据迁移脚本"
  }
}
```
