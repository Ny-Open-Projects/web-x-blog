---
title: [ARC-727] Vue2 到 Vue3 的存量迁移策略
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 面试题, 迁移]
type: 面试题
---

## ARC-727：Vue2 → Vue3 迁移

**答**：
- 迁移路径三选一：整体升级（小应用——compat 构建一周迁移）、逐模块迁移（大应用——@vue/compat 渐进）、组件库先行（公共组件库先适配，业务跟随）——按规模选择
- 兼容层（@vue/compat）的角色：Vue2 API 在 Vue3 运行时的兼容模式——「逐文件迁移，每迁移一个文件移除 compat 警告」——警告清单即迁移清单
- 高频破坏点清单：filter 移除、$listeners 并入 $attrs、事件总线移除、v-model 参数变化、函数式组件语法、全局 API 变化（new Vue → createApp）——迁移指南按破坏点组织
- 生态同步升级：vue-router@4/pinia（替换 vuex）/组件库（Element→Element Plus）——生态不配套则迁移不完整
- 深水点：迁移的「行为差异验证」——compat 下跑全量回归 + 线上灰度验证——语法迁移 ≠ 行为一致（patch 语义变化）

```text
Vue2→3 迁移:
  路径: 整体(小) / 逐模块(compat) / 组件库先行
  机制: compat 警告清单 = 迁移清单
  破坏点: filter/$listeners/总线/v-model/函数组件/全局API
  生态: router@4 + pinia + 组件库同步
  验证: compat 回归 + 灰度 (语法≠行为)
```
