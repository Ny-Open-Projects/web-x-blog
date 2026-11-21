# 13-8-使用 stream 模式完成图片上传以及缩略图生成

上节课我们学习了 stream 的基本使用和原理，这节课使用 stream 的方式重写上传文件的一系列逻辑。要完成的任务和之前一模一样：完成原始图片在项目文件夹中的保存以及缩略图的保存。不一样的地方是都要使用 stream 模式。

大家也许会想：既然已经使用 file 模式完成了文件的保存，为什么还要使用更难理解的 stream 模式呢？这样做是为了让大家更好地掌握 stream 这个知识点。其实 file 模式自动帮我们多做了一件事：它先使用 stream 把文件保存到一个特定的位置，然后再把文件提供给你，也就是之前看到的 request.files 里的文件。之后研读源代码的过程中，我们就可以更好地理解整个过程。

另外，使用 file 模式时，假如你想保存到一个特定的文件夹，只能修改它的根目录 tmpdir 为 uploads，但后面还会跟着一大堆按时间分类的子文件夹，这个格式写死在代码中，没法自定义。使用 stream 就有更多的可操作空间，也可以更灵活地定制。

第一步，把 file 模式的 controller 注释掉，使用 stream 模式完成任务。创建一个新的 function，称为 async fileUploadByStream，代表使用 stream 的上传模式。第一步还是把老三样中的 ctx 和 app 拿出来。

file 模式下我们使用 ctx.request.files 拿到文件，而 stream 模式下可以使用一个特殊的方法直接返回对应的 readable stream：`const stream = await this.ctx.getFileStream()`。注意这里是一个 await，它返回 promise。点进去看它的定义，是 FileStream 类型，继承自 Readable，所以它是一个可读流，并且在可读流上扩展了一些属性，就是文件的基本信息，比如 filename、encoding 等等一系列属性。

拿到这个 stream 以后，就可以使用上节课学的流的方法生成对应的文件。首先要确定文件要保存到哪里，我们想保存在 uploads 文件夹，然后生成一个随机的文件名，比如 xxx，扩展名保持不变；另外还要生成缩略图的路径：uploads/xxx-thumbnail.ext，跟上节课一样。

我们发现自定义保存的格式会稍微简单一些，不需要添加那么多按日期分类的文件夹。现在完成这个任务。首先生成一个 uid，也就是随机的字符串，用我们已经用过多次的 nanoid：`const uid = nanoid(6)`，生成六位的 id。接下来生成保存的路径，称为 saveFilePath，使用 join 组合出这样的结构：一开始拿到 config 上的 baseDir（项目文件夹），添加 uploads，然后是 uid 加上文件的扩展名。单独拿扩展名可以使用 path 上的 extname 方法，把文件名称传进去。文件名称刚才说了，stream 上有一个特殊属性 filename，可以拿到文件的名称。这样组合就完成了。

thumbnail 的 path 也生成一个，非常类似，直接复制过来，唯一是在文件名里多添加一个 thumbnail 字符串。有了这两个文件位置，有了可读流，还需要可写流，把数据写到对应的位置去。所以需要 createWriteStream，从 fs 中拿取。第一个称为 target，createWriteStream(saveFilePath)；第二个是 targetTwo，保存缩略图的位置，createWriteStream(saveThumbnailPath)。

有了它们俩就可以进行对应的操作了。之前学习的 stream 都使用 pipe、on 这样的写法，我们这里希望把它转换成 promise，因为整个应用大量使用了 promise，可以使用 async/await 的逻辑书写，更熟悉一些。所以要运行两个 promise：一个是生成普通图片的 promise，第二个是生成缩略图的 promise。

先创建第一个，称为 savePromise，做一个转换：new Promise((resolve, reject) => {...})。stream 从这个可读流 pipe 到一个可写流，自然是 targetOne（不是 targetTwo）。然后 .on('finish', resolve)，finish 的时候 resolve 掉，说明成功了；.on('error', reject)，出错的时候调用 reject。这样第一个就改装完毕了。

第二个 promise 的流中需要一个转换流，也就是使用 sharp 进行 resize。sharp 支持这样的写法，可以直接生成一个转换流帮我们处理。写一个 transformer 生成对应的转换流：sharp().resize({ width: 300 })，不需要传任何参数，只调用 resize 转换到 300。上节课学了转换流的力量：可以从一个可读流拿到数据，转换成另外一个可读流，再导入到可写流。

接下来是第二个 promise，thumbnailPromise，new Promise 跟刚才格式一样：resolve、reject。唯一不一样的地方是要多一步：stream 首先要 pipe 到一个转换流，也就是刚才创建的 transformer，然后再 pipe 到可写流 targetTwo。on finish 和 on error 复制过来就可以了。

现在两个处理的 promise 都转换完毕了，下一步运行它们。有两个 promise 怎么运行？当然使用 await Promise.all，里面是一个数组：先运行 savePromise，再运行 thumbnailPromise。运行它俩以后就应该生成两个对应的文件。最后返回：ctx.helper.success({ ctx, data: response })，response 里面要生成两个对应的 URL，需要做对应的转换。这个 replace 我把它单独拿成一个方法，更简单一些，称为 pathToURL，传入一个 path，返回一个对应的 URL。这样 url 和 thumbnailUrl 就都生成完毕了。

最后测试应用是否好用，看能不能生成两张图。还是使用这个接口，把 router 里的 fileLocalUpload 换成 uploadByStream。点击 send，希望返回两个对应的 URL。可以看到两个 URL 都返回了。用其中一个做测试，缩略图也成功生成了：uploads 文件夹下加一个随机的字符串，后面是 thumbnail，png 是它原始的扩展名。

看起来我们就完成了这个任务。功能一样，但和之前的做法已经大相径庭：这次是直接拿到上传文件的可读流，完成文件在特定位置的转换和写入。通过这个例子，相信大家可以更好地掌握 stream 的用法。
