---
title: [RBL-283] Native 构建工具的版本发布与 ABI 兼容管理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-283：Native 构建工具的版本发布与 ABI 兼容管理

**答**:
- 双版本节奏：JS API（npm semver）与 Native 二进制（可选版本矩阵）——绑定关系声明（JS 包指定支持的 binding 版本范围），不匹配报错而非静默错行为
- 平台包分发：optionalDependencies 平台包（@tool/darwin-arm64 等）按需安装，减小安装体积；CI 预下载校验
- ABI 稳定性策略：跨边界数据结构（NAPI 结构体）冻结为稳定面，内部重构不影响；破坏 ABI 时 major + 平滑期双支持
- 回滚能力：binding 版本锁进 lockfile；出问题 pin 回旧 binding（JS 包版本对应关系表）

```text
发布清单：JS 包 semver ↑ + 平台 binding 矩阵上传 + 绑定关系声明 + changelog（含 ABI 变更）
安装校验：require('@tool/binding') 报版本不匹配 → 明确提示重装
```
