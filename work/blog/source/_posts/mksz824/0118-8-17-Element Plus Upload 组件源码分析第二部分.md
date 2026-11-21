---
disableNunjucks: true
title: 8-17 Element Plus Upload 组件源码分析第二部分
date: 2026-11-17 16:58:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课分析了 Element Plus upload 的一部分源码，并抛出了一个问题：它面临和我们一样的问题，需要在实例上提供手动完成一系列动作的方法（比如 submit 手动上传），所以需要访问子组件中的实例方法。它是怎样完成这个任务的呢？我们之前学过，访问子组件的组件实例，第一个想到的就是 template ref。看看它是否使用了相同的逻辑。

## submit 的来源

直接看源码。来到 index.vue，找 submit 方法，拿它举例。首先发现 submit 是从 use-handlers 里取出来的。用图描述：submit 函数是 index.vue 从 use-handlers 取出的，这是第一步。然后要向外界返回出去，才可以被使用：index.vue 的 setup 最下面把 submit return，这样用户拿到 index 实例后就可以调用这些所谓的静态方法，完成手动上传。从文档得知，这些方法就是完成触发上传的一系列工作。

也就是图上的第二步：index.vue 拿到 use-handlers 返回的一系列函数，return 这一系列函数，使用者拿到 index.vue 的实例就可以调用，就是这么一个过程。

## use-handlers 内部

搞清楚之后，深入 use-handlers 看看 submit 在干什么。代码其实很简单：uploadedFiles.value.filter 找到 status 为 ready 的文件，然后 forEach，调用 uploadRef.value 的 upload 方法。

看到这个 ref 我就特别亲切了：它肯定是获得了 upload 组件的组件实例。看看它是怎么获得的。uploadRef 定义在 use-handlers 中，是一个响应式 ref，初始值 null，最后被 return。index.vue 调用 use-handlers 时就拿到了 uploadRef。

那怎样将一个 ref 和一个组件实例联系在一起呢？很简单：给组件添加一个同名的 ref 属性。在 render 中渲染 uploader 组件时，uploadData 是它的 props（传到 h 的第二个参数），我们发现了一个熟悉的老朋友：ref 属性，它的值等于字符串 "uploadRef"，和变量名相同。这样就让 use-handlers 的 ref 和 uploader 组件产生了关联，在 use-handlers 内部就可以使用 uploader 实例上的方法了，也就是 submit 中的 uploadRef.value.upload。

这个过程看起来挺绕，但采用的就是我们之前总结的 Composition API 中获得组件实例的最基本方式。

## 字符串 ref 的绑定时机

有的同学可能不清楚一个字符串 ref 属性是怎样和实例搭上关系的。文档中有描述，简单介绍一下：在 Virtual DOM 的 patch 过程中，如果一个 VNode 的 ref 属性等于 render 中的一个响应式对象，那么这个 VNode 对应的 DOM 节点或组件实例就会被赋值给这个响应式对象。这个过程发生在 virtual DOM patch 或 mount 的时候，所以只有在初次渲染完毕以后才能拿到这个值。

举例验证。在 App.vue 中我们用 ref 拿了 uploader（inner component ref），打印 `uploaderRef.value`：

- setup 中直接打印：是 undefined，因为 setup 在 mount 之前运行，自然还没有赋值。
- 用 onMounted（watchEffect/回调）验证：第一次是 undefined（DOM update 之前运行），后来又触发一次就有值了。
- 把回调的第二个参数 flush 改成 post（DOM 更新之后执行）：第一次就直接打出了 proxy 对象，已经拿到 uploader 组件实例。

这就证实了猜想：赋值发生在 virtual DOM patch 或 mount 时，必须初次渲染完毕以后才能拿到。

## 对这个设计的评价

到目前为止，我们分析完了 Element Plus uploader 组件的结构：数据操作拆分和组件结构拆分，大家从图上看应该很清楚。它是一个良好的设计吗？我认为有一点不好：对 uploader.vue 和 uploader-list 来说，它没有采用自上而下的数据流。数据修改时并不是以事件的形式发射回给父组件处理，而是直接将数据操作的一系列方法都传递进去，除了部分 props，use-handlers 拿到的数据操作方法一股脑传下去，然后直接在子组件里调用这些方法做修改。

当然，这样做算是一个省时省力的方法：如果使用事件的方式，代码有可能会更冗长，所以它是一个折中的方案。对于目前我们的 uploader 功能来说，我不认为把我们的实现改造成它的结构会更好，那会增加开发的复杂度，也更难理解。当然，如果后面想继续完善我们的 uploader、添加和它一样多的功能，也可以参考这样的结构。

所以这个组件的开发过程是我抛砖引玉的过程，大家学会对应的开发模式，继续将它发扬光大才是最重要的。这节课的分析就到这里，谢谢大家。
