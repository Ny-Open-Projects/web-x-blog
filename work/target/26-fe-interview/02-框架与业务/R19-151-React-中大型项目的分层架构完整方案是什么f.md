---
title: [R19-151] React 中大型项目的分层架构完整方案是什么？features 分层与依赖方向怎么约束？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-151：React 中大型项目的分层架构完整方案是什么？features 分层与依赖方向怎么约束？
**答**：
- 推荐结构：`app`（组装/路由/provider）-> `pages`（页面编排）-> `features`（业务用例）-> `entities`（领域模型+api+组件）-> `shared`（ui/utils/request），即 FSD（Feature-Sliced Design）的 React 落地。
- 依赖方向铁律：**只能向下依赖**，`shared` 不 import 任何上层；同层之间不互相 import，跨 feature 复用下沉到 entities/shared。
- 每个 slice 内部再分层：`api / model（store+types）/ ui / index.ts（公共出口）`，外部只能走 index.ts，内部实现不外泄。
- 约束工具化：eslint-plugin-boundaries / import-x 规则禁越层引用，CI 拦截，规范才不会腐烂。

```javascript
// 依赖方向约束 —— eslint 配置 + 目录结构说明
// 目录结构：
// src/
//   app/            # Provider 组装、全局路由、全局样式
//   pages/          # 页面级编排：组合 features，不含业务逻辑
//   features/
//     order-create/ # 一个业务用例一个 slice
//       api/        # 该用例的请求
//       model/      # store / types / 转换函数
//       ui/         # 组件
//       index.ts    # 唯一出口
//   entities/
//     order/        # 领域对象：类型 + api + 展示组件
//   shared/
//     ui/ request/ hooks/ config/

// .eslintrc.cjs —— 用 import 规则把依赖方向变成机器可查
module.exports = {
  overrides: [
    {
      files: ['src/shared/**/*.{ts,tsx}'],
      rules: {
        // shared 是最底层：禁止引用任何上层 slice
        'no-restricted-imports': ['error', {
          patterns: ['@/app/*', '@/pages/*', '@/features/*', '@/entities/*'],
        }],
      },
    },
    {
      files: ['src/features/**/*.{ts,tsx}'],
      rules: {
        // features 只能依赖 entities 和 shared，不能横向 import 其他 feature
        'no-restricted-imports': ['error', {
          patterns: [{
            group: ['@/features/*'],
            message: '跨 feature 复用请下沉到 entities 或 shared',
          }, {
            group: ['@/pages/*', '@/app/*'],
            message: 'features 不能反向依赖页面层',
          }],
        }],
      },
    },
  ],
};

// features/order-create/index.ts —— 唯一出口，控制外泄面
export { OrderCreateForm } from './ui/order-create-form';
export type { OrderCreatePayload } from './model/types';
// 注意：不导出内部 store 与 api，页面层只按出口引用
```
