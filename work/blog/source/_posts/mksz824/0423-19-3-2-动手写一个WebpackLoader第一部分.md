---
disableNunjucks: true
title: 19-3-2 动手写一个WebpackLoader第一部分
date: 2026-11-17 11:03:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课深入了解 Webpack 中很重要的一个概念：Loader 的工作原理。Loader 作为 Webpack 的核心机制，内部的工作原理其实非常简单。我们之前简单了解过 Rollup Loader 的原理，Webpack 跟它有异曲同工之妙。接下来一起开发一个自己的 Loader，通过这个过程来了解 Loader 的内部原理。

## 需求：加载 Markdown 文件

我们开发一个可以加载 Markdown 文件的 Loader，以便在代码中直接导入 md 类型的文件。Markdown 一般需要转换成 HTML 再呈现在页面上，所以我们希望导入 md 文件后，直接得到 Markdown 转换后的 HTML 字符串。

新建了一个 test.md，里面是一段非常简单的 Markdown。然后在 main.js 中导入它：

```js
import './test.md';
```

直接运行 webpack 肯定会报错，因为我们没有添加任何关于 md 的处理规则，所以现在要新建一个本地 loader 来处理它。建好之后称之为 markdown-loader.js。

## Loader 的基本形态

每个 webpack loader 都需要导出一个函数，这个函数就是 loader 对资源的处理过程：输入是加载到的资源文件的内容，输出是加工后的结果。

```js
module.exports = (source) => {
  const content = source;
  console.log(content);
  return 'hello';
};
```

参数 source 就是整个文件的源代码（source file content），对于 Markdown 来说就是那段字符串。可以用 console.log 证明一下内容，然后先直接返回 hello，导出成 module 的默认模块。

有了它以后，在 webpack 配置中添加对应的规则来处理 md 文件。在 rules 数组中多添加一项：test 写一个正则，处理 .md 结尾的文件；use 一个数组，里面有一项，可以直接写本地文件的地址：

```js
{
  test: /\.md$/,
  use: ['./markdown-loader'],
},
```

## 第一个坑：必须返回 JS 代码字符串

运行 npm run build，可以看到 console.log 输出了 Markdown 源文件的内容，说明 loader 被正确调用了。但刷新页面后报错了：hello is not defined。打开 bundle.js 格式化之后，拉到最后一个模块，可以看到这个 function 中直接把 hello 放在了那里，所以报错。

为什么？Webpack 加载资源文件的过程类似一个管道，可以在这个过程中依次使用多个 loader，但这个管道最后的结果必须是一段标准的 JS 代码字符串。而我们直接输出了一个 hello，它不是一段标准的 JS 代码，所以报错。

解决方法也想到了：在 loader 中返回一段 JS 代码字符串。

```js
module.exports = (source) => {
  const content = source;
  console.log(content);
  return 'console.log("hello")';
};
```

重新打包 npm run build，再刷新页面就不报错了，hello 打了出来。查看最后一个模块的代码，正是我们返回的那句 console.log('hello')。

## 接入 Markdown 解析

了解了 loader 的工作机制后，回到 markdown-loader.js 接着完成需求：安装一个能把 Markdown 解析成 HTML 的模块，称为 marked，安装命令是 `npm install marked --save-dev`。它可以将对应的字符串转换成标准的 HTML：

```js
const marked = require('marked');

module.exports = (source) => {
  const html = marked(source);
  const code = `module.exports = ${JSON.stringify(html)}`;
  return code;
};
```

marked 的参数是我们输入的 Markdown 字符串，返回一段 HTML。如果直接把这段 HTML 返回，会面临和刚才一样的问题（不是 JS 代码，没法解析），所以正确的做法是把这段 HTML 字符串拼接成一段 JS 代码：通过 module.exports 把字符串导出。

这里有一个细节要注意：假如简单拼接，HTML 中的换行和引号都可能造成语法错误，所以用一个小技巧 JSON.stringify 处理一下，它会把换行、引号和空格都转义掉。

最后试一下好不好用，还是 build 一次，刷新页面：这两段字符串都可以完美地解析出来，并且可以直接添加到页面当中。

这节课成功创建了第一个 Webpack Loader，完成了 Markdown 的转换工作。Loader 虽然看起来复杂，内在的道理还是比较简单的。下节课继续看多个 Loader 的工作原理。
