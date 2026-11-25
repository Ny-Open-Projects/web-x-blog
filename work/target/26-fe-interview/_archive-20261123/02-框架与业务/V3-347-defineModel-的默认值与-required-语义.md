---
title: [V3-347] defineModel 的默认值与 required 语义怎么正确使用？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-347：defineModel 的默认值与 required 语义怎么正确使用？
**答**：
- `defineModel({ default: 0 })` 编译为带 default 的 prop：父组件未绑定时读 default，子组件 set 时正常 emit。
- default 的坑：仅「父组件从未传值」时生效；父组件显式传 `undefined` 不等于未传（走 undefined），组件内部用 `props.xxx ?? default` 区分时要谨慎。
- `defineModel({ required: true })` 生成 prop 校验警告：父组件漏绑 v-model 时开发环境告警，避免静默失效。
- get 转换：`defineModel({ get: v => v ?? 0 })` 读取时兜底，适合「父传 null 但子组件要数字」的边界。
- 本地乐观修改：父未绑定时的本地 set 只改内部副本，不产生双向同步——文档明确这是「本地状态」，不要依赖它通知父组件。
