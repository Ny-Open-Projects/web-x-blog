# 13-19-学习 vue SSR 的基本用法

这节课学习 Vue 实现 SSR 最基本的用法，通过一个类似 Hello World 的例子，给大家一个最基本的、最浅显的认识。

## 安装

第一步安装 Vue。这里要用 Vue 3，所以要加 @next 标签安装最新版的 Vue 3，我已经装过了。按文档的说法，除了 Vue 本体还需要安装 @vue/server-renderer，不过浏览最新版的 server-renderer 文档会发现一个 Note：3.2.13 以上的版本，这个 package 被自动包含在了 Vue 主体（main vue package）当中，不用再单独安装。我们安装的最新版 Vue 是 3.2.22，超过这个版本，所以不需要另外安装。大家要特别注意这一点，先看自己的版本。

## 创建 SSR App

代码里有一个方法 renderH5Page，对应路由 `route/pages/:id/:uuid`，处理函数是 renderH5Page。这里需要从 vue 里导入 createSSRApp。特别注意：不是 createApp，那是浏览器里使用的，SSR 要使用 createSSRApp。

Vue 的世界都是从 Vue 实例（Vue app）开始的，SSR 也一样。先把 ctx 和 app 拿过来，创建 `const vueApp = createSSRApp(component)`。第一个参数是一个 component，大家应该非常熟悉。我们创建一个最简单的 component，由数据和模板两部分组成，用 Vue 2 的 Options 写法：data 是一个 function，返回响应式对象，这里叫 message，值为 hello world。

其实 Vue 3 的写法完全可以，因为 component 类型跟浏览器端完全一样。至于能不能在 setup 中使用，大家可以自己试一下，我没有尝试对应的写法。然后是 template，一段字符串，输出一个 h1 标题，内容用双大括号插值 message。

## 渲染为字符串

在前端 SPA 项目中，我们用 `app.mount()` 把实例挂载到 DOM 节点上；而在 SSR 的世界，需要通过数据（data）和模板两部分生成对应的字符串，供 HTML 直接输出。所以要拿 server-renderer 上的方法。

从 @vue/server-renderer 里拿 renderToString，顾名思义就是直接渲染成一个字符串。`const appContent = await renderToString(vueApp)`，它返回 promise，所以要 await；传入我们的 vueApp，返回的是一个 string，可以直接输出。

输出时设置 `ctx.response.type = 'text/html'`，让它渲染成 HTML 页面，然后 `ctx.body = appContent`。刷新这个 URL，可以看到 Hello World 输出了，说明整个渲染过程成功了。

## Stream 模式

除了字符串模式，它还提供我们熟悉的 Stream 模式。对应的方法叫 renderToNodeStream，它返回一个可读流。拿到可读流后就可以 pipe 进去。把字符串模式注释掉，用流的方式再测试一遍：

```ts
const stream = renderToNodeStream(vueApp)
```

生成的是一个 readable 类型的流。渲染时要先设置 status，然后可以用 pipe，也可以用 pipeline，随便挑一个即可：`pipeline(stream, ctx.res)`。可写流大家都知道，之前说过：ctx 上有一个 res，是原生 server 的可写流（node.js http 内部的），相对应的 req 是可读流，res 是可写流。写完整个逻辑，刷新页面，Hello World 成功输出，也没问题。

## 回顾

这节课的任务结束了，很简单，回顾一下：第一步用 createSSRApp 创建一个 app，这个 app 是为 SSR 服务的，跟浏览器端有区别。有了 app 后可以渲染为字符串：用 renderToString 以异步方式渲染成字符串然后输出；或者采用 stream 方式：用 renderToNodeStream 创建一个 readable stream，把它 pipe 到可写流（ctx.res）当中，最终完成任务。

基本概念今天学习到这里，下节课就可以使用真实的例子和真实的数据来完成对应页面的渲染了。
