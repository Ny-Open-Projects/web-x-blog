# 15-4-5-使用 Vue Draggable Next 完成排序

通过三节课我们完成了一个可拖动排序列表的简单编码，要掌握的是三个阶段：第一阶段是排序开始，监控被拖拽的元素，添加特殊的状态和 UI；第二阶段是移动阶段，进入别的列表条目时完成数据交换；第三阶段是 drop，松开鼠标时把状态恢复原状并发送对应的事件。

## Vue Draggable Next

了解了原理以后，这节课该使用成熟的第三方工具替换简陋版本了。之前说过，最流行的 Vue 拖拽排序解决方案非 Vue Draggable 莫属，而且在 Vue3 正式发布时就推出了兼容版本，叫 Vue Draggable Next。

它基于一个专门的拖拽排序底层库 SortableJS。在这个底层库之上，除了 Vue 的解决方案 Vue Draggable Next，还有 Angular（ngxAwesome）、Vue2、React 等一系列解决方案。它采用的技术和我们简单方案一样，也是基于 HTML5 drag 这个现代特性。它的一系列 features 包括：支持移动端、支持自定义 drag handles（用一个自定义区域负责拖动）、智能自动滚动等。

安装：`npm install --save vue-draggable-next`，注意要安装最新版本。它自带类型文件，不需要额外安装 @types。

## 接入组件

先把原来自己写的解决方案备份到一个新文件 `LayerListBack.vue` 中，把原来的 LayerList 恢复到没有添加排序的状态，再开始编码。

首先导入库：`import Draggable from 'vue-draggable-next'`，添加到 components 中。然后把 UL 替换成 draggable 组件（上下两个都替换）。它有一个 `list` 属性，就是传入的要排序的数组。再添加一个 `ghost-class` 属性，作用和我们之前一样，拖动起来时的状态 class，这里沿用已经添加好样式的 `ghost`。

注意它的模板写法：内部使用了一个具名 slot 自定义 template，slot 名称为 `item`，并传了一个 property，每个条目用 `element` 变量替代。所以我们把内容放进 `<template #item="{ element }">`（记得闭合），并把模板中所有的 `item` 替换成 `element`，同时把之前的 v-for 去掉。

再做一个小的修改：它支持自定义 handle，我希望添加一个自定义元素来处理拖动，而不是整个条目都可以拖拽。添加一个对应的按钮并使用图标 `DragOutlined`（引入方式和其他图标一致），放在最右侧 InlineEdit 的后面。关键属性是 `handle`，它告诉 draggable 哪个 DOM 节点负责处理 drag。同时特别注意，要在那个节点上添加 `class="handle"`，这样它才能对应处理。

## 排序生效但界面没更新：一个典型 bug

看整体样式已经出现，按住 handle 就可以拖拽。把图层一和图层二互换：拖起来之后已经完成了互换。但 drop 之后出现了一个问题：界面上看起来还是图层一、图层二，而左侧的排序反而已经生效了，看起来很奇怪。如果把整个 list 打印出来，会发现数组的顺序其实已经改变了；选中图层一编辑它的属性，发现文本已经是 hello two，说明数组里面那一项确实发生了转变。

这里应该想到可能是 InlineEdit 出了问题，里面的值没有更新。验证一下：在旁边多添加一个 span 显示 `element.layerName`，可以看到图层二和图层一这时已经正确了，但后面的 InlineEdit 并没有更新。所以不是整个列表的问题，而是我们自己写的组件的问题。

来到 InlineEdit 查代码：`innerValue` 来自 ref，初始化为 `props.value`。但有一个重要问题，当 props 更新的时候，我们并没有同步更新 innerValue。这是把属性映射到内部数据时非常常见的问题：当属性更新时，内部数据很可能是旧的，这一点一定要记住。

修复：添加一个 watch，使用 getter 监听 props 中的 value，当值变化（有 newValue）时执行 `innerValue.value = newValue`。

删掉调试用的 span，刷新后再拖动，排序成功完成，非常完美。

## 美化

最后做一点美化：让图层名称区域（InlineEdit）的长度充满，把按钮移到最右侧。给 InlineEdit 添加一个 class 叫 `edit-area`，然后给 handle 和 edit-area 分别添加样式：handle 设置 `margin-left: auto`，edit-area 宽度设为 100%。再添加一个鼠标样式，放上去变成 move 光标，让用户一眼看出它是干什么用的。

## 小结

这节课我们成功安装了 Vue Draggable Next 并学会了它的使用；更重要的是，它还帮我们发现并修复了 InlineEdit 的一个 bug。这个 bug 很有典型性，大家一定要记住：当你在 setup 中创建了 props 的一个副本以后，当 props 更新时，一定要同步更新这个副本。
