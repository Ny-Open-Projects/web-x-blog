# 13-27-完成 webpack 结合上传文件到 OSS 的功能

上节课我们完成了上传工作，但还没有把 webpack 和上传结合起来，这节课来完成任务。先分析目标：要针对两种环境做不同的配置。

本地开发环境跟原来一样：先运行 webpack build，public 文件夹中生成 main.js、main.css 等静态文件，模板文件 page.html 被拷贝到 views 文件夹下，page.html 引用的是 /public 下的这些文件。而 production 环境在上节课上传工作的基础上整体梳理一遍：一开始还是 webpack build，前面都一样，在 public 和 views 中生成对应的文件，然后多一步 upload，把静态文件上传到 OSS。区别在于 page.html 中引用的静态文件地址不再是 /public，而是 OSS 的地址，也就是上节课生成的 OSS 上 h5ss 那个地址。核心就是根据环境是 development 还是 production，构建不同的静态文件地址。

所以第一要务是怎样在 webpack 的配置文件 webpack.config.js 中获得不同的环境变量。求助文档的环境变量章节：要消除 webpack.config.js 在不同环境之间的差异，就需要环境变量。配置方式是命令行的 --env 参数，允许传入任意数量的环境变量，比如 `--env production` 或者 `--env goal=local`，后者是把一个叫 goal 的环境变量的值设为 local。这里有个小 tip：如果设置了变量却没有赋值，比如 `--env production`，那么默认会把 env.production 设置为 true。

要在脚本中获得环境变量，配置文件必须做一处修改。通常我们的 module.exports 指向一个对象，现在要使用环境变量，必须把它转换成一个函数，函数有一个特殊的参数 env，就是要拿到的环境变量。这个转换主要是格式上的调整，我直接改好了：现在 env 就是传入的环境变量值。做个测试，打印一下 env.production。

接着区别对待 publicPath，根据 env.production 是否为 true 赋不同的值，直接写一个三元表达式：env.production 存在时返回 OSS 地址，否则返回原来的 /public。另外，如果你想把这个 OSS 地址保存到环境变量也是完全可以的。因为上传文件的配置里我们并没有单独把它设置成环境变量，如果在多处使用，把它设置到环境变量是一个很好的实践，大家可以课下自己做，我这里就不改了。

配置修改完后，脚本也要改。先复习一下要完成的流程。这里会多出几个命令：build:template 我们分成两条。第一条叫 build:template:development，生成开发环境的模板文件，不需要注入任何环境变量，跟原来完全一致。第二条叫 build:template:production，这里要多做一步，把 env 插进去，也就是用刚才的 `--env production`。而且 production 除了生成 webpack 产物，还要运行 upload，上传完成才算有效果，所以在后面加一个 `&& npm run upload`。

现在两个脚本都完成了：development 跟原来一样，production 会插入环境变量并且运行上传脚本。运行一下看整个流程是否正确：`npm run build:template:production`。可以看到 env 是 true，打包完成后输出了两条上传成功和对应的地址。刷新最终页面，可以看到两个文件已经成功上传，并且可以被成功引用，页面中生成的引用变成了 OSS 地址。

这节课的工作就完成了：通过甄别不同的环境，生成不同的页面并上传到 OSS，然后在模板中生成不同的静态文件地址。当然还有一个问题，就是运行这些命令的时机。这两个命令都是一次性生成文件的，可能需要在 npm run dev 或 npm run start 之前执行，一个对应开发环境一个对应生产环境。而且生产环境可能还需要更多准备工作，因为还要单独运行编译 ts 到 js 的过程，也就是之前说过的要手动运行的 tsc 命令。不过在这里我们不会把它们添加到 start 或者 dev 的前面，这些准备工作留到后面部署的章节统一讨论。
