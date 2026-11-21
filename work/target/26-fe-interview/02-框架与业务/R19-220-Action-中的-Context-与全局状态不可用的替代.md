---
title: [R19-220] 为什么 Server Action 里读不到 React Context？替代方案是什么？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-220：为什么 Server Action 里读不到 React Context？替代方案是什么？
**答**：
- Action 在服务端独立执行，与客户端组件树无渲染关系——Context 是渲染期概念，服务端不存在。
- 替代：语言/租户等环境信息从 cookie/session 读（request 上下文）；user 从 auth() 读；配置从 env 读。
- 需要「客户端状态参与 action」时把值作为参数显式传入（通过 FormData 或参数），保证可序列化。
- 设计含义：服务端逻辑的依赖必须是「请求级可获取」的——推动把全局可变状态收敛到 DB/存储。
- 面试表达：先答「渲染期 vs 请求期的本质差异」，再列替代来源，避免背清单。
