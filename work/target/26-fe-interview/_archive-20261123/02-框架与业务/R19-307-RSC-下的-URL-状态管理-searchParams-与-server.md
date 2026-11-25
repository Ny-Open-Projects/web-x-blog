---
title: [R19-307] RSC 下 URL searchParams 状态怎么管理（server 端读取与变更）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-307：RSC 下 URL searchParams 状态怎么管理？
**答**：
- 读取：页面 props.searchParams（服务端直接可用），URL 即状态——刷新/分享不丢。
- 变更：客户端用 useRouter().push/replace 更新查询参数，触发服务端重新渲染该段；筛选变化包 transition 避免闪骨架。
- 细粒度更新：列表筛选高频变更时，客户端乐观过滤 + 服务端确认（transition 保持旧列表显示）。
- 编码规范：数组用重复 key 或逗号约定、空值剔除、分页 reset。
- SSR 缓存影响：searchParams 变化 = 不同缓存 key（页面禁缓存或短缓存时注意命中率）。
