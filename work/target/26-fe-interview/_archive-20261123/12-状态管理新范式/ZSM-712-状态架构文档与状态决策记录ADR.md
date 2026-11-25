---
title: [ZSM-712] 状态架构的决策记录（ADR）：为什么每个 store 的存在都要有出处
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-712：状态架构的决策记录（ADR）：为什么每个 store 的存在都要有出处

**答**：
- 状态架构腐化的根源不是技术而是「无据可查」——三个月后没人记得为什么 cartStore 要拆两个、为什么这里禁用 optimistic。ADR（Architecture Decision Record）把决策固化：编号、背景、决策、后果、替代方案被否的原因。
- 状态域的 ADR 模板（轻量版，一个 store/机制一份）：`ID-标题 | 状态背景（谁消费/多大/多频）| 决策（库+形状+更新模式）| 后果（正负面都写）| 备选方案与否决理由`。放在 store 文件头部注释或 docs/adr/ 目录。
- ADR 的验收价值：code review 时「新 store 有没有对应 ADR」是硬门禁；新人上手读 ADR 列表比读代码快十倍；重构时「翻 ADR 确认当初否决了什么」避免走回头路。
- 与 ZSM-550 六问表的关系：六问表是决策「输入」，ADR 是决策「输出存档」；两者合起来是状态治理的文档闭环——评审会记录（决策过程）+ 代码旁注（决策结论）。
- 追问钩子：ADR 的生命周期——superseded（被新决策取代）状态要显式标记并链接新 ADR，旧决策的「否决理由」在新 ADR 里要回应（为什么当时否决的方案现在可行了）。

```markdown
<!-- docs/adr/0007-cart-store-split.md -->
# ADR-0007: 购物车 store 拆分为 cart 与 checkout 两个

## 背景
- cartStore 同时承载「购物车编辑」（高频：增删改）与「结算单计算」（低频、强一致）
- 现状：一次加购触发结算摘要全量重算（见 ZSM-607 分段计时数据：selector 占 86%）

## 决策
- 拆分为 cartStore（items、编辑 action）与 checkoutStore（券、地址、结算计算）
- 两 store 间通信仅通过「结算动作」显式同步，禁止双向订阅
- checkout 使用服务端权威计算，前端只投影

## 后果
- 正面：加购重渲半径缩小 70%（基线 renders 87 → 23）
- 负面：新增跨 store 同步点一处，需要防「车与单不一致」的对账（已有 ZSM-549 对账器）
- 持久化结构变化：persist key 拆分，需 migrate（旧版本 cart 合并恢复）

## 备选否决
- 「保持单 store + selector 拆细」：评估后渲染层 diff 仍是大子树，收益不足 30%
- 「全部迁 Jotai atom」：迁移成本高，团队 Zustand 经验成熟，收益比不划算

## 状态
- adopted 2026-11
```
