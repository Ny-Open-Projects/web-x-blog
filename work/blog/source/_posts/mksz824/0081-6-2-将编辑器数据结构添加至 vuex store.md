---
disableNunjucks: true
title: 6-2 将编辑器数据结构添加至 vuex store
date: 2026-11-17 09:21:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上一周我们完成了 B 端项目整体框架的搭建，整体路由和 Vuex 的结构都已编码完毕。现在可以进入项目中最难的一部分，也就是编辑器这个路由（或者说模块）的开发。这个大模块的开发将伴随我们很长时间。对于这个功能的开发，我们会使用渐进式的开发手段。

对于编辑器的技术实现方案，我们在开始的一周已经对它的根本问题做了非常完备的技术实现方案，这就是问题的根本所在。整个编辑器就像盖一座楼：分析的关键问题实现就是地基，其他功能好像是地上往上的楼层。楼层可以渐进式地不断进化，但地基必须打好并且完善，这才是渐进式开发的必要手段。

先回顾当时技术方案里的具体实现。最开始写的那个主要部分，其实已经把结构创建好了；然后是整体的状态结构，里面已经非常明晰地分析了状态结构和场景设计。那么第一步自然就是创建对应的状态结构。现在我们已经有 user 和 templates 两个单独的 store，只需要再创建一个 editor，把这些状态放进去就好了。

第一步，请记住我们的 Git Flow。上一周的 PR 我已经发出来了，把整个一周作为 initial structure 这么一个 feature 分支，现在也成功 merged 了。开发完这个功能后就可以开发下一个功能，新的一周我会创建一个新的 branch，这里大家可以看到分支名为 feature/editor-step-one。分支建立完毕就可以开始开发。

照猫画虎，把建好的数据结构拷贝过来，稍微改个名字：这里不叫 GlobalDataProps，应该叫 EditorProps。建立完毕后再复述一下：EditorProps 就是整个编辑器的状态，里面有供中间编辑渲染的数组，称之为 components，它的数据结构就是这样；还有 props，是元素的一系列属性；id 是它的唯一标识符；name 是业务组件库的名称等等。我们还多加了一个 currentElement，返回当前编辑的是哪个元素，它里面存的 id 和这个 id 是对应的。

接着创建几个测试数据。由于要使用独一无二的 id，之前写了我们使用 uuid v4 进行创建。给大家推荐一个 npm 包，就叫 uuid，下载量非常大，是最通用的解决方案。用 `npm install uuid --save` 安装。特别注意的是，除了安装本体，它不自带类型文件，需要单独安装一下 @types/uuid。都安装完毕后拿过来使用：用 uuidv4（它有很多版本，v4 是现在使用人最多的）。引进来后就可以创建对应的数据了，叫 testComponents，是 ComponentData 的数组，里面有一系列数据。

然后创建 editor 本体。它是一个 Module 类型，第一个参数是本地 state 的 interface，第二个是全局的，也就是 GlobalDataProps。state 里 components 就是 testComponents 的测试数据，再来一个 currentElement，现在还没有选中任何元素，那就是空。最后把 editor 导出。

editor 创建完毕后，把它添加到 index.ts 这个主文件里。先把 editor 模块和它的类型导过来：GlobalDataProps 里自然要多加一项 editor，类型是 EditorProps；modules 下面同时也要多加一项 editor。现在编辑器模块就加到整体结构当中了。

整个 store 中已经有测试数据了，来完成第一个场景：将组件渲染到画布中。从一个简单的测试开始，不渲染真正的业务组件，而是渲染一个固定的 div，把我们当时确定的 text 属性渲染到里面。渲染真实业务组件其实是一样的，只不过把 div 换成对应的组件，这里采用渐进式的方式，先从最简单的开始。

对 editor.vue 做些文章。首先很重要的一点：把 script 的 lang 设置为 ts（我忘了改，这里没写 lang="ts"，要特别注意，保存一下）。然后导入 useStore，在 setup 里使用；把 GlobalDataProps 拿过来，from './store/index'，这个我们经常用，大家要记住。创建 store：`useStore<GlobalDataProps>()`。现在可以从 store.state.editor 里拿到 components 了。假如 components 这个名字你不太好理解，换成 element 也可以，不要搞混。把它 return 出去。

然后在模板的画布区域添加一个 v-for：component in components，给它添加一个 key，key 应该是 component.id，再把里面的内容添加上去，也就是 component.props.text。到页面上看一下，出现了一个错误：computed is not defined，把它导入一下。再看页面，这些内容成功出现了，编辑器的数据可以完美地渲染在页面中了。

编辑器的第一步就完成了。之所以做得这么顺，完全仰仗于技术实现方案文档，我们其实就是按照它的思路写下去。这也体现了复杂项目事先分析难点、撰写前期技术实现方案的重要程度。今天这节课就到这里，下节课我们不用这些假的糊弄人了，要实实在在使用真实的业务组件。
