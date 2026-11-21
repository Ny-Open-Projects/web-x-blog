---
disableNunjucks: true
title: 15-5-2 EditGroup 编码第一部分
date: 2026-11-17 17:19:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课进入 EditGroup 的编码阶段，接着上节课的思路，先做两件准备工作。

## 准备工作

第一件是把数据补充完整。这个工作我已经替大家完成了：数据来自 `editor.ts` 的 editor store，在 TextComponents 中对应的 LText 或 LImage，我们已经把 default 展开进去，所以现在一系列的属性已经填充完毕。

第二件是补充 propsMap 的对应关系。我添加了一系列新的对应关系，并按分类标注得很清楚。特别注意新增了一个对应组件叫 ShadowPicker，它处理的是 `box-shadow` 属性。

box-shadow 是一个很有意思的 CSS 属性。看界面：阴影颜色、阴影大小、阴影模糊看起来是三个表单，其实这三个表单都在 ShadowPicker 这一个组件里面，它们调整的是同一个属性的值。回到表单组件的原则：只要是一个属性，就肯定有一个 value 和一个对应的更新事件。

ShadowPicker 的值长这样：`10px 10px 0px red`，有三部分，前两个是阴影的大小，第三个是阴影的模糊程度，最后一个是 color。所以把这三个值用 `split` 分开，分别传入三个组件（一个 ColorPicker 和两个 Slider）；每次更新时再通过 update value 把这些值组合起来，生成一个新的完整值。这个组件是组件原则的一个充分体现。这些代码大家可以直接从本次的 commit 里复制。

## EditGroup 的 props

准备工作完毕，开始编码 EditGroup。现在组件属性已经很长了，急需一个 group 进行分组。

首先从 props 分析。第一个属性肯定是业务组件对应的 props 列表。OpsFlow 组件库已经把所有属性的列表导出了，类型叫 `AllComponentProps`，点进去看其实是三种类型的一个交叉类型。第一个 prop 就叫 `props`，type 是 object，用 `as PropType<AllComponentProps>` 传入泛型，并且 `required: true`。

第二个属性是想要展示的分组模式。分组的规则由一个数组确定，目前是定死的，由下拉区域的标题 text 和其中的 items（下拉区域展示的属性列表）组成。添加一个 interface 描述这种关系：

```ts
export interface GroupBox {
  text: string
  items: string[]
}
```

由于通用属性的分组是定死的，我已经写好了默认的对应关系：尺寸、边框、阴影与透明度、位置、事件功能等等各自的 items。同时我们还提供自定义组合的功能，所以把它作为一个属性传入，称为 `groups`，type 是 `PropType<GroupBox[]>` 数组，default 是 `defaultEditGroups`。

## newGroups 的计算

最终要根据传入的分组信息生成一个新的数组：在最前面多加一项，text 是"基本属性"，items 是 specialProps，即 `Object.keys(props)` 减去 allNormalProps 的差集，而 allNormalProps 就是 groups 中各项 items 的 key 集合。

这个值要基于 `props.groups` 派生，所以创建一个 computed，称为 `newGroups`。

首先拿到 allNormalProps：把 groups 中每一项的 items 累加起来。用 reduce 实现：

```ts
const allNormalProps = props.groups.reduce((prev, current) => {
  return [...prev, ...current.items]
}, [] as string[])
```

reduce 的初始值是一个空的 string 数组，累加用展开符即可。

然后求差集。大家可能有各自的做法，我用 lodash 提供的方法：对于数组和对象上的计算，既然已经引入了 lodash，建议直接去 lodash 里寻找现成的解决方案，它是开发过程中非常好的工具。这里使用 `difference`，它可以计算两个数组有区别的项，并且以前面那个数组为基础。所以前面是所有总体的 props 的 key 数组（`Object.keys(props.props)`），后面是 allNormalProps：

```ts
const specialProps = difference(Object.keys(props.props), allNormalProps)
```

这样基本属性就完美计算出来了。然后把第一项添加到默认 groups 的前面，剩下的直接展开 `props.groups`，newGroups 就打造完毕了：

```ts
return [
  {
    text: '基本属性',
    items: specialProps,
  },
  ...props.groups,
]
```

## 展示到界面

把结果展示到界面上验证属性计算是否成功。用简单的 v-for 就可以：`v-for="item in newGroups"`，展示 `item.text` 和 `item.items`，看看数组中到底有什么项。然后在 Editor 中做替换：引入 EditGroup，添加到 components 中，把原来的组件替换掉（改成小写看起来更整齐）。

看最终结果：分组实现了。基本属性是我们减出来的值，尺寸、边框系列都是定死的，看起来不错。看图像组件，它也能算出不一样的值。特别注意：有一个 position 和 right，默认值里面是有的，但对应的编辑表单里没有这两个组件，所以它们不会被显示出来。

这节课完成了 EditGroup 的第一步编码，已经能够生成分组后的信息了。下一步只要把 PropsTable 一一传入，就能完成最终的结果。下节课继续编码。
