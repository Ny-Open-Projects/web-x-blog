# 8-19-Jest 浏览器环境之谜

上节课通过图片预览的需求了解了读取图片的两种实践方法：一种是同步、比较简单的 URL.createObjectURL，另一种是异步、稍微复杂一点的 FileReader.readAsDataURL。这节课不要忘记给我们的 case 添加测试，同时学习一个新的知识点。

做类似业务时测试我们已经很熟悉了，但要注意抓住特殊的小点进行发散。这节课再演示一次：在已经看起来很熟知的过程中怎样学习新的内容。

## 编写测试

我创建了一个 only 的测试用例 "picture list mode should works fine"，创建了一个 wrapper，把 listType 设置成 picture，它应该渲染出带预览图片的列表模式。前面的逻辑都已经写完，只要写要测试的点。独特的 case 要测它关键、独特的点：

第一个是测试类名，因为 picture 模式下 ul 有特殊的类名。断言 `wrapper.get('ul').classes()` 应该 toContain 'upload-picture-list'（ul 根据 listType 添加了独特的类名）。

然后在 flushPromises 之后，列表长度要变成 1：`expect(wrapper.findAll('li')).toHaveLength(1)`，已上传完了一个 li。接着检测 image 是否正确渲染，这是 picture 模式最独特的地方：`expect(wrapper.get('li:first-child').find('img').exists()).toBe(true)`。

## 神秘的报错

保存运行，测试没有通过：没有找到对应的 image，并且报了一个错误：`URL.createObjectURL is not a function`，这就是出现错误的主要原因。

前面我们学过很多 mock 的知识：可以 mock 第三方模块（比如 axios），可以 mock 特定的组件（希望某个子组件用特定组件替换）。但 URL.createObjectURL 是 window 上本来就有的方法。既然 mount 整个组件貌似创建了一个类似浏览器的环境，为什么 window 对象上的一个 API 还是会报错呢？

原因就是：运行测试的过程中，mount 方法挂载了组件，但我们并没有创建一个真实的浏览器环境，而是采用了狸猫换太子的做法。Jest 运行整个测试用例的过程中，采用的环境叫 jsdom。在配置参数中可以看到 testEnvironment 的默认值就是 jsdom。注意文档说的是 "jsdom is a browser-like environment"，类似 browser，但不是真的 browser。

## jsdom 是什么

jsdom 是何方神圣？看它的首页：用的人很多，有 15.3k 个 star。简介说它首先是一个 JavaScript 的实现（JavaScript 库），模拟了非常多的 Web standards，包括 DOM 和 HTML 一系列标准，目的是在 Node.js 的环境下模拟大部分真实浏览器的 API 以及行为。它一般用于测试和爬虫两种用途。

现在搞清楚了：它就是在 Node.js 环境下提供了一大堆浏览器的标准对象来模拟环境。注意它这里写了一个词 subset，也就是只是一部分，另外一部分是不存在的：比如 window 上的 alert、confirm 等需要展示 UI 的方法都不存在。我们报错的地方 URL.createObjectURL 也是不存在的。

## 模拟缺失的 API

很简单，在测试中给它模拟一下就好：

```ts
window.URL.createObjectURL = jest.fn().mockReturnValue('test url')
```

用 jest.fn 模拟，直接 return 一个 test url，模拟就完成了。保存运行，测试通过，说明 image 已经出现了。

有了 image 还有一个重要检查点：image 的 src 对不对。把 image 拿出来设为 firstImage：`wrapper.get('li:first-child img')`，断言 `firstImage.attributes('src')` 应该 toEqual 模拟的值 test url。保存运行，没有问题，测试通过。最后把 only 去掉，看看之前的测试是否都通过，绿色的 pass 又出现了，原来的测试也全部通过。

这节课通过一个 window.URL.createObjectURL 的错误，深入到 jsdom 底层：在 Node.js 环境下运行时，是使用一个称之为 jsdom 的库来模拟浏览器的 API 的。但这个库并没有模拟全部的方法，假如没有，我们只能自己来，把它的实现自行创建和写一下。这节课就到这里，谢谢大家。
