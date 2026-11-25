---
title: [R19-206] useActionState 挂 form action 与手动 onSubmit 两种姿势的差异？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-206：useActionState 挂 form action 与手动 onSubmit 两种姿势的差异？
**答**：
- `form action={formAction}`：React 接管提交、FormData 自动收集、isPending 自动管理、可配合 form 动作属性做渐进增强——首选。
- 手动 onSubmit：适合需要预处理（客户端校验失败直接 return）、非表单控件数据（canvas、地图坐标）的场景，但失去原生 FormData 语义与渐进增强。
- 混合姿势：action 内仍可先跑 zod schema 校验，失败返回 fieldErrors——把校验留在服务端单一来源，客户端校验只做体验优化。
- 细节：手动 onSubmit 里调 formAction(formData) 也能走同一管线（useActionState 返回的 formAction 可直接调用）。
- 面试表达：先说「优先 action 属性，特殊数据源才手动」，体现取舍而非背 API。
