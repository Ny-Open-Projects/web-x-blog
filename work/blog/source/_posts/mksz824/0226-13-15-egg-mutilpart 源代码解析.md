---
disableNunjucks: true
title: 13-15 egg-mutilpart 源代码解析
date: 2026-11-17 14:46:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课完成了多文件的流式上传，也了解了一些 multipart 插件的原理。这节课通过 egg-multipart 源代码的分析，解释一下 egg 提供的上传相关属性是怎样来的。

## 先回顾用过的属性

第一个是 ctx.multipart，上节课已经分析过：它其实就是 co-busboy 的返回值，直接 return 了 parts 的调用方法。使用时调用它，返回一个可以多次执行的 promise，每次拿出 body 数据的一部分，直到数据被完全拿完（返回 undefined）。

重点分析之后用过的两个 context 属性：getFileStream 和 ctx.request.files。

## 自己先想想怎么实现

看源码之前，先自己想想如果是自己来完成该怎么写。

**getFileStream**：它仅针对单文件，只能拿到一个单独的 file stream。思路自然是：调用一次 `await parts()` 拿到第一部分。特别注意一个问题：怎样确保拿到的 parts 是 stream 而不是普通文本 field？因为 multipart 里不仅有文件还有普通文本。之后可能还要判断 stream 是否有效、是否超过文件限制等等。最后直接把 stream 返回，供框架中使用。

**ctx.request.files**：它是一个数组，保存了和文件相关的一系列信息。第一步应该判断是否是 file mode（multipart 有一个参数叫 mode，只有在 file mode 下才会有这个属性）。如果是 file mode，应该在中间件中运行一个特殊方法，步骤是：保存文件，生成一个包含文件信息的数组，然后把它赋值给 ctx.request.files。具体过程和上节课写的很相似：`while (part = await parts())` 一部分一部分地拿出数据，是文件流就保存到本地目录并把数据添加到数组，所有信息处理完毕后把数组赋值给 ctx.request.files。

## 验证 getFileStream 源码

现在见证一下分析是否正确。把源码 clone 下来，访问 extends/context.js。开头是一系列检查，略过。接下来和分析的一样，它直接调用 `this.multipart()`，也就是 ctx.multipart 返回 parts，可以多次 await。这里执行了第一次 await，然后直接认为拿到的是 stream，没有任何类型判断。

第一部分很有可能是文本，那怎样排除？它有一个特殊参数：multipart 的 options 里叫 `autoFields: true`。求助文档：If you want co-busboy to automatically handle the fields, set the autoFields to true. Now all the parts will be streams，即自动处理文本字段后，每一部分都会自动变成 stream。那文本字段去哪了？A field object array will be automatically be populated：看例子，返回值会多出一个属性 parts.fields，fields 里以 key-value 的数组形式保存所有文本相关的信息。通过这种方式保证拿到的每一部分都是 stream。这就解决了"怎样确保拿到 stream"的问题。

确保拿到 stream 后，自然还有一些判断，比如文件太大时监听 limit 事件抛出错误等等。总之最后返回一个 stream，也就是 fileStream 类型。这个方法比较简单，分析完毕。

## ctx.request.files：saveRequestFiles

最后看大头 ctx.request.files 是怎么来的。先看中间件 middleware/multipart。框架中它自动 enable 为 true，会执行。开头一句判断：fileMode 是否设置为 true，是才继续。再加两个判断：不是 multipart 直接 return；不是 file mode 也直接 return。两个都满足，说明在处理文件上传且 file mode 为 true，这时运行 `await ctx.saveRequestFiles()`，然后继续返回。所以关键点在 saveRequestFiles 这个方法。

进入 saveRequestFiles：一些判断略过。它有两个临时变量 requestBody 和 requestFiles，初始都为空。处理 parts 也使用 multipart，用 try/catch 加 do/while 的形式，和我们的写法其实一样：每个 part 拿出来；出现任何错误时执行 cleanUpRequestFiles，顾名思义是把 requestFiles 保存的文件都清理掉，做文件清理工作（可以自己看）。

`if (part.length)` 判断它是不是文本节点：之前说过，如果 part 是数组，part.length 就为 true，这时处理的是文本节点，可以拿到 fieldName 和 fieldValue，然后塞到 requestBody 当中（中间有些判断，不详细解释）。requestBody 初始为空对象，实际上就是把拿到的数据以 key-value 的形式保存进去，处理的是文本字段。

otherwise it's a stream：这时开始处理 stream。先给 stream 赋一些属性，与 part 拿到的属性保持一致。如果它没有 filename，empty part 直接 ignore，sendToWormhole。如果有，就开始保存。保存需要目录：它创建了一个 storeDir，前面是 tmpdir（我们之前设置成了本地的 uploads 文件夹），然后 moment().format()，这就解释了那些和日期相关的文件夹是怎样创建的：用 moment 按当前时间创建了一系列文件夹。再判断文件夹是否存在，不存在就创建，然后生成 filePath 和对应的 target，使用 pump 从 part（read stream）写到 write stream（target）。

这里补充一点：写这个插件的时候，Node.js 还没有推出我们现在使用的 pipeline 写法，所以这里的 pump 是他们魔改的一个支持 Promise 的 pipeline，本质上就是 part pipe 到 target，进行保存。保存完毕后 requestFiles push 一项。如果超过 requestFileSizeLimit（文件太大），就清理掉并抛出对应的错误。

最后 `ctx.requestBody = requestBody; ctx.requestFiles = requestFiles`。所以这个方法最终添加了两个属性：body 处理文本节点，files 处理上传的文件节点。

## 结论与收获

抽丝剥茧之后，这个方法其实不复杂，和我们的预期完全一致。现在 multipart 插件的源码分析就完成了。大家会发现：预先实现了各种方式的上传之后，再来分析源码会简单很多。其实它比我们的方案就多了一步手动上传、保存文件到本地目录。

由此也能更深刻地理解：直接使用 stream 的方法要比 requestFiles 快一些，因为 files 模式中间要保存一次文件，特殊情况下还要删除文件等一系列过程。所以从效率讲 multipart（stream）是最好的方式；为了好理解，files 是比较简单直观的方式，各有利弊。

这个源码分析也是面试时可以讲给面试官的亮点：大部分程序员都有使用这些高度抽象库的能力，但整个库是一个黑盒，对内部原理了解的人不多。我们不仅使用它，而且了解它的内在，这是很大的优势。希望通过这节课，大家把 multipart 插件以及整个文件上传的过程彻底弄清楚。
