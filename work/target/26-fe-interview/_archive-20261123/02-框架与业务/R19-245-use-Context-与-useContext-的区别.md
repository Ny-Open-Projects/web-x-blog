---
title: [R19-245] use(Context) 与 useContext 的区别是什么？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-245：use(Context) 与 useContext 的区别是什么？
**答**：
- 功能等价（读取 context 当前值），区别在约束：use 可以在条件分支/循环中调用，useContext 必须顶层。
- 设计动机：统一 use 作为「资源读取」原语（Promise、Context、未来更多资源），减少 API 面积。
- 推荐：React 19 中新代码可用 use(Context)；useContext 保留兼容。
- 性能语义相同：context value 变化都会触发订阅组件重渲染，优化手段（拆分 context/memo provider）不变。
- 细节：use 不接受 hook 形式的参数（不是 use(xxx) 就行），必须是 Context 对象或 Promise 或 thenable。
