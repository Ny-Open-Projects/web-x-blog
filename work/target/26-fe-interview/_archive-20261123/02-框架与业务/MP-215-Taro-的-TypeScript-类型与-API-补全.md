---
title: [MP-215] Taro 的 TypeScript 类型体系与多端 API 补全怎么做？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-215：Taro 的 TS 类型体系？
**答**：
- Taro API 类型：union 平台返回类型 + 平台差异标注（仅微信支持的 API 有条件类型）。
- 组件类型：多端组件 props 的公共子集 + 平台特有 props（泛型扩展）。
- 条件编译类型：process.env.TARO_ENV 用 const enum/字面量类型支撑类型收窄。
- 实践：业务层封装 `api.safeCall` 统一 fail/success 处理与类型推导；声明文件补充自定义端。
- 价值：多端 API 差异是小程序 TS 的核心痛点，类型系统即文档。
