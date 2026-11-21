---
disableNunjucks: true
title: 9-6 花絮 - Snowpack 另类打包工具 简介
date: 2026-11-17 15:27:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

前面介绍了 Webpack 和 Rollup 两种打包工具，也讲了几种 JavaScript 的模块类型。架构师课有个重要意义：知识广度和知识深度同样重要，广度能很好地开阔视野。这节课就顺着已了解的常见打包工具，介绍一个另辟蹊径的后起之秀：Snowpack。看这个名字和 Webpack 很像，同样带 pack，也是个打包工具。

Webpack 和 Rollup 这类工具被称为 Bundler，Bundle 就是打包，把 JS、CSS、图片、模板等互相依赖的资源，处理生成浏览器可以使用的几个文件。但这里有个问题：项目里的资源越来越多时，要处理的依赖关系越来越多，转换的文件类型也越来越多，打包时间自然越来越长。大中型项目第一次打包启动，有可能达到数分钟之久。用过 Webpack 的同学在工作中多半遇到过类似问题。

要知道，Bundler 打包的过程主要解决的是 ES Module 在浏览器中不被兼容的问题。但目前已经有一些最新版浏览器可以原生支持 ES modules 了。在本地开发这种场景下，使用者只有工程师自己，需求就是要快，也不需要兼容那么广的浏览器，一般都用最新版。那能不能直接利用浏览器对原生 ES modules 的支持？之前讲脚手架时对比过 Vite，Vite 作为脚手架用的正是这个理念，而 Vite 其实深受一个前辈的影响，它就是 Snowpack。

Snowpack 的核心思路和 Vite 非常类似：在开发环境下启动一个开发服务器，走所谓的 Unbundled 模式，也就是不打包。文件不会被编译打成一个或几个文件，每个文件在启动时只编译一次，并被永久缓存下来。当某个文件发生修改，只需要重新 build 那一个文件。对比上面 Webpack 那种 bundled 模式：修改一个文件，每次都要重新编译生成打包文件，项目一大，这个时间很恐怖。而 Snowpack 这种模式下，浏览器可以瞬间完成重新加载。

用 Snowpack 做个小实验。新建一个项目 Snowpack Test，安装依赖后，用 `npm run snowpack dev` 启动开发服务器。它默认使用 index.html 作为入口文件。项目结构跟之前测试 Webpack 时的类似，里面直接写 ES modules。注意它的入口文件直接引用的是 `src/main.js`，而不是打包后的 bundle.js。main.js 直接用 ES modules 写，引用了另一个模块 hello，hello 里是两个 function。

页面成功显示出来后，看一下服务端返回的文件：和本地 src 目录下的文件完全一致。main.js 点 Preview 发现跟源代码一模一样，hello.js 也一样。这就是这类工具宣传的 unbundled 开发环境：省掉了打包的漫长过程，而且和源代码一致，非常利于调错。

还有一个更好玩的：npm 依赖的处理。这里装了一个第三方模块 canvas，用来生成 canvas 烟花效果。把示例代码直接复制到 main.js 里保存刷新，一瞬间美丽的烟花就出现了。看一下 Snowpack 对这个第三方模块的处理：Node Modules 里的模块一般都写成 Node.js 标准的 CommonJS 格式，无法在浏览器中直接使用。其他打包工具通常把这些模块统一打包进一个或几个文件，而 Snowpack 采用了另一种机制：先扫描 Node Modules 中的模块，找到要使用的模块，然后把每个模块分别转换成单个的 JS 文件，且都是 ES modules 格式，可以被浏览器直接使用。比如装了 React、React DOM，就会转换成类似 `/_snowpack/pkg/...` 的模块。我们的例子里，main.js 引入了 `/_snowpack/pkg/canvas` 就产生了烟花效果。有更多的 node modules，每个模块都会转换成对应的唯一文件。

最后说 build，也就是为生产环境打包。Snowpack 默认生成的文件和开发环境几乎完全一致，这体现了它的信条：You should be able to use the bundler because you want to, not because you need to。意思是，为生产环境打包代码时，只有当你想生成全浏览器兼容的代码时才需要用 Bundler，这不该是必须项。如果只希望支持最新版浏览器，就没必要用 Bundler。

当然它也提供了插件来生成兼容性更全面的代码。比如想生成类似 Webpack bundle 的产物，可以用 `@snowpack/plugin-webpack`：在默认配置文件 `snowpack.config.js` 的 plugin 里配置这个插件，然后运行 `npx snowpack build`。构建完成后在 build/js 下生成了两个文件：一个把整个内容打包进去、带哈希值的 main JS 文件，另一个是 Webpack 运行所需的 runtime 文件，底层就是用 Webpack 打包的结果。

总结一下：Snowpack 是一个另辟蹊径的打包工具，更关注开发环境的迅捷，理念和 Vite 很类似。开发环境使用 ES Modules 模块类型，并把第三方 Node Modules 做了简单的格式转换，给开发带来非常大的便利，速度也飞起。但到生产环境，如果想支持全浏览器，它底层还是依靠其他打包工具，比如 Webpack 或者类似 Rollup 的理念。区别在于它给了你选择的权利：只要支持最新浏览器的话，把一堆文件打包成一两个 bundle 文件就不是必选项。
