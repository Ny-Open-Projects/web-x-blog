# 19-3-3-动手写一个WebpackLoader第二部分

上节课接触了 loader 的简单流程，这节课来学习多个 loader 的串联用法。在开始串联之前，先学习一个在 loader 中获取配置选项的用法。

## 在 loader 中获取 options

在 webpack 配置的 use 这个 object 中，我们可以传入一个称之为 options 的选项，为 loader 设定个性化的配置。那么在 loader 的代码中怎样获取这个配置呢？loader 函数的参数只有 source，没有第二个选项参数，这时需要一个第三方库来完成，叫 loader-utils。它是 webpack 的官方第三方库，提供了不少好用的方法。

我这里已经安装完毕，大家自行安装即可。引入之后调用 utilities 上的 getOptions 方法：

```js
const utils = require('loader-utils');

module.exports = function (source) {
  const options = utils.getOptions(this);
  const html = marked(source, options);
  return html;
};
```

特别注意：这里把 this 作为传入参数，而整个 function 原来是箭头函数，没有 this 绑定，所以要把它改成普通函数的形式（去掉箭头），现在就能拿到 options 了。

有了 options，希望在转换时给 marked 传参。marked 的文档里有一系列转换时的 options，我们用其中一个做实验：headerIds，默认是 true，转换过程中会给任何标题自动添加一个 ID。可以看到我们的 h1 现在有一个 about 这样的 ID。现在希望不要这个 ID。

先在 webpack.config 里传入想要的 options：headerIds 设为 false，然后把 options 传给 marked。npm run build 之后刷新页面，h1 上面就没有 ID 了，使用配置的任务完成。

## 多个 loader 串联的规则

有了这个小知识，就可以尝试将多个 loader 串联起来处理资源。当链式调用多个 loader 时，use 接受一个数组。特别注意：它会以相反的顺序执行。就像 CSS 的例子一样，从下而上执行，先执行 css-loader，再执行 style-loader。

多个 loader 串联的规则是：最后的 loader 最早调用，传入的是原始资源的内容；第一个 loader 最后调用，期望输出 JavaScript 和 source map，跟我们目前唯一一个 loader 是一个意思；中间的 loader 执行时，会传入前一个 loader 传出的结果，所以中间的 loader 不必产出 JavaScript 代码，直接产出对应的资源内容即可。整个流程就像一个 pipe，资源像水流一样一个一个流过去，最后完成最终的处理。

## 串联演示：HTML 再转回 Markdown

现在已经将 Markdown 转换成了 HTML。接下来我希望再多加一个 loader，把生成的 HTML 再转换回 Markdown。现实中这么做肯定多此一举，没人会这么干，但这里只是为了演示用法，它是一个很好的例子。

变化在于 markdown-loader 现在不需要返回 JavaScript 代码了，而是直接返回结果就好，所以把拼接 code 的部分注释掉，直接返回 HTML。

然后新建一个 loader，叫 markdown-html-loader.js。先把 loader-utils 拿过来，创建一个新的普通函数，接受 source 参数。第一个 loader 给它的内容是 HTML，第二个 loader 可以接力它进行下一步的处理。

完成 HTML to Markdown 的转换需要另外一个第三方库，叫 turndown，使用的人很多，安装命令是 `npm install turndown --save-dev`。它的使用文档都写得很清楚，我们照着写：

```js
const utils = require('loader-utils');
const TurndownService = require('turndown');

module.exports = function (source) {
  console.log(source); // 此时 source 已经是 HTML
  const options = utils.getOptions(this);
  const turndownService = new TurndownService(options);
  const markdown = turndownService.turndown(source);
  const code = `module.exports = ${JSON.stringify(markdown)}`;
  return code;
};

module.exports = markdownHtmlLoader;
```

首先引入 turndown；接着先 console 一下 source，看看传入时已经是什么样了。然后照猫画虎：新建一个 service，构造函数里可以传入 options，每个 loader 可以有对应的 options，我们把它传进去。然后调用 turndownService 的 turndown 方法，把 source 传进去，完成转换。因为它是最后一个 loader，需要输出 JavaScript 代码，所以把上节课的拼接 code 方式拷贝过来，把 HTML 替换成我们要的 Markdown，最后把整个函数导出。

写完之后把它添加到 webpack 配置中。它作为最后要处理的 loader，所以写在数组的第一位，loader 名称是 ./markdown-html-loader。

## 验证

运行 npm run build，可以看到第二个 loader 接收到的内容已经是 HTML。打开页面，已经变成了 Markdown。再细化一下：现在它的标题是用 setext 这种 Markdown 格式写的（内容下一行跟一串下划线），我们希望转换成井号在前的 atx 格式。turndown 有一个选项叫 headingStyle，默认是 setext，我们希望是 atx，所以在 webpack 配置中再给这个 loader 添加 options：headingStyle 设为 atx。

刷新页面，现在就转换成了井号标题的形式。

至此我们完成了整个 md 文件的处理，使用两个 loader 串联完成了任务。整个过程重点在于 loader 的工作原理和实现方式，通过这个例子大家应该已经了解得差不多了。
