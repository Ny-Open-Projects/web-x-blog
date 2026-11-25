---
title: [V3-504] Vue3 渐进迁移：从 Options API 与 Vue2 的策略
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 迁移]
type: 面试题
---

## V3-504：Vue3 渐进迁移：从 Options API 与 Vue2 的策略

**答**：
- 兼容构建：@vue/compat（Vue3 的 Vue2 兼容模式）——逐组件迁移，compat 按「明确兼容/警告/不兼容」分类 API 行为；迁移完成移除 compat
- 迁移顺序策略：工具层先行（utils/组合函数与框架无关）→ 叶子组件 → 容器组件 → 路由/状态层——依赖越少越先迁
- Options API 与 Composition API 共存：Vue3 完全支持 Options——迁移可以「组件内渐进改写」而不是全仓一次性改；新代码规范 composition，老代码按需
- Vue2 特有依赖替换清单：filter（移除→方法/computed）、$listeners（并入 attrs）、事件总线（移除→ mitt/Provide）、Functional 组件语法变更
- 度量与风险：迁移分支按模块合入 + 每模块回归测试；compat 模式的运行时性能劣化可接受（迁移期临时态）

```text
迁移路线:
  W1: 依赖盘点(filter/总线/functional) + compat 构建
  W2~N: 按模块迁移(叶子→容器), 每模块: 改写 → compat 警告清零 → 回归
  收官: 移除 @vue/compat, 全量 composition 规范
```
