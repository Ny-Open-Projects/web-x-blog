---
title: [R19-271] React Compiler 对并发渲染有什么帮助？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-271：React Compiler 对并发渲染有什么帮助？
**答**：
- 自动 memo：编译期分析依赖，给组件/hook 插入 memo 与 useMemo，减少无效重渲染——并发渲染的成本大头（重渲染）被自动压缩。
- 依赖正确性：编译器识别闭包依赖，修复漏依赖导致的 stale closure 类竞态。
- 与并发的配合：并发特性要求组件「可重复执行且结果一致」（幂等），Compiler 静态检查推进这一纪律。
- 边界：动态 dispatch、循环依赖、不安全 mutation 的代码编译器会放弃优化并警告——仍是人工代码审查的补充。
- 落地：babel-plugin-react-compiler 渐进启用（按目录），配合 ESLint 插件检查。
