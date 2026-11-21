---
disableNunjucks: true
title: 9-12 添加 Typescript Plugin
date: 2026-11-17 15:17:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们完成了 Vue 文件的处理，有了这个技术就可以处理 TypeScript 文件了。通过上节课内容应该了解到，Rollup 处理的大体流程就是使用对应的插件处理不同的文件类型。所以首先要找到处理 TS 文件的插件。搜一下 TypeScript，可以看到很多插件，排名最靠前的是官方的 TypeScript 插件，后面还有一些其他的。

我选用的是 rollup-plugin-typescript2，没有用官方的 rollup-plugin-typescript。原因是使用官方插件的话，它和 Vue plugin 不兼容，会报错；而 Vue plugin 官方的例子和 Element Plus 都使用 rollup-plugin-typescript2，所以请大家也选用这个插件。安装地址在下面，大家自行安装即可，我已经安装完毕。

用了这么长时间的 TypeScript，TypeScript 是怎样编译成 JS 的呢？其实是 tsc 在起作用，tsc 也就是 TypeScript Compiler，这是我们转换 TS 的法宝。这些插件底层都是在使用 tsc 进行转换。关于 tsc 的配置，都写在 tsconfig.json 当中，脚手架给我们生成了一个默认的配置文件。注意，这个配置是和开发环境相关的，而打包模块时要用到它，所以到时候可能要在里面改一些配置。tsconfig 的配置项非常庞杂，TypeScript 官网做了一个单独的页面来陈列和说明这些选项，分成几个大类。看到这里我已经感觉眼睛很晕了。其实我们不需要弄懂每一项的意思，就简单看看 Vue CLI 默认生成的 tsconfig 里有什么玄机。

第一个字段是 compilerOptions，里面有很多字段，控制 tsc 执行之后的结果。先从 module 看起：module 就是输出的模块类型，解释里有一大堆类型，我们这里选择 ESNext 就可以了，剩下的活让 Rollup 来干。接下来是 target：它和 module 的区别是，编译以后要符合什么样的 ES 标准，指定编译目标的 ECMAScript 版本。target 属性做的事和著名的 Babel 一样：让你在源代码中使用未来版本的 JavaScript 特性，比如 object spread、箭头函数等，然后生成代码会自动加上这些特性的兼容代码，让不支持最新特性的浏览器也能完美运行。可选值从 ES3 一直到 ESNext，我们这里也直接选 ESNext，因为 TypeScript 处理完之后还有 Babel 进行处理，不需要它来做转换。

接下来是 jsx 选项。它这里选择的是 preserve。文档中有很多选项，不同选项可以把它转换成不同的代码。JSX 是 createElement 的语法糖，假如选择 react，默认就会把 JSX 转换成 React.createElement。我们选 preserve，就是什么都不管、不做任何处理，因为 Vue 文件在 TS 处理以后还要经过 Babel 的处理，所以保留原样就好。其他选项暂时不看，想知道详情可以自己看文档。

接下来是两个关于文件的选项。第一个是 include，听名字就很熟悉：要编译哪些文件。它接受一个数组，特别注意这里采用的是 glob 格式，两个星号代表任意长度。意思是 src 和 tests 文件夹下任意的 tsx 或者 vue 文件都会被编译。当然还有一些文件不需要编译，就是 exclude 属性，我们这里写了 node_modules。

看完配置文件，现在来第一次运行。我在 app 里做了点小改动：把 script 的 lang 改成 ts，并且 export 出去一个简单的 interface，因为要用一些 TS 特性做测试。添加插件：回到 rollup.config.js，把 TypeScript 引进来，`import typescript from 'rollup-plugin-typescript2'`，放在 plugins 数组最前面调用。这个插件会默认读取刚才查看的 tsconfig 的配置，所以这里什么都不用添加。

运行老命令 build:esm，成功了。看一下最终结果，但是发现一个问题：生成的文件和原来一样，还是 JS。要知道，使用 TypeScript 的时候，我们的库最好要有类型定义。比如应用中用的一些外部库，Vue、lodash 等，都可以获得 TS 的类型和方法提示，它们是通过 .d.ts 文件也就是声明文件完成的。所以我们的库除了输出源代码，.d.ts 文件也是不可或缺的，这样使用我们组件库的 TS 用户就可以完美获得 TS 的提示和类型检查。

这就需要改配置。先看插件文档，里面有一个选项称为 declaration，就是声明文件，把它设置成 true 就可以生成 .d.ts 文件。我们不希望直接改原来的 tsconfig，因为那是开发环境的配置，所以要生成一个新的配置。插件支持 override 覆盖选项：新建一个 tsconfigOverride，它是一个 object，配置加在 compilerOptions 里面，属性名称是 declaration，值设为 true。把这个选项传给插件，属性名是 tsconfigOverride。特别注意，这个选项的任何配置都是 deep merge 的，直接设置并不会影响 tsconfig 里的其他项，只是把这一项 merge 进去。保存后运行 `npm run build:esm`。

进入 dist 看一下，出现了一大堆 .d.ts 文件。打开一个可以看到，它把 interface export 出去了，把 Vue 的类型也 export 出去了。但现在所有的类型文件都出来了，这和 tsconfig 里写的 include 有关系：include 覆盖了一大堆文件，它和 Rollup 当中的入口文件没有关系。所以需要简单修改配置里的 include，现在只想生成一个对应的类型文件，改成只包含 src/app.vue。

修改完毕，把 dist 里的文件删掉，重新生成一次 `npm run build:esm`。可以看到报了一个错误：没有找到入口文件。查一下文档，include 下面最后一行有说明：假如文件设置不使用 glob pattern，也就是单文件形式时，只能添加后缀名为 ts、tsx 或 .d.ts 等被支持的文件。我们这里是一个 vue 文件 app.vue，明显不行。所以为了测试，把入口文件改成 main.ts：在 main 里把 app 直接引入并导出，把入口文件改成 main.ts。再运行一次，成功了。进入 dist 的 .d.ts 文件夹看一下，很完美：现在只有 app.vue.d.ts 和 main.d.ts，任务成功了。

这节课我们安装了 TS 插件，了解了 tsconfig 的配置详情，尝试把 app.vue 中的 TS 部分进行转换，并最终成功转换、生成了定义文件。有了这些经验，下节课就可以真刀真枪地处理入口文件，不用再使用假的 App.vue 组件做测试了。这节课到这里，谢谢大家，再见。
