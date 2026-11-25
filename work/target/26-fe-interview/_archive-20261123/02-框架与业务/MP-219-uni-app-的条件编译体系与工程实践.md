---
title: [MP-219] uni-app 条件编译体系与工程实践？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-219：uni-app 条件编译体系？
**答**：
- 语法：#ifdef PLATFORM / #ifndef PLATFORM / #endif，支持 js/css/模板/配置（pages.json）块级与行内。
- 平台常量：H5、MP-WEIXIN、APP-PLUS、MP-ALIPAY 等；组合条件 #ifdef MP-WEIXIN || MP-ALIPAY。
- 工程实践：差异收敛在「适配层」（api/platform.ts），业务代码少写条件编译（避免分支爆炸）；条件编译与 TS 类型配合（平台联合类型收窄）。
- 检查：CI 按端构建跑类型检查，确保某端的独有代码不污染他端编译。
- 反模式：大量 if(平台) 散落业务——用适配器模式替代。
