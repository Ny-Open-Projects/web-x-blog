---
disableNunjucks: true
title: 21-9 添加 VeeValidate 第三部分 完成登陆页面
date: 2026-11-17 13:15:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课整个 VeeValidate 已经能良好运行，这节课对它做进一步优化。审视一下现在的两个 input 组件（email 一块、password 一块），会发现它们的功能高度重合：取值、验证、显示错误，相似的 HTML 结构要写两遍。如果有十个表单元素，结构和功能就会非常复杂且冗余。解决办法自然是抽象一个单独的组件来完成这些工作，所以这节课做一次小的重构，把这部分逻辑抽取到一个全局组件里，命名为 `ValidatedInput`。

## 搭建组件骨架

先把 login 页面里那一大块结构拷贝到新组件的 template 中，变量暂时报错没关系，慢慢改。删掉会产生变化的冗余值，调整缩进。label 和 SVG 图标这些额外结构就去掉了，想加的后期可以通过 slot 添加，这里只保留最基本的结构来演示功能。

然后想想哪些属性是变化的：一是 input 的 type，二是 placeholder 的值。创建 `InputProps` 接口，placeholder 是可选的 string，type 也是 string。接着 `defineProps` 传入泛型，把变化的值接上去：type 取 `props.type` 并给默认值 text（也可以用 `withDefaults` 来加默认值，效果一样），placeholder 直接写 `:placeholder="props.placeholder"`。

## useField

接下来是重点任务，隆重推出一个来自 VeeValidate 的新组合式函数：`useField`，它可以操控整个 form 的状态。之前用的是来自 `useForm` 的 `defineField`，而 `useField` 可以完全分离地完成这个任务。

组件里需要传入一个属性，我们称之为 name，它等于使用组件时传入的 key 值。这个 key 对应的就是 `userLoginSchema` 中的规则，所以定义的这条属性就代表一条验证规则，作用和 key 完全相同。

`useField` 的神奇之处在于：可以把一条特定的验证规则取出来，和 `useForm` 这个中枢神经交互，并返回最新的值。调用时不能直接传属性，而要接受一个回调函数，这样设计是为了保持响应性：name 修改后能从 useForm 中取得最新的值：

```ts
const { value, errorMessage, meta } = useField(() => props.name)
```

它返回一系列值：value 是每一个单独的值，响应式对象，和之前 defineField 的返回非常一致；errorMessage 是单独的响应式对象，可能是 string 也可能是 undefined，通过它可以直接拿到错误信息。

有了这两个值，组件内的修改就很简单：value 放到 input 上；`v-bind` 不需要了，绑 attrs 的部分删掉；然后把所有 `errors.password` 之类的引用一一替换成 errorMessage（也可以批量替换）。

## 在 login 页面使用

ValidatedInput 应该可以运作了，下一步在 login 里做完整替换，删除一大段逻辑，直接使用全局组件。需要填几个属性：第一个是 name 为 email，placeholder 填 enter email address；第二个是 password，type 为 password，placeholder 改成 enter password。特别注意 name 不要写错，要和之前的 key 完全相同：要验证哪个值就写哪个 key。

保存后测试：完全刷新获得全新状态，点击表单，错误照常出现；切换值时对应信息也会变化，比如"至少是六个"的提示；验证通过时错误消失，重构成功了。

## 验证时机的差异

不过有个小问题。完全刷新后，鼠标放上去再 blur，这种情况下验证不会出现，而之前是可以的。这是验证时机的区别：表单整体提交的行为没变，点击 sign in 一样；但单个表单元素上，之前是通过绑定的 attr 事件在 blur 或 input 时更新值，而 useField 机制是值变化后才验证，值没变化就不触发。刚才的场景里进去时值是空，blur 后值还是空，所以不出现验证；键入任意字符后值变了，验证才出现。

如果要做到和之前行为完全一致，useField 还返回一系列辅助函数，其中 `handleChange` 可以手动调用完成一次验证。简单修改：在 input 上再添加一个 blur 事件，blur 时手动发起验证。刷新测试，没有任何值时 blur，验证就触发了。这样我们改变了它的默认行为。

## 单个字段的状态

最后，每个表单元素还有自己的状态。login 里 `useForm` 的 meta 对象上是整个表单的状态，单个字段同样可以拿到 meta。把 meta 放到组件里输出，字段和表单级的几乎一致，只不过针对每个表单元素单个的状态。之前是整个表单的状态，现在能拿到单个的，就可以做到更细粒度的控制：修改值时 meta 的值实时变化，通过这些变化可以控制单个元素的属性。

这节课进一步优化了表单验证方式，`useField` 能完成很多功能。正好项目里有登录，还有一个和登录非常相似的注册功能。对管理系统来说一般没有注册用户的功能，但作为教学巩固的一部分，我把它留作作业给大家练习，下节课带着大家一起完成。不会一行行写代码，但会把整体思路过一遍，更好地巩固知识点，其中还会学到一些新知识。这节课先到这里。
