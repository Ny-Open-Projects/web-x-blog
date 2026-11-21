---
disableNunjucks: true
title: 17-4-6 AForm 源代码解析 ：Form 组件 和 FormItem 完成验证
date: 2026-11-17 08:10:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

本章开头我们用 Ant Design Vue 的 Form 和 FormItem 完成了表单验证，它的验证过程让人印象深刻，也是这类组件设计时公认的难点：AFormItem 以 Slot 的形式存在于 AForm 之中，父子组件之间看起来没有任何属性传递，验证是怎么完成的？这节就解析源码，只聚焦验证功能的实现，分析粗略的基本思想，其余部分难度不大，可以自行阅读。文中行号基于 clone 下来的源码（未安装依赖，编辑器报错可忽略）。

## 从 validate 入口向下追

验证是调用组件实例上的 validate 方法触发的，所以直接到 `form.tsx` 的 157 行找 validate。可以看到它内部调用了 validateFields，validateFields 又调用 validateFields，后者才是最终实现。

按正常思路，这个方法体内要用 async-validator 验证表单中的值，必然伴随循环。方法前面有一些 warning 类的参数校验，最关键的部分在 `this.fields` 这个数组：它 forEach 循环，对每一项调用 `field.validateRules()`，该方法返回一个 Promise，被 push 进 promiseList 数组；经过一系列处理后，最终返回一个带 errorFields、outOfDate 等属性的 Promise 结果。核心就落在两个点上：`this.fields` 数组，以及 fields 项上的 validateRules 方法。

## fields 数组与 FormItem 的关系

fields 里的每一项应该对应一个 FormItem。到 `form-item` 源码的 221 行找一下，果然有实例方法 validateRules，猜想得到证实。

画出流程：Form 组件里 `this.fields` 数组 forEach，每项调用 validateRules，而这个方法正是 FormItem 实例上的方法，返回验证结果。

但验证需要两样东西：要验证的值（model）和验证规则（rules）。这两个数据都传给了 Form 组件，formState 这个 reactive 对象作为 model 属性，rules 也传在 AForm 上。难题出现了：**FormItem 子组件怎样拿到父组件的数据？**

## provide / inject 打通数据

回到 FormItem 的 validateRules，前面同样是数据拼装，关键点是 `const promise = validateRules(...)`，这个同名函数内部调用 async-validator，返回验证结果的 Promise，然后设置 FormItem 的一系列状态：validateMessage、errors、validateStatus 等。

看这个函数接受的参数。第一个是 namePath，来自 111 行：`fieldName = props.name`，也就是 AFormItem 上传的 name，它必须和 formState、rules 的键一一对应；namePath 是用外部函数 getNamePath 把 fieldName 转换成数组，比如 `['name']`。

第二个参数 fieldValue，来自 127 行，这里出现了关键角色：

```ts
const model = formContext.model
```

formContext 从哪来？109 行给出了答案，它是一个 **inject** 进来的值。再回到 Form 的 98 行，created 生命周期里调用了 `provide('formContext', this)`，把整个 Form 实例一股脑 provide 下去，命名为 formContext。子组件 inject 拿到的就是父组件 Form 的完整实例。

于是 fieldValue 就清楚了：model 是 formContext.model，也就是父组件上的 formState；接着调用外部函数 getPropByPath，第一个参数 model，第二个参数 namePath，拿到的正是 formState 上 name 对应的值，也就是 input 里输入的值。

第三个参数 filterRules，来自 140 行，最终调用 getRules：先拿 formContext.rules，再用 getPropByPath 传入 rulesRef 和 namePath，拿到该 name 下面的 rules。

到这里，要验证的值和规则都齐了，验证自然可以执行并返回结果。

## 最后一块拼图：注册子组件实例

还剩开头留下的问题：父组件 Form 怎样拿到子组件实例，放进 fields 数组循环调用？答案还是靠传下去的实例。看 FormItem 的 203 行，在 mounted 时判断 `this.fieldName` 存在，从 formContext 上拿 addField 方法，传入 `this`，也就是子组件自己的实例。addField 的实现非常简单：

```ts
addField(field) {
  this.fields.push(field)
}
```

至此整个流程闭环：Form 在 created 时 provide 实例；FormItem 靠 inject 拿到 model 和 rules，完成验证；再在 mounted 时调用父组件的 addField，把自己 push 进 fields 数组，供 validate 循环调用。

整个设计的奥秘就在于 provide，它把 Form 实例共享给所有子组件，让它们都能访问上面的属性，其中 fieldValue 和 rules 是完成验证的关键；子组件再在 mounted 时反向注册实例。还没完全理解的同学，可以对着流程图，按文中给出的行号逐段回看源码。
