---
title: [FRP-248] 表单方案：受控、非受控、Headless 表单的判据？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-248：表单方案的判据？
**答**：
- 受控（antd Form/v-model）：与 UI 强联动、校验即时——适合中后台标准表单；代价：每键重渲染。
- 非受控 + ref 提交（HTML 原生 + Server Action）：性能好、渐进增强——适合提交型表单（登录/下单）。
- Headless（react-hook-form）：非受控内核 + 声明式校验注册——大表单性能与类型安全的平衡点。
- 判据：字段数（>50 考虑 RHF）、校验复杂度（联动校验选受控引擎）、提交模式（action 原生 vs AJAX）。
- Vue 侧：v-model 协议 + VeeValidate/zod 统一校验层。
