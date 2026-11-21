---
disableNunjucks: true
title: 21-7 添加 VeeValidate 第一部分
date: 2026-11-17 11:13:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课完成了服务器端验证。接下来是继续开发服务器还是先暂停？我们先暂停，因为现在的前端验证方案还有一点问题：管理错误的形式是每个字段都要创建一个响应式对象，如果表单越来越复杂，有十个 field，就要创建一大堆变量。我们需要一种更简洁的表单验证方式。

## VeeValidate 简介

隆重推出一个新工具：VeeValidate。它的 slogan 是 Painless Vue Forms，完全无痛的 Vue 表单。它是 Vue 生态里目前最流行的表单验证库，Stars 高达 10.4k。建议大家以后遇到任何表单和验证相关的需求都用它，我在最近的项目里高频使用，确实非常好用。

安装有两种方式：一是 `npm install vee-validate` 直接安装；二是 Nuxt module 形式，会帮你自动导入常用方法和组件。我直接用了 npm 安装，觉得更直接、更方便。

它的特点值得细数。第一，提供两种验证方式：

1. **组件形式**：和之前组件库的方式类似，接入很快。核心是三个组件：`Form` 在外层包裹其他组件，`Field` 带 name 和 rules（规则直接写上去），`ErrorMessage` 与 field 联动、出错时显示在这里。非常直观，但我们不采用这种方式，详细用法可以看文档。
2. **组合式函数 API 形式**：布局和验证方式更灵活，界面想怎么写就怎么写，只要有数据和中心状态即可。我们采用这种形式。

功能方面，它提供数据跟踪、验证、异步验证，支持多种第三方验证工具（Zod 可以和它完美结合），还有国际化等等。表单相关的所有需求它基本都能完成，而且高度可定制。

## useForm 与 defineField

请大家先自行安装 VeeValidate，然后来到 login 页面。第一步使用它提供的组合式函数 `useForm`，它是整个表单验证的中枢神经，提供一个表单上下文对象，任何单独的表单选项都可以注入。直接调用，先不传参数：

```ts
const { values } = useForm()
```

没定义任何表单选项时 values 自然是空的。`useForm` 定义完毕后，就可以把已有的表单元素和这个中枢神经集成起来。通过 `useForm` 返回的 `defineField` 添加表单值：有多少个表单元素就定义多少个 field。

和之前的方案说拜拜：`formData` 和那些 error ref 都没用了（之后删掉，先放着）。`defineField` 接受一个参数，即 field 的名称，第一个叫 email。它返回一个数组，第一个值是表单值本身（响应式对象），第二个是表单相关的一系列属性，其中包含事件处理，会在合适时机触发验证：

```ts
const [email, emailAttrs] = defineField('email')
const [password, passwordAttrs] = defineField('password')
```

后面演示只用 email。有了它们，把界面上的表单元素组合起来：email 的 `v-model` 改成直接绑 `email`（不再用 formData），再用 `v-bind="emailAttrs"` 把属性放上去。

打印 values 看联动效果：它是空的；在 email 输入一些值，values 里立刻出现，说明通过一次次 `defineField`，值会插进去。password 没做绑定所以输入暂时无效。表单数据和响应式对象成功联动了。

## errors 与验证规则

错误也很简单。`useForm` 还返回一个响应式对象 `errors`，与 values 一一对应：有多少个 value 就有多少个 error。这节课还不和 Zod 联系，先手动添加验证规则。`useForm` 有个参数叫 validationSchema，在里面给 email 写一条完全自定义的规则，它返回一个回调函数：

```ts
const { values, errors, handleSubmit } = useForm({
  validationSchema: {
    email: (value: string) => {
      return /^...$/.test(value) ? true : 'invalid email'
    }
  }
})
```

正则表达式就是验证 email 最简单的规则（可从源代码复制）。验证通过返回 true，不通过返回字符串作为错误信息。把 errors 打印出来看看效果：输入时 invalid email 立刻出现，验证已起作用。errors 和 values 一一对应，而且验证是及时的：v-model 更新时就立马验证。

## 改变验证时机

通过属性可以改变这个行为。`defineField` 还有第二个参数，里面有 `validateOnModelUpdate`，顾名思义就是 model 更新时验证，默认 true。设为 false 后行为就变了：值更新时验证不出现，而是 blur 的时候才出现。在外侧点击一下，错误才显示出来。

大家可以选择自己喜欢的时机：值更新立即验证，或 blur 时再验证。下节课把 Zod 和 VeeValidate 结合起来，就不用手动写这些烦人的验证规则了，同时看看表单提交怎样更快完成，把整个流程跑通。
