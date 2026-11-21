# 19-3-5-动手写一个Webpackplugins第二部分

这节课继续完成插件的编码。上节课简介了插件的写法、apply 方法以及 compiler 上不同的生命周期。我们的任务是完成一个插件：提示最终生成文件的大小是否符合要求。自然需要拿到最终生成的文件，所以生命周期肯定是在 done，也就是完成的时候进行处理。上节课的两个测试钩子先注释掉，我们需要的是 stats 这个对象。

## 从 stats 拿到 outputOptions

stats 对象中有很多属性和方法，几乎能拿到方方面面的数据。但现在没有 TS，只能盲人摸象，可以再次感受一下 TS 在复杂场景下的优点，大家课下可以把这个文件改装成 TS，好好对比感受一下。

我打开了 Webpack 提供的类型文件：stats 定义成一个 class，实例上有一系列属性和方法。这里需要一个特殊的属性 compilation。Compilation 是 compile 旗下的一个具体阶段，由于它很重要和特殊，所以单独拿出来做了一个对象。这个阶段就是 create new compilations or builds，生成具体代码的阶段。它也是基于事件的，可以在上面 tap 各种生命周期，数量非常多。

我们需要的东西是最终生成文件的类型，称之为 outputOptions。它在类型文件的 1393 行左右，类型是 OutputNormalize，点进去有一系列属性。打印出来看看：

```js
compiler.hooks.done.tap('bundle-size-plugin', (stats) => {
  const { path, filename } = stats.compilation.outputOptions;
  console.log(path, filename);
});
```

先从 stats 拿到 compilation，再拿到 outputOptions。运行 npm run build，可以看到这个对象里有两个有用的属性：path 是路径，filename 是最终生成的文件名。有了 path 和 filename，组合起来就可以用 Node.js 的 fs 模块上的方法拿到文件大小了。

## 计算文件大小

完成整个任务：

```js
const path = require('path');
const fs = require('fs');

compiler.hooks.done.tap('bundle-size-plugin', (stats) => {
  const { path: outputPath, filename } = stats.compilation.outputOptions;
  // generate a bundle path
  const bundlePath = path.resolve(outputPath, filename);
  // get file size in KB
  const { size } = fs.statSync(bundlePath);
  const bundleSize = size / 1024;
  // ...
});
```

首先把 path 和 filename 取出来（加一行注释 get path and filename from outputOptions），然后把它们拼接成一个组合路径：用 path 模块中的 resolve 方法，第一个参数是路径，第二个是文件名，生成 generate a bundle path。

有了它就可以读取文件大小：使用 fs 上的 statSync 方法（有异步的 stat 和同步的 statSync 两种，用同步的这个），传入 bundlePath。stats 上有一个 size 属性，number 类型，拿到文件大小。特别注意它是以字节为单位的，希望转化成多少 K，所以做一个转换：size 直接除以 1024，得到 bundleSize。

## 与配置比较并输出警告

有了大小，就可以和插件的配置进行比较。在 options 中拿到对应的参数，称之为 sizeLimit（从 dist options 拿 sizeLimit）。在 webpack config 中传入：new BundleSizeWebpackPlugin({ sizeLimit: 3 })，也就是最大等于 3KB。

然后是一个简单的判断过程：假如小于 sizeLimit，就提示 safe bundle size；假如大于，就提示 unsafe bundle size，并且输出一系列的信息：

```js
if (bundleSize < this.options.sizeLimit) {
  console.log('safe bundle size', `${bundleSize}KB`);
} else {
  console.warn('unsafe bundle size', `${bundleSize}KB`);
}
```

把多余的 console.log 删掉，直接运行。当前大小是 4.85KB，sizeLimit 是 3，所以输出了 unsafe，给你一个提示：bundle size 太大了，要想办法把它优化一下。

## 小结

通过这个过程我们就描述了整个 plugin 的工作原理。最根本的就是：apply 方法可以获取 compiler 这个对象，然后通过 compiler 不同阶段的钩子函数，使用 tap 把逻辑 tap 进去，tap 进去之后能获取不同的参数；拿到参数之后，可以将自定义逻辑一一植入，它可以劫持和修改整个编译的默认过程。原理就是这样，这节课就到这里。
