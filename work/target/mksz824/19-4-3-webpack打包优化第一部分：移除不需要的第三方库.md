# 19-4-3-webpack打包优化第一部分：移除不需要的第三方库

上节课我们成功使用 webpack-bundle-analyzer 生成了分析图，现在看看怎样借助这张图完成构建优化。这个过程全程干货，完全结合项目实际，没有脱离实际的夸夸其谈。

## 读懂分析图

图中由一系列格子组成。这边是我们的 chunk-vendors.js，也就是一系列第三方库打成的整体文件，它很大，parsed size 有 2.25MB；另外一边小的蓝色部分是我们整个应用的逻辑代码，只有 112.96KB，说明它不是优化的重点。

每个格子代表一个第三方库，格子里面还会套格子。最大的一块是我们使用的第三方组件库 Ant Design Vue，占了很大一块，有 1.1MB；然后按大小排列，Moment 也很大，有 262.79KB；再往后是 lodash、core-js、vue-draggable、html2canvas 这些我们用过的第三方库。

先把优化前的大小记录下来：parsed size 2.25MB。通过图做优化的方案，首先就是找对对象：要针对比较大的模块进行优化，那些非常小、几乎看不见的模块，就算优化了也没什么大用。

## 第一步：检查依赖放置位置

第一大步是看看有没有重复的模块、或者没用的模块被打包进了最终代码。第一个步骤是检查 package.json：它有两个 dependency 字段，dependencies 和 devDependencies。devDependencies 应该放置跟开发相关的模块，但有的同学会把开发相关的包放到 dependencies 里面，这样做有可能会造成最后的引用被打包到最终文件中。我们的项目没有这种情况，因为我安装任何包时对放置位置都很讲究，将开发依赖的包或者项目依赖的包放到对应的字段中。我觉得这一点真的挺重要，但确实见过有人一股脑全部装到 dependencies 里，这是一种不好的实践。

## 第二步：移除重复加载的模块

第二点是检查是否有重复加载的模块，或者功能大体相同的模块。图中我发现了端倪：这里有一个 lodash.js，有 71.28KB；再找一下，点开放大，这里还有一个 lodash-es，是 lodash 的 ES 版本，是另一份重复的依赖。

从这里也可以完全看出 ES 版本的优势：使用 ES 版本的第三方库可以享受 Tree Shaking 的红利，我们用到了哪个方法才打包哪个方法，大小要比 lodash.js 小很多。

现在搜索代码中哪里使用了 lodash：大部分文件使用的是 lodash-es，但有些文件没注意就使用了 lodash。要把这些全部修改成一样的版本，也就是统一使用 lodash-es。我大约修改了三处文件。

重新打包看看能缩减多少：优化后 lodash 从图上消失了，总大小变成了 2.18MB。记录一下，这一步优化到 2.18MB。

## 第三步：移除没用到的模块

第三个步骤是检查是否有没用到却打包进最终文件的模块。Ant Design Vue 下节课再分析，这是一个比较复杂的过程。先看排名第二的 Moment：我们的项目其实根本没有用到 Moment，它是处理时间格式的库，是 Ant Design Vue 内部使用的，比如 Calendar、DatePicker 都用了它。

Moment 的主库这么大，但里面还有一系列叫 locale 的文件，一看文件名就是各个国家的名字，是做国际化的一系列文件，用于不同语言的处理。这在我们项目中完全没有用，因为根本不需要国际化，所以要想办法把它去掉。

去掉也就是 ignore 一些文件，可以使用一个对应的插件：Webpack 内置的 IgnorePlugin。顾名思义，就是当代码中有 import 或者 require 符合特定格式时，把这些都忽略掉。它有两个参数：resourceRegExp 指定 import 中想忽略哪些文件（一个正则）；contextRegExp 指定在哪个文件夹下发生的 import（use to select specific directories）。文档里正好有一个 example of ignoring moment locales，和我们的场景完全对应：moment 2.18 之后，所有的 locale file 都被 bundle 在一起，跟 core library 打包到一起，所以要想办法去掉。

它的写法就是：resourceRegExp 匹配任何 locale 文件，contextRegExp 匹配 moment 文件夹，在 moment 文件夹中的任何 locale 文件都 ignore 掉。来到 vue.config.js，先把 webpack require 进来（这是 webpack 内置的插件），然后 config.plugins.push。这个插件不需要区分环境，所有环境都可以添加：

```js
config.plugins.push(
  new webpack.IgnorePlugin({
    resourceRegExp: /^\.\/locale$/,
    contextRegExp: /moment$/,
  }),
);
```

有了这个插件之后再打一次包。打包完毕后发现排名第二的已经不是 Moment，Moment 被降下去了，而且它所有的 locale file 已经消失。现在的总体大小降到了 1.95MB。记录一下：优化到 1.95MB。

## 小结

经过简单的两步，包大小已经从 2.25MB 缩减到了 1.95MB。当然还有重头戏：最大的家伙 Ant Design Vue 占据了这么大一块空间。下节课看看怎样对这个最占空间的第三方组件库进行优化。
