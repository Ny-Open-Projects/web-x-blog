---
title: [R19-309] Next SSR 的 HTML 流与 RSC payload 流是什么关系？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-309：HTML 流与 RSC payload 流的关系？
**答**：
- 首次访问：服务端输出 HTML 流（用户可看）+ 内嵌 RSC payload（script 标签，水合数据），两流同源同步。
- 客户端导航：不再请求 HTML，只请求 RSC payload 流（轻量），React 用它更新客户端树。
- 同步机制：payload 中的引用与 HTML 中的 DOM 对齐，水合时按边界匹配。
- 优化含义：payload 体积影响导航速度、HTML 影响首访——分别预算。
- 调试：View Source 看 HTML + script payload；Network 看 .rsc/.flight 请求。
