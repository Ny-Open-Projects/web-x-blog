---
title: [R19-113] 大型 React 项目目录怎么组织？feature-first 是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-113：大型 React 项目目录怎么组织？feature-first 是什么？
**答**：
- feature-first：按业务特性切片，每个 feature 目录内聚 api/components/hooks/store，自治闭环。
- 反面是 layer-first（全局 components/hooks 两大箩筐）：改一个需求要横跨五六个顶层目录，feature 间依赖随意。
- 约束规则：跨 feature 引用只能走 index.ts 公共出口；与业务无关的通用层沉到 shared。
- app/ 目录只做路由与组装，不含业务逻辑，方便框架迁移。

```javascript
// feature-first 目录组织
// src/
//   app/                # 路由与页面组装层，只做编排
//   features/           # 业务特性，每个目录自治
//     order/
//       api/            # 该特性的请求封装
//       components/
//       hooks/
//       store/          # 该特性的 slice
//       index.ts        # 公共出口，跨特性只从这里引
//   shared/             # 与业务无关的通用层
//     ui/               # 基础组件库
//     lib/              # 工具函数
//     hooks/            # 全局通用 hooks

// features/order/hooks/useOrderDetail.ts —— 从公共出口引用其他 feature
import { useUser } from '@/features/user';   // 只能走 index.ts，禁止深入内部路径
import { fetchOrder } from '../api';         // 本 feature 内相对引用

export function useOrderDetail(orderId) {
  const { user } = useUser();
  return useRequest(() => fetchOrder(orderId, user.id));
}
```
