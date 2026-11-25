---
title: [WCN-140] 五大编译器路线对比：Solid、Vue Vapor、Svelte 5、Qwik、React Compiler 的定位差异？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-140：五大编译器路线对比：Solid、Vue Vapor、Svelte 5、Qwik、React Compiler 的定位差异？

**答**：
- Solid：编译定位动态点 + 运行时 signals，组件只跑一次；表达力最强，心智（解构丢响应）需学习。
- Vue Vapor：Vue 生态内的"无 VDOM 编译目标"，与现有 vdom 混用渐进迁移；语义与 Vue ref 一致。
- Svelte 5：runes 语法糖 + 信号内核，编译产物极小；生态相对小，适合组件库/独立产品。
- Qwik：resumability 重新定义 SSR 成本模型，交互代码全切片；适合内容/电商首屏，JS 执行模型变化最大。
- React Compiler：不改运行时模型，编译期自动 memo；兼容性最好、收益上限有限。
- 共同趋势："运行时少做事"——或省掉重跑（Solid/Vapor/Svelte），或省掉启动（Qwik），或缓存重跑（React）。

```text
            更新粒度      SSR 模型       心智成本    生态
Solid       表达式级      SSR+水合        中          中
Vapor       表达式级      复用 Vue SSR    低(Vue用户) 大(Vue)
Svelte5     表达式级      SSR+水合        低          中
Qwik        任务级        Resumable       高          小
ReactC      子树级(缓存)  RSC+水合        极低        极大(React)
```
