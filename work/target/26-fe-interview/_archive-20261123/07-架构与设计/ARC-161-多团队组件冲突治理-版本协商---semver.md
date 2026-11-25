---
title: [ARC-161] 多团队组件冲突治理（版本协商 / semver 约定 / owner 机制）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-161：多团队组件冲突治理（版本协商 / semver 约定 / owner 机制）如何设计？
**答**：
- 冲突根源治理：共享包必须有唯一 owner（CODEOWNERS 声明），无 owner 的共享包禁止存在；两个团队都想改同一个包，说明包的边界设计错了，先拆包再谈协作。
- semver 约定实操：breaking change 提前发 next 版本 + 变更公告，给依赖方一个版本窗口（如支持 N-1 两个月）；deprecated API 保留 console.warn 至少一个版本。
- 多版本共存是缓冲带：monorepo 允许短期多版本共存（scoped alias），但纳入"重复依赖看板"，限期收敛——共存是过渡态不是稳态。
- 仲裁机制：版本冲突升级到架构例会裁决（基于使用量/迁移成本数据，不拍脑袋）；重大 breaking（如 react 大版本）由基建团队主导 lockstep 升级（全仓统一窗口）。

```yaml
# 共享包治理配置
shared_package_policy:
  ownership:
    CODEOWNERS:                           # 唯一 owner 强制
      - path: packages/ui/**        owner: platform-ui-team
      - path: packages/trade/**    owner: trade-fe-team
    rule: "无 owner 的包不允许被跨团队引用（CI 校验）"
  semver_contract:
    breaking:  发 next 预发布 + 公告，依赖方迁移窗口 60 天
    deprecated: 保留至少一个 minor 版本并 console.warn 指引新 API
    support_window: 当前版本 + N-1（两个月）
  coexistence:
    allow: monorepo 内短期多版本（alias 引用）
    board: 重复依赖看板（按包聚合多版本数量），超 1 个 minor 差异标红
    deadline: 每条共存记录必须带收敛排期
  lockstep:                                 # 大版本统一升级
    scope: [react, vue, major-ui-libs]
    mode: 基建团队开分支统一升级 + 全仓回归 + 一次性合入
  arbitration:
    - 团队间冲突 → 架构例会，输入：使用量数据 + 双方迁移成本评估
    - 裁决记录进 ADR（编号可追溯）
```
