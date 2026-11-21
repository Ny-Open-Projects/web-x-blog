---
title: [R19-202] 多步表单用 useActionState 怎么拆分与聚合状态？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-202：多步表单用 useActionState 怎么拆分与聚合状态？
**答**：
- 每一步一个独立 useActionState（各自 action + state），或单一 action 按 step 字段分派——按域拆分可避免一个巨型 reducer。
- 跨步数据用 URL searchParams 或隐藏字段随 FormData 传递，服务端校验完整链路（不信任前端只传增量）。
- 聚合状态：外层容器用 useReducer 管 step/current，各步 actionState 挂在对应表单上，提交成功才前进。
- pending 语义：useActionState 的第三项 isPending 只覆盖当前表单的 action 执行期，步间跳转的导航 pending 用 useTransition 补。
- 坑：步内字段错误要在 state（prev + errors）中回填，action 返回 { fieldErrors, values } 双向绑定，避免错误后清空用户输入。
