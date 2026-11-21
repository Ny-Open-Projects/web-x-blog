---
disableNunjucks: true
title: 6-16 方案一：使用 JSX 重写 PropsTable 组件
date: 2026-11-17 16:18:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课说到在 Vue 的单文件组件中，template 部分假如直接渲染一个 VNode，会以字符串的形式输出它整个 object 内容，而不会转换成对应的虚拟 DOM 节点并展示。这节课来解决这个问题。第一种解决方案大家肯定能想到：使用 JSX 直接替换 SFC（Single File Component）的写法。JSX 天生就是转换成 VNode 的，在 JSX 中写 Vue 的变量，肯定会被完美转换。

现在我们的 template 写得比较复杂，JSX 和 Vue template 写法上有一些差异，正好可以做一个对比，看看差异在哪里。我已经新建了一个同名的 PropsTable，不过后缀名是 tsx，写到生成 finalProps 的代码的地方。要想返回一个 JSX，可以在 setup 中 return 一个 function，function 里面再返回你想要返回的 JSX。

finalProps 已经包括了属性的对应关系。第一步是循环它：没有了 v-for，循环一个 object 可以使用 Object.keys 方法。跟原来对比一下，从这里开始写：Object.keys(finalProps.value)（注意是 value，因为它是一个 computed），称之为 key。首先拿到 value：`const value = finalProps.value[key]`。拿到以后先 return 最外面这个结构：创建一个 div，上面的 key 就是 key，class 是 prop-item。

第一个最简单的是输出 label。这里没有 v-if，直接使用 JavaScript 表达式来写：value.text，后面是那个 span 结构，直接复制过来。写完 label 后面是 class 为 prop-item-component 的部分。看界面，label 已经循环展示出来了。

现在遇到第一个难题：在 Vue template 中渲染动态组件名，我们使用了 component is 这种写法，但在 JSX 中不能这样做。对于动态的名称，必须拿到它的组件实例，然后把变量赋值给组件实例。注意这个变量最好是大写的，代表它是一个组件。由于我们只有组件的名称（记得 propsMap 里它是 string），所以必须建立一个 string 和真实组件实例的对应关系。

怎么做呢？把需要的这些组件的实例都拿出来（Ant Design Vue 的一系列组件），建一个 key 和 value 的对应关系。我已经写好了：a-text-area 对应的是 Input 下面的 TextArea，这些都是组件的实例。特别注意有些组件是在主要组件的属性上面的，比如 Input.TextArea 就是属性上的；下面也有，比如 Radio.Group、Radio.Button、Select.Option 等等很多。

现在就可以根据字符串拿到组件实例了。称之为 ComponentName（大写开头）：mapToComponent[value.component]，拿到它的实例，然后就可以进行渲染了，很简单，复制过来。完成渲染后看看界面效果：点击一个，这些组件都已经出现了。

继续做，同时把子组件添加一下。子组件很简单，照猫画虎把 subComponent 的名称也添加一下，直接复制，没有难度。先判断 subComponent 是否存在，然后取出来。在这里面进行循环，当然使用的是 value.options，假如存在，和之前的逻辑一样：value.options.map，每一项称为 option，return 的是 subComponent，它的属性是 value，等于 option.value，上面这个字就是 option.text。

完成渲染后看看现在的组件：选项都有了，点开字体，虽然这里有点短，但我们朝思暮想的 fontFamily 已经带样式出现了，VNode 的渲染非常成功。

下一步是添加属性。在 JSX 中添加属性就像在 HTML 标签上添加属性一样：比如刚才在 subComponent 上面添加的 value 属性，直接写 value 等于花括号包裹的值。但是现在主要 component 上属性比较多：不仅有 key 可变的 valueProp，还有一系列的 extraProps。为了解决这个问题，JSX 还支持在标签上进行 spread 写法，可以把属性全部展开。创建一个 props 对象：首先拿动态的 valueProp，它的值是 value.value；还有一系列的 extraProps，展开就好了。最后把这个 props 在 ComponentName 上进行动态展开。

看看属性是否出现：现在属性已经上来了。再点击看一下：宋体、黑体、楷体、仿宋，我们定义的样式已经成功出现了。现在属性全部出现了。

最后添加事件。不同于 template 的写法：原来 template 是 v-on:change，在 JSX 中的写法是 on 加上事件名称，后面事件的第一个字母要大写，比如 onChange。所以需要转换命名方式。首先需要一个帮助函数，把字符串的第一个字母转换成大写，这里已经建好了 capitalizeFirstLetter。然后在 events 里做一个简单的转换：on 加上 capitalizeFirstLetter 包裹的名称，这样就完成了事件的改造。最后把值也加到属性当中去：value.extraProps 展开放到里面去。

测试一下结果：点击看看是否会更新。中间的字号进行了更新；点击中，它已经换了位置。试试心爱的字体：楷体没问题；黑体都会变成对应的字体。展示、更新都没有问题，这节课的任务完成了。

我们使用 JSX 替代了 template 的写法。特别要注意刚才提出的三点完全不一样的差异。你觉得怎么样？更喜欢哪一种呢？下节课我们看看使用 template 怎样完成这个任务，同时对比 JSX 和 template 两种写法的优劣。到这里，谢谢大家。
