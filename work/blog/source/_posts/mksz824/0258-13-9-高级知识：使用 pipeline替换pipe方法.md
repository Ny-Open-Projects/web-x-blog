---
disableNunjucks: true
title: 13-9 高级知识：使用 pipeline替换pipe方法
date: 2026-11-17 16:18:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们使用 stream 模式完成了文件的保存，看起来工作得很完美，但是有没有什么问题呢？这节课讲讲比较高级、而且在工作中非常实用的内容。stream 是 Node.js 中新手最容易出问题的地方，尤其我们使用的 pipe 方法。

试想，假如这串代码中某个环节出错了，自然可以想到我们在运行 promise，可以用 try/catch 对它进行错误捕获。添加 try 包住对应的 promise，假如有任何错误，直接 return ctx.helper.error。我在这里添加了一个 errorType，称为 IMAGE_UPLOAD_FAIL，已经添加完了，大家自己去创建一个新的 error 类型的定义就好。

现在假如在这里故意制造一个错误，应该会被捕获到并直接返回对应的错误。试一下是否按我们所想的运作。创建一个 readable stream：createReadStream，把 stream 替换掉，文件地址传一个 fake.txt，一个错误的、不存在的文件。点击 send 看看服务器会有怎样的效果。大家可以看到，现在服务器整个都卡死了，没有任何反应。再来看 log，只弹出一行错误，并没有进行对应的反应。这就是说，实际使用的时候，一旦出现源文件不存在或者 transform 出错等等情况，进程会立马 crash 掉。

是的，国内绝大部分教程都不会告诉你：每使用一个 pipe，都需要对每一个 stream 进行错误处理。我们需要这么写：假如有一个 readStream，每次 pipe 的时候都要使用 on 对它进行错误处理。这样写丑爆了有没有？而且即使你是老手也经常容易踩坑。我们这里只在最后一个也就是 target 这里添加了 error，所以并没有捕捉到第一个流出现的错误，程序就会被卡死。

这时候就需要使用 Node.js 在 stream 上推出的新特性来解决这个问题，这是 Node.js 针对社区反映的这个问题特别推出的 API，叫 pipeline。它是 Node.js 10 以上版本才支持的函数。它采用了另外的写法：stream.pipeline 是一个 function，把这些流一一写在参数中，最后一个参数采用回调函数的形式进行错误的捕获，流中任何环节出现错误都可以在这里捕获掉。

使用 pipeline 来改造，看看还会不会出现之前的错误。把 pipeline 导进来：import { pipeline } from 'stream'。拿到以后做对应的修改，不使用 pipe，而是使用 pipeline：第一个参数是可读流 stream，第二个参数是我们要写入的可写流 target，最后是一个 error 回调。放上去可以看到它有对应的提示，跟官方文档的例子完全一样。

把它改造成 promise：假如出现 error 就调用 reject；假如什么问题都没有就 resolve。把原来的 pipe 写法注释掉。经过这个修改再看看能否捕获到最终的错误。应用会自动重启，重启完毕后点击 send。可以看到，虽然是第一个流出错，但使用 pipeline 以后也能获取到对应的错误并进行 reject，这样 try/catch 就可以直接拿到错误并输出对应的 errorType，任务完成。

当然，如果你不想自己把它修改成 promise（因为它使用的是 callback 的形式），Node.js 也听取了社区的建议，添加了很多默认的 promise API，替代这些丑陋的 callback 类型 API。举个例子，文件操作 fs 模块，可以从 fs/promises 下面把所有和文件操作相关的 function 拿出来，就可以进行 promise 类型的操作了。这个例子明显表明了这种现象，强烈建议大家使用 promise 类型的 API，抛弃之前的 callback 方式。

pipeline 也有默认的 promise 实现。看文档，它有 stream/promises，在这里就可以直接 await 这个 pipeline 了，不需要在回调函数中进行操作。但是特别注意：这个 API 是 Node.js 16 以上版本才添加的，想尝鲜的同学一定要把 Node.js 升级到够新的版本。升级还不算完，还要特别注意把 package.json 中的 @types/node 也升级成 16 以后的版本。我这里已经完成升级，这样才能自动获得一系列 TS 的提示。

现在看看怎样完成任务。使用 promises 类型的 pipeline：从 stream/promises 导入 pipeline。导入后做对应的修改，就不需要那么麻烦了，把 new Promise 的包裹全都删掉。第一个 promise 应该是 await pipeline(stream, targetOne)；thumbnailPromise 一样，把包裹删掉，写成 await pipeline(stream, transformer, targetTwo)，第一个入参是 stream，第二个是要经过的转换 transformer，第三个是 targetTwo 这个可写流。

这样我们就使用 pipeline 完成了对应的改造。写成这种方式以后非常简单明了，比原来舒服很多。最后测试一下这个方法是否好用：点击 send，应该生成两张对应的图片。可以看到图片生成了，没问题，一张原始图片，一张对应的缩略图。这样就使用 promises 形式的 pipeline 完成了对 pipe 的重写。

最后这条经验请大家一定要记住：原来的 stream.pipe 方法别再用了。它更倾向于让用户链式调用，但我们特别容易遗漏错误处理，要么写起来感觉很别扭。要使用最新的 pipeline 对 pipe 进行替代。我觉得这个在面试中可以作为亮点讲出去，面试官对你的 stream 知识会刮目相看。
