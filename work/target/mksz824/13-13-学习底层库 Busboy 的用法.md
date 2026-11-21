# 13-13-学习底层库 Busboy 的用法

上节课学习了使用流上传单文件到云服务的方式，而我们的任务是完成多文件上传。文件模式的多文件上传大家应该都能写出来：files 是一个数组，循环数组给每个文件调用对应的方法即可。这里要学习的是流上传多个文件的方式。为了了解它，要深入流的方式探索，先研究一个几乎所有框架上传文件都要使用的底层库：Busboy。

## Busboy 是什么

Express 使用的 multer（用户非常多）或者 koa 的 multipart，底层都依赖 Busboy，官方也是这样描述的。可以这么说：Node.js 上传文件的应用程序，都使用了 Busboy。它有什么魔力？了解一下它的基本用法，这个底层库也可能在某些特定场合帮到你。

Busboy 的定义：A Node.js module for parsing incoming HTML form data，专门用来解析 form data，特别针对 multipart 数据类型，可以很好地区分普通文本内容和文件类型的内容。它不限于任何框架，例子中直接使用原生的 HTTP createServer 以及 req、response 这两个原生对象。

安装时除了本体外，特别注意还要安装 @types/busboy 类型文件。

## 基本用法：基于事件

在应用里做对应的修改。创建一个 controller，称为 testBusboy。第一步引入 Busboy（`import * as busboy from 'busboy'`），拿过来 ctx 和 app 两个老朋友。

先测试它基于事件的方式。第一步 new 一个实例：`const busboy = new Busboy({ headers: ctx.req.headers })`。参数 headers 要来自原始的 req 对象。注意不能用 ctx.request，那是经过 koa 魔改以后的对象；要拿原始对象用 ctx.req，它就是 node 的原始对象，把它的 headers 属性放上去。这里会有一个类型错误，因为两个定义文件之间有版本差异，做一个简单的类型断言暂时通过即可，之后我们不会使用任何相关的类型。

有了实例，就可以绑定一系列事件：

- `busboy.on('file', ...)`：拿到 file 时触发，参数有三个：fieldName（字段名）、file（文件流，可读流）、filename（文件名）。先用 logger.info 都打印出来观察；
- `busboy.on('field', ...)`：拿到普通文本时触发，两个参数：fieldName（键）和 val（值），也打印出来；
- `busboy.on('finish', ...)`：处理完毕后触发，打一个 finished。

最后把 `ctx.req` pipe 到 busboy 实例中去，完成整个处理。

它的原理其实很简单：multipart 发送的数据根据 boundary 分割，然后按不同类型处理。普通文本（field）拿到 name 和里面的值；file 类型拿到 name、filename 和里面对应的值。

把 router 暂时改成 testBusboy，测试。请求里有一个文本节点 hello 和一个 file 节点，应该分别输出不同的内容。响应是 404，因为我没有任何返回，看日志：第一个是 field 事件输出的 hello test；第二个是 file 事件输出的，包括 fieldName、一个 file（readable 类型的可读流）、以及文件名 bubble.png。通过这种方式就拿到了不同的数据类型。

## 进阶：多文件保存到本地

第一步测试完成，再做另一个测试：使用 Busboy 完成多文件保存到本地。保存到本地和上传到云端是一样的。

创建一个新的方法 uploadFilesUseBusboy，做成一个 promise，调用时返回一个数组，数组里是文件的路径。`return new Promise((resolve) => {...})`，把刚才的函数体拷贝进去，做一些处理工作。

on file 时把文件写到本地，和之前的写法一致：先创建 uid 等于 nanoid(6)，再创建 savedFilePath 等于 `join(baseDir, 'uploads', uid + extname(filename))`，仍然传到 uploads 目录，文件名用拿到的 filename。file 是一个可读流，直接 pipe 到可写流：`createWriteStream(savedFilePath)`。

为了最后输出数组，再创建一个空数组 `results: string[]`。用 file 流的 end 事件：当完成写入时，把这一项 push 进去，`results.push(savedFilePath)`。on field 保持输出信息即可。最后在 finish 事件里 `resolve(results)`。把 Promise 的返回类型确定成 string 数组（现在还是 unknown）。

然后修改 controller：改成 async，`const results = await this.uploadFilesUseBusboy(ctx)`，上传完毕后返回 success，response 就是 results。

## 测试

测试时多添加一个 file：请求里有了一个文本字段和两个文件字段。点击 Send，两个文件都完成了处理，并且保存到了对应的 uploads 文件夹，测试成功。

到这里，其实我们已经可以用 Busboy 完成多文件上传了：拿到 file 可读流之后，如果调用 OSS 上的方法，就可以完成云上传。感兴趣的同学可以用这种 Busboy 的原始方式改造一下，完成云端上传。不过这里我们还是要探究一下 egg.js 在 Busboy 上做的修改，以及它最终采用的方式。

这节课的主要任务是学习 Busboy 的基本概念。通过这个例子，大家可以比较基础且深入地了解 Busboy 的工作原理：它是基于事件的方式，代码不复杂，原理表达得非常清楚。
