# 13-25-拷贝和清理 webpack 生成的文件

上节课我们已经成功用 webpack 把 JS、CSS 和 HTML 打包生成到了 public 文件夹。但我们对应的模板文件需要放在 views 文件夹下，所以现在的任务是完成一个简单的拷贝：把 public 中的 page.html 拷贝到 views 中做覆盖。

有同学可能会说，用一条 cp 命令不就行了。考虑到后面文件操作可能会更多，这里介绍一个通用的解决方案，插件叫 filemanager-webpack-plugin。注意它的名称里有 File Manager，说明它能做很多跟文件相关的任务。

在完成拷贝之前，先要解决一个特殊问题。打开 .gitignore，里面有一条默认生成的规则 `*.js`。有这条规则后，项目中所有的 js 文件都会被忽略，但我们需要把 webpack 文件夹中的一系列 js 文件添加到版本管理（repository）中，所以要把这条规则删掉。删掉后会不会影响其他任务呢？比如 app 中 ts 编译生成的 js 文件是和源码放在同一文件夹下的，这些文件我们需要忽略。注意 .gitignore 里还有一条配套规则可以完成这个忽略，保证 app 中的所有 js 文件仍然被排除。所以删除那条规则没有问题。

解决这个问题后言归正传，安装 filemanager-webpack-plugin（大家自己安装），然后把插件导入配置文件。既然要拷贝，就需要一个拷贝的目标地址。新建一个变量 templateFileDestination，用 path.resolve 指向 views 文件夹。有了它以后，在 plugins 中多添加一个插件，因为它是对整体转换的处理：`new FileManagerPlugin`。

它是基于事件的，所以配置里有一个 events 选项，有 onStart 和 onEnd 两个阶段。我们自然是在编译完成以后处理，也就是 onEnd。操作用 copy，它的操作非常丰富（move、delete、mkdir、archive 等），我们只需要简单的复制。copy 的规则用数组分类，添加一条规则：第一个参数 source 表示从哪里拷贝，用 path.join 拼接 buildFileDestination（也就是 public 文件夹）和 page.html；目标参数 destination 用 path.join 拼接 templateFileDestination 和 page.html。

插件添加完毕，测试一下是否好用。运行 npm run build:template，没有报错。到 views 文件夹里验证，page.html 已经被修改，里面的链接变成了指向 public 中的一系列地址，说明拷贝成功。

最后到页面上验证。刷新第十个作品页面，样式已经添加上了，JS 里的 console 输出也显示出来了。检查元素可以看到，p 标签上的 element style 里有 l-text-component 对应的 white-space: pre-wrap，之前我们说过这是在单独的 CSS 文件中加载的，现在已经生效，任务完成。

最后还要做一些善后的清理工作。每次打包都会在 public 中生成新的文件，文件名带哈希，每次生成都不同，旧的文件就是没用的了，越积越多，需要对旧文件做处理。这时候需要一个新插件：clean-webpack-plugin。顾名思义，它完成清理工作。文档里写道：默认情况下，这个插件会移除 webpack 的 output.path 目录中的所有文件，然后再重新生成，这正是我们想要的。安装后（我这里已经装好）把它导入配置。特别注意它不是一个默认导出，外面包裹了一层对象 `{ CleanWebpackPlugin }`。使用它不需要添加任何参数，直接调用，走默认配置即可。

为了验证效果，我们稍微修改一下 index.js，比如把 console 输出改成 hello cat，然后重新 build。修改前 public 里有几个 9218 开头的旧文件，重新 build 后只剩下 88d6d 开头的新文件，9218 已经被删除，说明清理生效了。再看 page.html 是否引用了正确的地址，确实是新的 88d6d，页面上验证也没有问题。

到这里整个 SSR 需求看起来差不多完成了：静态页面可以根据编辑器创建的内容在后端完美展示。不过既然课程的目标是深入浅出，下节课我们就再深入一步，看看这个过程中还有没有可以进一步优化的地方。
