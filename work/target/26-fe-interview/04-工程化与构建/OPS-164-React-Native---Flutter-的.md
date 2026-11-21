---
title: [OPS-164] React Native / Flutter 的发布模型与纯前端有什么差异？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-164：React Native / Flutter 的发布模型与纯前端有什么差异？
**答**：
- 共同点：native 壳走应用商店审核（节奏以周计），JS/Dart 层有热更能力可绕过审核（须注意商店政策）。
- RN：JS bundle 热更成熟（CodePush/自建 pushy），灰度按设备放量、可秒级回滚（服务端切回旧 bundle）；bundle 必须声明兼容的最低 native 版本。
- Flutter：Dart AOT 编译，原生不支持 JS 式热更；合规通道内用 shorebird 类方案或接受发版节奏。
- 热更 bundle 与商店版本交替期要设上限（如 4 周），超期强制发新 native 版，防止热更与壳版本组合爆炸。
- 热更同样进制品库（版本/哈希/回滚记录，OPS-138），崩溃率联动放量——热更是发布不是补丁。

```yaml
# RN / Flutter 发布差异与热更治理
react_native:
  native_release: 走 App Store / 应用市场审核，节奏以周计
  bundle_hotfix:
    - CodePush / 自建 pushy：JS bundle 与资源热更（注意商店政策边界）
    - 灰度：按设备号放量 5% → 50% → 100%，与崩溃率监控联动
    - 强制匹配：bundle 声明兼容最低 native 版本，壳不匹配不加载
    - 回滚：服务端指向切回旧 bundle，客户端下次启动生效
flutter:
  - Dart AOT 编译，原生不支持 JS 式热更
  - 合规通道内方案：shorebird 代码推送，或接受发版节奏
shared_rules:
  - 热更 bundle 进制品库管理（版本 / sha256 / 回滚记录，OPS-138）
  - 热更与商店版本交替期最长 4 周，超期强制发新 native 版
  - 新 bundle 崩溃率超阈值自动暂停放量（发布联动可观测性，OPS-187）
```
