---
title: [R19-303] 大表单（200 字段）走 Server Action 的性能与体验怎么优化？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-303：大表单走 Server Action 怎么优化？
**答**：
- 分节提交：表单按域拆多个 action（基本信息/地址/发票），每节独立校验保存，避免一次 200 字段 payload。
- 校验分层：客户端即时校验（react-hook-form + zod resolver）挡明显错误，服务端最终校验。
- payload 控制：隐藏字段清理（不传无用字段）、File 单独走直传。
- 体验：分节 action 各自 isPending/成功态；草稿自动保存（防抖 action）防丢失。
- 服务端：action 内事务包整体或分节入库 + 最终提交一致性检查。
