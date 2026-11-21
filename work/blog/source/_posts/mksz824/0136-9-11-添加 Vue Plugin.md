---
disableNunjucks: true
title: 9-11 添加 Vue Plugin
date: 2026-11-17 14:16:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们了解了 Rollup 插件的基本运作机制，现在来添加对应的 plugin，让项目最终生成两种格式的代码。我们的入口文件 index.ts 是一个 TypeScript 文件，它加载进来的其他文件中还有 Vue 格式的代码，所以需要至少两种类型的 plugin 来完成代码的对应转换：先用处理 Vue 文件的 Vue plugin 进行第一次处理，再使用 TypeScript plugin 进行第二次处理。它们返回的类型应该有两种：一个是我们主要需要的 ESM 格式的文件，一个是 UMD 格式的文件。同时注意，还要单独生成一个 CSS 文件，因为组件库有单独的一系列样式，需要单独产出样式文件。

这节课先看第一个步骤：处理 Vue 文件。为了简化演示，用项目中原有的 App.vue 来处理。App.vue 很简单，有三块内容，但很丰富，因为 template、js、css 三块都有。这节课只测 js，所以我把 lang="ts" 去掉了，暂时处理 Vue 文件、不管 TypeScript。rollup.config.js 的创建过程就不多说了，我已经创建好。这里说明一下，我已经把所有组件补齐了，从 index.ts 中可以看到 LImage、LShape 都补好了，也提交在代码中了，不知道怎么写的同学可以看我的提交记录。

开始写配置文件。第一步导出一个 object，export default。input 是什么？这节课使用测试的 src/app.vue。output 里面有 fileName 和 format。我希望从 package.json 里把 name 拿出来，非常对应：`import { name } from '../package.json'`，在 output 中添加 name 字段。第二个字段是 file，我想添加一个函数动态生成名称，因为 file 的类型有两种，ESM 和 UMD。创建一个函数，参数是 type，用模板字符串返回 dist 文件夹下的 `name.type.js`。这里先把 file 传入 esm，format 是 es。ES 格式的配置文件基本写完了。

接下来要处理 Vue 类型的文件。在插件列表里找对应的处理插件，有一个 Vue，点开就是 Rollup-plugin-vue 的链接。安装：`npm install rollup-plugin-vue`。注意安装完后要确定它是 6.0 版本以上，@next 才是支持 Vue 3 的插件版本。它的文档里有一系列配置，感兴趣的可以看看，我们使用默认配置就好。回到代码，确认一下 package.json 中的版本号，6.0 以上没问题。添加进去：放在最前面 `import vue from 'rollup-plugin-vue'`，然后创建一个新字段 plugins，它是一个数组，首先用 vue 插件处理。

插件添加完毕，运行一下看看结果。已经添加了一条命令叫 build:esm，运行 `npm run build:esm`。可以看到它报错了：unexpected token，you need plugins to import files that are not JavaScript，错误出现在 style 的 CSS 部分。根据错误信息猜测，它是没有 CSS 类型文件的处理器。

大家都知道，.vue 这种格式称为 SFC 单文件组件，编译以后它就是一个 object，上面有一系列组件的属性，比如返回的类型是 render 方法，也就是说 template 和 script 最后是编译在一起的，但 CSS 不是。所以 CSS 需要单独的处理。这里暂时把 style 删掉，保存再运行一次，可以看到它就能成功运行了。这意味着我们需要一个处理 CSS 类型文件的插件。

大家都知道，Rollup 默认只处理 JS，而且是 ES6 modules 类型的代码，别的都需要插件完成操作。搜一下有没有对应的 CSS 处理插件，分类里点开 CSS，可以选用 css-only 这个插件，它是处理 CSS 最简单的一个插件，首页在这里，大家可以自行安装。把插件在 plugins 中添加一下：`import css from 'rollup-plugin-css-only'`。看它的用法很简单，就是 plugins 里多添加一项 css()。注意它有一个参数 output，用来设置产出的文件名，这里直接复制官方的例子就好。它还支持传入一个 function 动态创建，我们这里用最简单的先演示。放在 vue 处理的后面，两个插件都添加完毕。

再次运行 `npm run build:esm`，样式也改回去了，成功了。看看我们生成了哪两个文件：进 dist 先看 bundle.css，它把我们里面的样式代码抽取出来放到了一个单独的文件中；再看 ESM 生成的 OpsFlow 组件库 esm.js，这一串代码和一个单文件组件编译以后非常相似，其中的 render 方法就是在创建一系列的 VNode，过程就是这样。

成功了，没问题，我们暂时搞懂了 Vue 格式文件的处理。下节课给它加上 TypeScript，双管齐下，完成 TS 对应的处理。到这里，谢谢大家，再见。
