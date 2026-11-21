---
title: Schema→UI 的驱动机制：为什么改数据就能改页面
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 原理, Schema, MobX]
---

## Schema→UI 的驱动机制：为什么改数据就能改页面

闭环链路是：**右侧表单改值 → MobX action 写回 store → observer/useMemo 响应式触发组件重渲染 → 画布/发布页展示新值**。反向（数据→视图）则是 `omit + form.setFieldsValue` 回填表单。

为什么成立？因为组件视图是 store 数据的纯投影：组件只消费 `options`（Record<string,any>），不持有自己的业务状态。React 用 MobX 必须 `observer` 包裹，列表渲染前 `toJS` 转普通对象——这是响应式生效的前提，漏了 observer 就是经典的"改了没反应"bug。

**本项目实例**：props 在「一维表单值」与「{defaultValue, isHidden, value} 二维对象」间双向转换，数字/布尔字符串做类型归一；FormItem 二次封装用 isHidden 控制显隐。编辑器 store 五状态中 `componentConfigs`（id→配置字典）驱动"画什么"，`sortableComponentConfig`（id 数组）驱动"什么顺序"。

推论：一切画布操作 = 对这两个数据结构的增删改查，键盘操作、拖拽、撤销重做全部统一到这个模型上。

出处「课程25 · 14-8、14-9；scan3」
