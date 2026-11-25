---
title: [V3-350] props 运行时校验的成本与工程策略是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-350：props 运行时校验的成本与工程策略是什么？
**答**：
- 运行时校验（validator 函数、type 数组）只在开发环境告警，生产仍执行但无意义输出；高频更新的组件 props 校验是纯开销。
- 类型安全主力应是 vue-tsc（编译期），运行时校验只保留「接口边界」：如深层数据结构（列表项 shape）在渲染前断言。
- 对象/数组 prop 的 default 必须是工厂函数 `default: () => ({})`——这是常考易错点。
- 复杂校验推荐 props 定义 + Zod：defineProps 用泛型，数据源处用 schema 解析，避免双份维护。
- 生产构建可以把 validator 抽到 `__DEV__` 分支让 DCE 摇掉，省高频路径开销。
```javascript
defineProps<{ list: Item[] }>() // 类型层为主
// 数据入口用 zod 解析，组件内不再重复校验
```
