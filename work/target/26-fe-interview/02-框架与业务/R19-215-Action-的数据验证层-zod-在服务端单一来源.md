---
title: [R19-215] 为什么说数据校验「服务端单一来源」？zod 在 Action 中怎么组织？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-215：为什么数据校验要以服务端为单一来源？
**答**：
- 客户端校验只优化体验（即时反馈、减少无效请求），安全与正确性必须在 action 服务端校验——客户端输入永远不可信。
- 组织方式：schema 定义在共享包（同构），服务端 parse、客户端复用同一 schema 做即时校验，规则只写一份。
- Action 模式：`const parsed = schema.safeParse(Object.fromEntries(fd))`，失败返回 `{ ok:false, fieldErrors: flattenError(parsed.error) }`，UI 按 field key 回显。
- 深层结构（数组字段、嵌套对象）在 schema 中表达，避免手写循环校验。
- 面试亮点：说明「校验位置决定攻击面」——只校验前端的表单接口等于裸奔。
