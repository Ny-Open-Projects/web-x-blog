---
title: [R19-315] RSC 迁移中最常踩的 10 个坑清单？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-315：RSC 迁移最常踩的坑清单？
**答**：
- 'use client' 传染：一个交互组件把整页拖进 bundle——组合模式（children）下移边界。
- 服务端组件误用浏览器 API（window/document）——报错在构建/渲染期。
- Date/Map 穿透到图表库崩——边界整形 DTO。
- redirect/notFound 在 try/catch 里失效——throw 控制流。
- Router Cache 返回旧数据——staleTime/revalidate 配置。
- action 里读不到 Context——参数显式传。
- 双份状态（RSC 数据又存 Redux）——收敛数据源。
- payload 超大（DTO 未裁剪）。
- Suspense 边界滥用整页闪烁——粒度设计。
- middleware 里判断逻辑过重拖慢每个请求——轻量路由级判断，重逻辑进 RSC。
