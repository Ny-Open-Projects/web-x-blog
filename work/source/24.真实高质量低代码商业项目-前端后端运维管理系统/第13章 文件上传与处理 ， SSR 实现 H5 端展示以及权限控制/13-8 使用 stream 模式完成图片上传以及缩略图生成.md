大家好，上节课我们学习了 stream 的基本使用和原理。

那么这节课呢，我们就使用 stream 的方式呢来重写这个对应的上传文件的这一系列逻辑啊。

我们要完成的任务呢和之前一模一样，完成原始图片在项目文件夹中的保存以及缩略图的保存。

那么不一样的地方呢，就是我们都要使用 stream 模式。

这里大家也许会想呢，我们既然呢已经使用 file 模式完成了对应的这个文件的保存，为什么这里我们还要使用更难理解的 stream 模式呢？

这样做呢，是为了让大家更好的掌握 stream 这个对应的知识点。

其实呢，假如我们使用 file 模式啊，它是自动的帮我们多做了一件事啊，它是先使用这个 stream 保存到文件到一个特定的位置，然后呢再把文件提供给你，也就是我们之前看到的啊，在这个 request files 里面这个文件给你去使用啊。

之后在研读源代码的过程中呢，我们就可以更好的理解它的整个过程。

但是呢，使用这个 file 模式呢。

假如呢，你想保存到一个特定的文件夹，我们只能修改它的这个根的目录啊，time dir我们修改成uploads，但是呢，它在后面呢还会跟着一大堆按时间分类的子文件夹。

这个格式呢是它写死在代码中的，我们没法进行自定义。

现在呢，假如我们使用stream，就有更多的可操作空间，也可以更灵活的进行定制。

好，那么第一步，首先呢，我们把这个注释掉，我们不使用file模式，而是使用stream模式来完成对应的这个任务。

好，接下来呢，我们在这里创建一个对应的 function，我们称之为 async file upload by stream。

代表呢，这里面要使用 stream 的一个上传模式。

第一步呢，把这个老三样啊，把 ctx 和 app 给拿出来。

好，那我们在这个 file 模式下呢，可以使用这个 ctx request files 拿到对应的文件。

而在 stream 模式下呢，我们可以使用一个特殊的变量直接返回对应的 readable stream 这个可读流啊。

来看一下，我们这里就叫这个 stream，它呢这里是一个 await 啊，是个 promise 这里特别注意啊。

this 点 ctx get file stream，这个时候呢我们就拿到了对应的一个可读流。

假如您进去看一下啊，我们看一下它的定义啊，它是一个 file stream 这个类型的啊。

然后我们 go to type。

Definition. We can see that it is inherited from readable, so it is a readable stream, and on the readable stream, we have expanded some properties. These basic properties of the file, such as file name, file name, encoding, etc., etc., a series of properties. Well, after we get this stream, we can use the methods of the stream we learned in the last class to generate the corresponding file. First, we need to determine the format of the file. Where do we want to save it?

We want to save it in the uploads folder.

然后呢，我们给它生成一个随机的文件名，比如说叫叉叉叉。

然后呢，它的这个 e x t，也就是 extend name，应该保持不变。

还有呢，当然是就是 uploads x x x，然后呢后面加上这个 thumbnail 啊，跟上节课一样，然后是 e x t。

我们发现呢，我们自己要保存这文件夹呢，格式会稍微简单一些，我们不需要添加那么多的一系列按日期分类的文件夹。

好，那么现在呢，完成这个任务。

首先呢，我们来生成一个 U I D 啊，也就是生成这个随机的字符串。

我们这时候需要把这个对应的拿过来，那么自然是呃 Nano I D 啊，我们已经用过多次的 Nano I D。

Nano I D。

好，我们在这里生成一个六位的 I D 呢，就是 U I D 等于 Nano I D 六。

好，接下来呢，我们来生成要保存到哪里啊？

它的一个路径。

称之为 C 的 file path。

好，自然呢，我们要组合生成这样的一个结构。

这里我们还是使用 join。

一开始呢，拿到这个 config 上面的 base_dir，也就是我们的项目文件夹，它呢添加这个对应的 uploads，然后呢，我们要生成这个这么一个文件格式啊，那么是 U I D 加上我们这个文件名称的这个扩展名名称。

这里单独拿一个扩展名，我们可以使用 path 上面一个对应的 ext name。

大家可以看啊，这可以帮你拿到这个对应的扩展名儿。

好，那么这里呢，我们就是 ext name，然后把文件名称传进去。

文件名称刚才我们说了啊，在 stream 上面有一个特殊的属性，它叫这个 file name，可以拿到这个文件的名称。

好，这样呢我们就完成了对应的组合。

当然呢，我们给那个 thumbnail 的 path 呢也给它生成一个啊。

非常类似，我这里就不重新打一遍了啊，直接复制过来就好了。

唯一呢就是在这里多添加了一个字符串。

好，有了这两个文件这个位置以后呢，这时候我们需要这个有了可读流，我们需要可写流，把它写到这个对应的位置去。

所以呢，我们需要 create write stream 啊，我们在 file 这里进行一个拿取啊，fs，那么就是 create，大家可以看到啊，我们需要的是 write stream。

我们第一个称之为 target，然后 create write stream， save file path。

第二个呢是 target two啊，我们这是保存这个缩略图的一个位置， create write stream，应该是 save thumbnail path。

好，现在有了它俩以后呢，我们就可以进行对应的操作了。

我们可以看到呢。

我们之前学习的这个 stream，我们都使用了 pipe on 这样的写法啊。

我们这里呢，希望把它转换成一个 promise，因为我们整个应用呢大量使用了 promise，我们可以使用 async wait 啊这样的逻辑进行一个书写，我们更熟悉一些。

好，所以呢，我们来进行一个转换啊。

这里呢，我们当然是要运行两个 promise，一个呢是这个生成普通图片的一个这么一个 promise，第二个呢是生成缩略图的一个 promise 啊。

所以我们来先创建第一个啊。

我们称之为 save promise. 好，我们这里给它做一个转换啊。

New promise resolve reject. 这里应该 stream 从这个可读流，它到哪儿呢？

到一个可写流，那么自然是 target。

这应该是 target 一啊，不是 target 二。

然后呢，我们 on。

在 finish 的时候啊，我们在这里给它 resolve 掉，说明成功了。

然后在 on error 的时候啊，这时候调用 reject。

好，这样我们这个应该就是改装完毕了。

有了我们的第一个这么一个 promise，我们还需要第二个的这个流。

这个流中呢，我们需要对应的一个转换流，也就是使用 sharp 进行一个 resize。

当然，sharp 支持这样的写法，它也可以生成直接生成一个转换流，帮我们进行一个处理。

我们来看一下该怎么写。

我们这里写一个 transformer，生成一个对应的转换流。

上节课呢，我们也学了这个转换流它的一个力量啊。

那么它呢，可以从一个可读流拿到数据，把它转换成另外一个可读流，再导入到可写流当中去。

那么这里呢，我们直接调用 sharp，啊，我们这里不需要传输任何的一个参数，然后调用这个 resize 方法。

我们这里要要转换到三百去。

好，这样呢，我们就创建了一个转换流。

接下来呢，是我们第二个 promise，我们称之为 thumbnail promise。

new promise 跟刚才这个格式是一样的啊。

我们再写一遍吧，resolve、reject。

然后呢，唯一不一样的地方呢，就我们就要多一步啊，那么就是 stream。

可读流，那么首先呢，我们要 pipe 到一个转换流去，也就是我刚刚才创建的这个 transformer，然后呢再 pipe 到我们的这个可写流当中，也就是 target to。

好，这样我们这个就写完了啊。

on finish 和 on error，把它复制过来一下，这样就可以了。

好，那么现在呢，看来我们两个处理的 promise 呢都经过转换啊，写完了。

下一步呢，就是来我们来运行这个 promise。

我们现在有两个 promise，怎么运行呢？

我们当然要使用 promise all await promise all。

这里面呢是一个数组。

首先呢，我们运行 save promise，第一个这个对应的 promise。

第二呢是 thumbnail promise。

好，运行它俩以后呢，就应该生成两个对应的缩略图。

最后呢，给它返回一下就可以了。

ctx helper success。

ctx,然后response这里面要生成两个对应的URL。

我们这里呢，所以要做一个对应转换啊。

这样的replace，我给它呢把它单独的拿成一个方法吧，这样更简单一些。

我们这里称之为path to URL啊。

我们传入一个对应的path，然后返回一个对应的URL。

所以呢，这里呢我们应该是来拷贝一下吧，这个变量呢比较长。

好，那么大家可以看到，URL和thumbnail URL都已经生成完毕了。

最后呢，我们就来测试我们的应用呢是否好用，看看呢它能不能生成这么两张图。

好，那么来这里还是使用我们的这个接口啊，把这个接口换一下，router把file local upload换成这个upload by stream。

这时候呢，我点击send，希望呢能返回两个对应的URL。

好，大家可以看到呢，现在这两个U L就返回了啊。

我们使用其中的一个做一个测试，大家会看到呢，这张缩略图呢也就成功的生成了。

它是在uploads文件夹下加一个这个随机的字符串，后面呢是thumbnail，然后PNG呢是它原始的一个扩展名。

好，那么看起来呢，我们就完成了这么一个对应的任务。

功能一样啊，但是呢，和之前的做法呢已经是大相径庭了。

这次呢，我们是直接拿到上传文件的这么一个可读流，完成这个文件的特定位置的转换和写入。

好，通过这个例子，我相信大家可以更好的掌握一个这个 stream 它的用法。

好，那么我们这节课到这里，谢谢大家，再见。

