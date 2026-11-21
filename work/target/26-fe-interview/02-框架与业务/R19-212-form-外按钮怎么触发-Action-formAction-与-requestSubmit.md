---
title: [R19-212] form 外的按钮怎么触发 Action？formAction 与 requestSubmit 的姿势？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-212：form 外的按钮怎么触发 Action？
**答**：
- 方式一：`<button form="myForm">`（原生属性）关联指定 form id，React 对带 form 属性的 submit button 也走 action 管线。
- 方式二：programmatic 提交 `formRef.current.requestSubmit()`——模拟真实提交（触发校验），比 dispatchEvent(submit) 可靠。
- 方式三：直接调用 useActionState 的 formAction(formData)——手动构造 FormData，适合非表单控件数据。
- 工具栏按钮（弹窗底部「保存」）常用方式二/三组合：校验失败 focus 到出错字段。
- 注意 submitter 场景：多个提交按钮带不同 formAction/按钮值（value 会进 FormData），删除 vs 保存复用一个 action 时用按钮 name/value 分支。
