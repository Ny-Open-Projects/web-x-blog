# 19-4-9-使用chainWebpack修改webpack已有配置

经过前面一段时间的优化，我们其实已经掌握了 Webpack 优化静态文件的大体思路和方式，学会了很多方法。在这章的最后，再介绍一点和优化没有关系、但我认为非常重要的方法。

## 问题：修改插件的参数很难

我们都知道 Vue CLI 给我们预设了一系列的 Webpack 配置，可以把它导入到一个文件中（比如 sample.webpack.js）。现在想去修改这个配置。对于修改自定义 Webpack 配置，我们已经掌握了 configureWebpack 这个字段：它可以拿到对应的 config，在 config 对象中拿到 webpack 的一系列配置进行修改，看起来可以完成各种任务。

但这时候有一个特殊的任务：我们想修改整个输出的 HTML 的标题，这样做可以改善 SEO。首先要知道 HTML 页面是怎样生成的：它使用 HtmlWebpackPlugin 生成，这个插件之前已经介绍过，可以自动生成一个 HTML，按照配置替换对应的项，以及动态插入 script 和 style 等一系列操作。

它的模板是 public/index.html，这是我们创建的一个普通 HTML 文件。里面有一些神奇的占位符，比如 options.title。再看插件对应的变量就明白了：处理过程中这些占位符会被替换成对应的变量。title 是从 package.json 直接拿的，也就是项目的名称。看最终生成的文件（dist/index.html，format 一下），title 被替换成了 OpsFlow，并且动态插入了一系列 script，这就是它的工作原理。

明白原理之后，我们知道只要修改 title 这个值即可。但假如使用 configureWebpack 来做，会发现很麻烦：首先需要在插件的数组中找到对应的项（找到它的 index），这是一个很复杂的过程，而且数组有可能会发生变化；更要命的是它已经被实例化了，我们也不知道该怎样修改它的参数。这该怎么办？

## webpack-chain 与 chainWebpack

Webpack 给我们提供了对应的功能。文档中写了链式操作这个高级特性：Webpack 配置是通过 webpack-chain 来维护的。这个库提供了 Webpack 原始配置的上层抽象，可以定义具名的 loader 规则和具名的插件，并有机会在后期进入这些规则，对这些选项进行修改。文档下面已经有一系列非常详细的例子，帮我们理解它的强大之处。

我们要做的是修改插件里的选项。在 vue.config.js 中添加 chainWebpack 选项，跟 configureWebpack 相平行，返回的是一个 function，里面可以拿到 config：

```js
chainWebpack: (config) => {
  config.plugin('html').tap((args) => {
    args[0].title = 'OpsFlow';
    args[0].desc = 'low code platform OpsFlow';
    return args;
  });
},
```

拿到 config 后调用上面的 plugin 方法，通过它能拿到具体的插件。想修改哪个插件，就可以到 sample.webpack.js 里看，每个插件都有一个对应的名称，以注释的形式写在那里。我们要改的是 HTML 插件，就写 plugin('html')。

通过 plugin 拿到一个神奇的对象，上面有一个方法叫 tap。tap 里返回一个 function，function 中能拿到插件的 arguments（一系列参数），然后可以修改参数、返回新的参数，完成对应的工作。args 是什么还是需要看 webpack 最终的配置：它只有第一个参数，里面有一系列的值，只要修改 title 就可以了，设置为 OpsFlow。还想添加一个 description，不仅能修改还能添加：args[0].desc 等于我们整个页面的描述。修改完把 args return 出去，新的参数就生效了。

因为添加了 description，还要把它添加到模板 HTML 中去，是一个 meta 标签：

```html
<meta name="description" content="<%= options.desc %>" />
```

特别注意这里应该是 options.desc。重新运行 npm run serve，应用启动后查看源代码：description 已经做了对应的修改，title 也做了对应的修改，任务完成。

## css.loaderOptions 是一个快捷方式

我们发现 chainWebpack 可以实现强大的自定义和细粒度的修改选项，有这样的需求不妨在这个文件中做对应的修改。当然，写到这里大家应该有种似曾相识的感觉：我们其实是修改过某个 loader 的选项的。往上看配置文件里的 css.loaderOptions：想修改 CSS loader 的时候，我们是在这个选项进行修改的。

这其实是 vue.config.js 给我们添加的一个快捷方式。文档中也有说明：对于 CSS 相关的 loader 来说，我们推荐使用 css.loaderOptions，而不是直接链式指定 loader。也就是说 Vue CLI 提供了一个很方便的方法来实现这个功能，不需要繁琐地使用 chainWebpack 进行修改。当然它只有这一个快捷方式，其他选项还是要通过 chainWebpack 来实现自定义化。

这节课学习了使用 chainWebpack 修改 plugin、修改 module 的一系列规则，任务完成。
