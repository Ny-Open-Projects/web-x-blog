---
disableNunjucks: true
title: 19-4-4 webpack打包优化第二部分：按需加载ant-desig
date: 2026-11-17 08:10:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课来优化使用最多的 Ant Design Vue。从分析图上看，它占据了项目的半壁江山，大小高达 1.1MB。Ant Design Vue 是一个组件库，由非常多的组件构成，但特别注意，我们的项目中并没有使用它的全部组件，只使用了一部分。

## 问题所在：全局引入

看一下我们的引用方式：把 Ant Design Vue 的入口文件直接全部引用过来，然后在最下面 use，这样使用以后，所有组件都会被打包进来，无端将最后的应用增大了非常多的体积。仔细看本地应用的话，会看到一句提示：using a whole package of antd，请使用某个插件 to reduce app bundle size，也就是使用插件来减小整体打包大小。

其实这个内容官方文档是有的，叫按需加载，会使用 babel-plugin-import 这个插件。这个插件最早是 React 版本的 Ant Design 推出的配套 babel 插件，它做的事是做一个语法糖：将 `import { Button } from 'ant-design-vue'` 这样的格式转换成分别引入 JS 和 CSS 的单独导入。但这在组件局部使用的时候才有用。所谓组件局部使用，就是所有组件都使用局部引用的方式引入，比如在 props-table 当中引入一系列组件，用 components 字段进行注册。

我们现在采取的是全局一次性应用：直接引入整个包，然后以插件的方式 use。这么做就没法使用这种优化了。想采取按需加载有两种方式：

1. 不使用全局引入，在每一个组件都使用局部引入。这样做耗费的功夫很多，所有组件都要经过修改。
2. 手动完成按需加载：将应用中用到的组件一一 import 进来，放弃一次性全部使用的方案。

## 手动制作小组件库

我的根本思想是将使用的组件做成一个小的组件库。创建一个新文件，叫 config/ond.ts，把应用中使用的组件手动引入进来（import all used components in whole project）。这里就要细心地手动引入了，没有捷径。我统计了一下，引入了我们用到的这一系列组件。有可能某些界面没有全部测试到，可能会缺失一些，大家可以自行添加。

接下来需要把 app 引进来，它是一个类型（App）。有了这些依赖之后就可以进行小组件库的操作：把所有 components 放到一个数组中。特别注意，有一些子组件是用属性的方式引入的：比如 layout，想用 layout 的 header 组件，它是从 object 下面的属性来引入的。好在我们使用 TS，所有都有提示，点进去以后会很方便地弹出提示。

接下来创建一个 install 方法，跟之前学组件库时的方式完全一样：

```ts
import { App } from 'vue';
// import all used components in whole project
import { Button, Table, Layout, ... } from 'ant-design-vue';

const components = [Button, Table, Layout.Header, ...];

export default {
  install(app: App) {
    components.forEach((component) => {
      app.component(component.name, component);
    });
  },
};
```

install 当中的 app 会自动获得对应的组件实例。直接拿到 components 数组，调用 forEach 循环，每一项都是一个 component，在里面使用 app.component 注册全局组件：第一个参数是 component.name，第二个参数是对应的 component。最后不要忘记导出一个对象，其中有一个 install 方法，这样就满足了一个插件的要求。

现在做替换：不再使用整个 ant-design-vue 的库，而是使用 config/ond 这个文件。修改完毕重新运行 analyze 程序看结果：键入 npm run build:analyze，稍等一会儿，弹出最终的分析文件。可以看到 Ant Design Vue 现在只剩下了 478KB，原来是 1.1MB。从图上也能看到，现在只加载了我们需要使用的那些组件，一块一块都是按需加载的组件。整体大小只有 1.25MB，之前是 1.94MB，优化效果非常显著。

## Moment 为什么还不能移除

再分析一下图：moment.js 这个库，之前已经把它的 locale file 都去掉了，但它在图上还是比较扎眼。我们的应用中应该没有用到这个库，因为我们没有用到 Ant Design Vue 里面的日历和时间选择器组件，那些组件才和时间相关。但是如果直接把 moment 库 ignore 掉，会直接报错。为什么？

其实我们引入的组件和 Moment 有千丝万缕的联系。简单分析一下：有一个组件叫 locale-provider/index.tsx，它是一个中间组件，使用了 Moment 库，并且使用 provide 方法给下层提供数据，数据中有一些关于 locale 的内容。它有一个方法叫 setMomentLocale，搜索一下在哪里使用：在 create 的时候调用，拿到 moment，然后设置它的 locale。它做的其实就是设置 moment 库默认值的这么一件简单的事。

在我们使用的组件上，比如第一个用到的 avatar 组件，它的源代码中使用了一个叫 config-provider 的东西。config-provider 又包括刚才说的 locale-provider 这个组件，因为在这里它要拿到对应的配置，inject 了 config-provider 之后，就可以拿到一些全局配置值。

所以这些组件就和 moment 产生了联系：虽然这些组件可能没有直接使用 moment 的任何方法，但现在我们还不能把它忽略掉。这也是我觉得 Ant Design Vue 设计得不太完美的一点。

## 小结

通过两节课我们完成了第三方库的优化工作，库的大小已经大大缩小，最后是 1.25MB。基本原则有三条：第一，看看是否有重复的、不用的代码，比如之前的 lodash 和 moment.js 的 locale file；第二，看看是否按需加载，对组件库要按需加载需要的一系列组件；第三，选择支持 ES 版本的第三方库，比如我们使用的 lodash-es，Ant Design Vue 也支持 ES，这样可以大大缩小打包的体积。
