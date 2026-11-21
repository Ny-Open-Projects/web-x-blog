# 19-3-4-动手写一个Webpackplugins第一部分

这节课来学习 Webpack 的另外一个概念：Plugin 插件的原理。Loaders 是对代码中具体某一种资源的转换输出，而 Plugins 更偏向对整体流程的掌控。对开发者来说，可以通过 Webpack 构建流程中的每个阶段劫持做一些代码处理；对使用者来说，可以通过各类插件实现诸如自动生成 HTML 模板、自动压缩图片等等一系列整体的功能。官方有一个插件教程，大家可以去看，但它写得比较复杂，这里就不展示页面了，直接说插件应该长什么样。

## 插件的格式

官方文档中写了几条：

1. 它应该是一个 JavaScript 函数或者 JavaScript 类；
2. 它在原型上要自定义一个 apply 方法，会在安装插件时被调用，并且被 webpack compiler 调用一次；
3. 要指定一个触及到 webpack 本身的事件钩子（hooks），用于在特定时机处理额外的逻辑。

光看概念很难理解，直接用代码来说明。现在创建一个插件，任务是检查最后生成的文件的大小，当大于特定大小时输出一个警告。这个 plugin 本身比 loader 要复杂很多，通过这个例子只是让大家了解插件的基本运作原理，也就是插件的冰山一角。

## 创建插件类

新建文件 bundle-size-webpack-plugin.js。按规则一，创建一个类：

```js
class BundleSizePlugin {
  constructor(options) {
    this.options = options;
  }

  apply(compiler) {
    console.log('bundle size plugin');
  }
}

module.exports = BundleSizePlugin;
```

constructor 里有 options，可以接收一系列参数。第二步很重要：在原型上定义 apply 方法，它有一个参数称为 compiler。这个 compiler 就是 webpack 编译器本身，假如把它 console.log 出来会发现非常复杂，有了它基本可以掌控整个编译阶段。这里不展开它所有的属性，感兴趣可以看文档，我们聚焦在要完成的任务上。

有了 compiler，我们希望触及整个编译过程的各个阶段，也就是生命周期。这和 DOM 元素以及 Vue 组件的实现方式一样，都是基于事件的。为了在指定的生命周期做自定义的逻辑处理，需要在 compiler 的 hooks 上植入自定义逻辑。hooks 非常多，也就是阶段非常多，文档在 compiler hooks 这一节，每个 hooks 有不同的对应参数，比如 environment、afterEnvironment、run、watchRun 等等。

## 植入钩子逻辑

先测试一个钩子：compile，表示编译这个阶段。在 compile 后面有一个方法叫 tap，可以把你的逻辑植入到这个阶段。tap 是一个 function，接受两个参数：第一个是插件的名称 bundle-size-plugin；第二个是回调函数，文档中有 callback parameters，每个阶段的参数不一样。在 compile 阶段能拿到 compilation params，把它打印出来看看：

```js
compiler.hooks.compile.tap('bundle-size-plugin', (compilationParams) => {
  console.log('compile', compilationParams);
});
```

导出之后就可以使用了。在 webpack.config.js 中导入这个插件，添加到 plugins 数组的第一位：new BundleSizeWebpackPlugin()。

运行 npm run build，可以看到它输出了一系列信息：首先是 bundle size plugin，这是 apply 里 console 的信息；然后到 compile 阶段，参数拿到了一系列关于 compile 的内容。

## done 阶段

再在另外一个生命周期里写一段逻辑。这个生命周期叫 done，所有工作完成以后调用，对应的参数叫 stats，能拿到打包完毕后所有文件和参数的信息。照猫画虎：

```js
compiler.hooks.done.tap('bundle-size-plugin', (stats) => {
  console.log('done', stats);
});
```

我们最终要完成的任务（判断最后文件的大小）需要在所有过程都结束、拿到对应的文件之后才能做，所以逻辑应该添加在 done 这个生命周期。运行之后可以看到 stats 的信息非常多，几乎滚不到最上面，说明拿到了 webpack 打包成功以后的一系列信息。

## 小结

插件的基本格式就是一个 class 或者 function。class 里有一个很重要的方法 apply，在 apply 上可以获取 compiler 这个 Webpack 编译器实例；compiler 上提供了 hooks，通过 hooks 可以在不同阶段植入逻辑，比如我们测试了 compile 阶段和 done 结束阶段。插件的第一部分知识就到这里。
