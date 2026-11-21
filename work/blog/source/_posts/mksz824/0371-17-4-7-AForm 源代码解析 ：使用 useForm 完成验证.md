---
disableNunjucks: true
title: 17-4-7 AForm 源代码解析 ：使用 useForm 完成验证
date: 2026-11-17 09:11:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节从组件层面分析了 Form 实现验证时的数据流向，设计相当复杂，根源在于 FormItem 是以 slot 形式运作的，数据只能以比较别扭的方式传递：把父组件实例以 formContext 的形式，靠 provide/inject 获取。

换个维度思考：验证不过是数据处理而已。只要拿到要验证的数据 model 和对应规则 rules，循环调用验证即可，完全不必和界面、组件打交道，照样能完美完成任务，这是一个典型的可复用逻辑，用自定义 hooks 把它封装成函数就行。这就是 Ant Design Vue useForm 的诞生原因，这节分析它的源码。

## validate 的执行链

先回顾用法。useForm 接受两个参数：第一个是 modelRef，即表单数据的响应式对象；第二个是 rulesRef，每个值对应一组规则。传入后返回一系列函数，包括之前用过的 validate，调用后通过 Promise 返回是否通过。

把源码 clone 下来，validate 在 `useForm/index.ts` 的 283 行。它很简单：调用时可以不传参，但支持传入 names 参数，想只验证哪些 key 就传哪些。不传时，直接用 `Object.keys(rulesRef.value)` 取出所有 key，在我们的例子里就是 `['name']` 这样的数组。

接着它调用一个眼熟的函数 validateFields，把 keys 和默认 option 传进去。validateFields 内部逻辑非常直接：

- 一个 for 循环遍历 names；
- 每轮拿到 name，以及 prop，用之前用过的 getPropByPath 从 modelRef 里按 name 取值，最终拿到 input 中的值 `prop.value`；
- 再用 filterRules 根据 rulesRef 和 name 拿到对应的 rules。

有了这三个数据，就可以调用 validateField 函数，参数正是 name、prop.value 和 rules。validateField 里调用的是 async-validator 提供的 validateRules 方法，同样传入这三个参数。验证过程是一个 Promise，过程中动态修改 validateInfo 对象里的值：没通过就置为 error，通过就是 success，并附上 help 帮助信息。

这样验证轻松完成，且与界面完全解耦。

## 界面如何跟着更新

结果拿到了，但验证完成后界面还得显示成功或失败状态（比如点 submit 时出现的错误提示）。这个例子和组件式用法略有不同：AFormItem 上用 v-bind 传入了一个 `validateInfos.name` 这样的 object，而 validateInfos 正是 useForm 直接返回的。来看它的来龙去脉。

定义从 168 行开始：validateInfos 初始是空 object，然后根据 `Object.keys(rulesRef)` forEach，为每一项设置默认值，required 和 autoLink 两个属性。之后就是在前面见过的 255 行那个逐项验证的函数里，Promise 完成时动态更新这个值：validateStatus 置为 error 或 success，help 置为帮助信息。

validateInfos 上的这些属性，正好对应 FormItem 支持的 props。查一下 API 文档就能对上：required 是初始设置，validateStatus 支持 success、warning、error 等状态，help 是提示信息。这些属性一更新，界面更新就随之完成。

## 小结

这是一种非常巧妙的设计：不和任何组件打交道，不需要复杂的实例传递，源码也清晰易懂，本质就是循环数据做验证调用，返回的 validateInfos 交给你做界面上的自定义绑定，用数据驱动界面。对比上节的组件方案，我认为自定义 hooks 的 useForm 是更好的解决方案。建议大家课后把两种方案放在一起做个总结比较。
