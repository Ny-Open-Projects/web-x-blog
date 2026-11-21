---
disableNunjucks: true
title: 19-4-2 安装webpack-bundle-analyzer插件
date: 2026-11-17 16:08:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课大体了解了 vue.config.js 的简单格式，现在进入这个文件完成一个任务：精简打包文件的大小。如果大家看过 npm run build 的输出，会发现有一系列 warning：我们的文件大小大于它推荐的 244KB，达到了惊人的 2.78MB。它提醒我们打包出的文件太大了，要想办法尽量优化打包文件的大小，这是资源优化中我认为非常重要也是最显著的一个点。

## 分析工具：webpack-bundle-analyzer

要优化就得知道这个 bundle size 这么大的文件是由什么构成的，这时就需要一个重要的分析工具。看一下 vue-cli build 命令的帮助：`npx vue-cli-service help build`，其中有两个配置 `--report` 和 `--report-json`，解释是 generate report html to help analyze bundle content，会生成一个 report 的 HTML 帮助你完成分析。这节课说说这个命令内部采用的是什么插件、可以完成怎样的分析。这样在其他使用 webpack 打包的项目中，不管 React、Vue 还是 Angular，都可以使用这套策略。

内部使用的是 webpack-bundle-analyzer 这个插件，使用人数非常多。它有两种使用方法：第一种 as a plugin，在 webpack 配置文件中像插件一样使用；第二种是像 CLI 命令行工具一样使用。我们要采取的是第一种。

运行完毕它会生成一个可视化的图，从图中可以做几件事情：一是分析模块是由哪些不同的模块组成的；二是分析哪些模块占据了比较大的体积；三是分析是否有错误的模块被打包进来。通过这一系列分析，最后达成优化的目的。

## 添加 analyze 模式

现在把这个插件添加到应用中。我们不使用刚才看到的 Vue CLI build 的 report 选项，而是在 vue.config.js 中自己添加这个插件。Vue CLI 安装后其实自带这个插件，如果是别的项目，请大家自行安装。

首先把它引过来：

```js
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
```

添加 webpack 配置需要在 vue.config.js 中使用一个特定字段：configureWebpack。文档中说明，它提供一个对象，要使用什么 plugin 就添加到里面，这个对象会被 webpack-merge 合并到最终的 webpack 配置里去。此外它还可以返回一个 function，function 能拿到 config 这个参数（最终内置的配置），可以针对不同的环境进行修改。我们采用第二种方法，我觉得它更灵活也更强大。

写之前先新建一个模式，只用于 analyze，跟 build 加以区分。创建一个新的环境变量文件，加入两个环境变量：NODE_ENV 设置为 production，希望它使用生产环境的模式进行打包；另外多加一个变量 ANALYZE_MODE。配置文件中不管什么样的变量都能拿到（这跟客户端不一样），所以在配置里添加 isAnalyzeMode，等于 process.env.ANALYZE_MODE，也转成布尔类型。

然后添加 configureWebpack 选项，它是一个函数：

```js
configureWebpack: (config) => {
  if (isAnalyzeMode) {
    config.plugins.push(
      new BundleAnalyzerPlugin({
        analyzerMode: 'static',
      }),
    );
  }
},
```

首先判断是不是 analyze mode；是的话把插件添加进去。怎么拿到插件的数组呢？config 上面有 plugins，直接调用 push 把 new 出来的插件加进去。插件有一系列参数，我们加一个比较特别的：analyzerMode，可以是 server、static、json 和 disable。server 会开启一个 HTTP 服务器帮你把页面引过去；static 直接生成一个静态文件；json 生成一个 JSON 文件。这里采用 static 模式。另一个参数 openAnalyzer 表示运行完毕后自动打开页面，默认就是 true，跟我们的想法一样，不必添加。

## 添加命令并运行

Webpack 配置弄好之后，在 package.json 中添加一个特殊的命令。把 build:staging 复制一份，新建一个 build:analyze，它的 mode 应该是 analyze：

```json
"build:analyze": "vue-cli-service build --mode analyze"
```

保存之后运行 npm run build:analyze。命令运行完毕后，它会自动打开一个 HTML 页面（本地的一个 file），以图表的方式展示一大堆依赖的形式。

有了这个图就可以做分析。怎样从这个图入手精简我们的代码？下节课一起来看。
