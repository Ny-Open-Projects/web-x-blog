---
title: [ARC-016] feature 目录 vs 类型目录（components/hooks/services），如何选择与演进？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-016：feature 目录 vs 类型目录（components/hooks/services），如何选择与演进？
**答**：
- 类型目录（按技术分层）适合小项目：直观、上手快；但一个需求要跳 4 个目录，且"哪个组件属于哪个功能"会逐渐失控。
- feature 目录（按业务内聚）适合中大型：删功能=删目录，边界清晰；需要纪律防止跨 feature 乱引。
- 演进路径：MVP 用类型目录 → 出现 3+ 并行团队/复杂域后迁移到 feature 目录，迁移按域逐步进行。

```text
方案A 类型目录（技术视角）              方案B feature 目录（业务视角）
src/                                    src/
├── components/                         ├── features/
│   ├── OrderCard.vue                   │   ├── order/          # 交易域
│   ├── AddressForm.vue                 │   │   ├── components/
│   └── SkuPicker.vue                   │   │   ├── hooks/
├── hooks/                              │   │   ├── api.ts
│   ├── useOrder.ts                     │   │   └── index.ts    # 公共出口
│   └── useAddress.ts                   │   ├── address/        # 地址域
├── services/                           │   └── logistics/      # 物流域
│   ├── order.ts                        ├── shared/             # 跨域公共（受管控）
│   └── address.ts                      │   ├── components/
└── api/                                │   └── utils/
    └── index.js                        └── app/                # 组装入口（路由/全局Provider）
# 取舍：A 改一个需求跨 3 个目录；B 删除 address 功能=删一个目录，依赖被 index.ts 卡住
```
