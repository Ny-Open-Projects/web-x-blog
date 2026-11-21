---
title: [R19-208] useActionState 的 isPending 与 useFormStatus 有什么关系与区别？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-208：useActionState 的 isPending 与 useFormStatus 有什么关系与区别？
**答**：
- useActionState 的 isPending：表单组件自己发起的 action 执行中状态，作用域是「这一个 form 的调用方」。
- useFormStatus：在 form 内部的任意子组件读取「父级 form 的提交状态」，作用域是 DOM 层级的 form——按钮 loading、禁用必用它。
- 差异场景：提交按钮在深层子组件（自定义 Input/Button），拿不到 useActionState 的返回值时用 useFormStatus。
- 同时使用不冲突：外层用 isPending 渲染遮罩，按钮内用 useFormStatus 禁用。
- 坑：useFormStatus 必须是 form 的后代（Context 机制），平级组件拿到的是 idle。
