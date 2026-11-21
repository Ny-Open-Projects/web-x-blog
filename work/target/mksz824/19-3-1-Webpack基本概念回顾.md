# 19-3-1-Webpack基本概念回顾

了解了环境变量的奥秘之后，这节课来学习 Vue CLI 底层的打包工具 Webpack 的基本概念。Webpack 是一个通用的 Module Bundler。之前有过 Rollup 的经验，应该对这类工具的本质有了比较深入的了解：从根本上说，就是把浏览器不支持的模块进行编译转换、合并，最后生成可以在浏览器良好运行的代码。

这节课作为开端，简单介绍一下 Webpack 的使用。用过 Webpack 的同学应该都比较熟悉，如果你已经很熟悉 Webpack 配置，可以选择跳过。这里直接用代码的方式快速复习 Webpack 的使用以及两大概念。

## 最基本的例子

第十三周出现过这个例子：用 ES6 写了一个脚本，里面引用两个另外的文件。第一个是 hello，里面有个 function，输出一个简单的字符串；package.json 是一个已经存在的 JSON 文件，version 是其中一个字段。最后在一个 DOM 元素上把它的 innerHTML 设置成对应的值，完成一个简单的功能。

Webpack 配置写在配置文件中，默认名称是 webpack.config.js，和 Rollup 非常类似，有入口和出口：

```js
module.exports = {
  entry: './src/main.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```

entry 是入口文件，我们选用 main.js；output 是出口，path 指文件夹路径，这里创建一个新的 dist 文件夹，filename 称之为 bundle.js。运行 npm run build（内部就是直接调用 webpack），bundle.js 就生成了。我创建了一个 index.html，它直接引用了 dist/bundle.js，并有一个 root 的 DOM 节点。最终页面输出了 Hello Viking 1.0.0，两个方法都成功执行。

通过这个例子可以看出，Webpack 天生支持两种类型的文件：一种是 JS 模块文件，ES modules 和 CommonJS 都支持；另一种是 JSON 文件，Rollup 本身不支持（需要插件），而 Webpack 可以直接把 JSON 转换成 JavaScript 的对象。对于其他类型的文件，它和 Rollup 一样爱莫能助。

## Loader

在根目录创建一个 style.css，简单设置 body 的 background-color 为 yellow，把它 import 进来再运行，就报错了：error in style.css unexpected token，意思是它不知道怎样处理这种类型的文件。这时就需要和 Rollup 一样的针对不同类型文件的处理机制，在 Webpack 当中称之为 Loader。

文档中说，Loader 用于对模块的源代码进行转换，可以在 import 或加载模块时预处理文件。为了处理 CSS 文件，需要一个特殊的 loader，叫 css-loader（需要自行安装）。在配置中添加 module 字段，module 中创建一系列 rules：

```js
module: {
  rules: [
    {
      test: /\.css$/,
      use: [{ loader: 'css-loader' }],
    },
  ],
},
```

rules 是一个数组，可以添加多种多样的规则。每条规则是一个 object，test 字段用正则表示要处理什么类型的文件，这里处理以 .css 结尾的文件；use 表示用什么 loader 来处理，它也是数组，因为一个类型的文件可以用多种 loader 处理。

添加完之后，刚才的报错没有了，bundle.js 也能成功生成，说明 loader 已经起作用。但页面上还没有出现样式，body 没有变成黄色，这是因为 css-loader 只是对 CSS 做了处理，并没有把它添加到页面上去。想添加到页面上，需要另外一个 loader：style-loader。这就是多个 loader 串联的用法，rules 允许你在配置中指定多个 loader。

loader 可以串联，排序是有规则的：从下到上执行，下面的先被执行，上面的后被执行。所以要添加 style-loader 时，把它放在 css-loader 的下面：

```js
use: [{ loader: 'style-loader' }, { loader: 'css-loader' }],
```

也就是先执行 css-loader，再执行 style-loader。style-loader 的作用是把 css-loader 拿到的值 append 到页面的 style 标签上去。保存后运行 npm run build，刷新页面，黄色的背景出现了，说明 style-loader 生效了。这就是 Loader 的简单知识，和 Rollup 非常类似。

## Plugin

除了 Loader，Webpack 还有一个重要概念：Plugins，顾名思义是插件。文档中说，插件是 Webpack 的支柱功能，目的在于解决 Loader 无法实现的其他任何事。我自己的理解是：Loader 解决的是各种不同资源的问题，而 Plugins 更多解决的是项目整体的一系列问题。

这里演示两个 Plugin，一个是内置的，一个是第三方的。使用内置的 plugin 需要把 webpack 引过来。第二个插件解决的是这样一个问题：我们每次都要手动建立一个 html 文件并手动输入它的路径，假如文件路径变了，还得手动处理。我希望有一个插件自动生成 html 文件，这就是第三方插件 html-webpack-plugin（需要自行安装）。

插件的添加很简单，新添加一个 plugins 字段，它也是一个数组，接受任意多个插件：

```js
plugins: [
  new webpack.ProgressPlugin(),
  new HtmlWebpackPlugin(),
],
```

第一个是内置的 ProgressPlugin，可以显示打包的过程；第二个就是第三方插件 HtmlWebpackPlugin。执行 npm run build，可以看到除了 bundle.js，还生成了 index.html，这就是插件的功劳。看看 dist/index.html 的内容，它输出了一段默认的 HTML 代码，并且 src 设置成了我们的 output 文件名，也就是 bundle.js。

## Vue CLI 中的 Webpack 配置

这就是 Webpack 的基础理念，非常简单，和 Rollup 有几分类似。现在来看看 Vue CLI 打包过程中使用的 Webpack 配置。回到之前的项目，vue-cli-service 有一系列命令，其中有一个内置的命令叫 inspect，可以检查当前采用的 Webpack 配置：

```bash
vue-cli-service inspect > sample.webpack.js
```

这个配置非常长，所以用 Linux 的管道写法，把输出导入到 sample.webpack.js 文件中。打开它是一个很长的 JSON 文件，是一系列配置，但很多我们都很熟悉：比如 output；还有 module 字段，下面的 rules 也是一系列的规则，比如遇到 vue 类型的文件会使用 node_modules 下的 vue-loader，我们知道它肯定是读取 vue 文件的。

除了 loaders，它还有一系列 plugins。在 1695 行左右可以看到 plugins 是一个数组：之前我们说过它可以把变量注入进去，这时就使用了 DefinePlugin，它把一系列环境变量注入到应用当中，还有其他的变量，大家可以自己了解。

所以这个配置虽然复杂很长，但无非是 plugins 和 loaders 的组合：loaders 负责对要处理的文件类型进行转换；plugins 负责整体流程的各种处理。大家课下简单看看这个文件即可，不用陷入其中，知道大概的意思就好。

这节课我们了解了 Webpack 的配置文件以及它的两大概念：loader 和 plugin。下节课继续深入了解 loader 是怎样工作的。
