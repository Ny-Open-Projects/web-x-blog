# 11-24-egg-mongoose 源代码解读

上节课用自己发布的插件把 MongoDB 和 egg.js 结合了起来，这节课来分析官方 egg-mongoose 插件的源代码。地址和用法在仓库里都有，大家可以简单了解一下用法。先把源代码克隆下来，目前的版本是 3.3.1。

看它的文件结构。有几个非常熟悉的文件夹：app，里面有个 extend，是给 context 对象做扩展的，不讲，点开一看就发现很简单；config 文件夹很重要，是插件必须的，里面有默认配置文件；还有个没见过的 lib 文件夹，马上说；最重要的就是我们说过的 app.js 自定义入口文件。

看到 app.js 就知道各文件夹的作用了：假如 config 中有 mongoose 这样的配置，就进行调用。于是来到我认为最重要的文件 mongoose.js，几乎所有需要的 mongoose 逻辑都在里面。我挑重要的步骤讲，一些比如过滤、重命名之类的逻辑跳过，大家课下自己看。

这个文件本身是个函数，调用时把 app 传了进来。app 当然就是 application 那个最重要的、唯一的全局对象。首先它把 mongoose 的配置一一拿出来，具体配置在 config.default 里：url 是连接哪个数据库，还有 options、plugins 等等，大家自己看一下就好。

接下来有一句很奇怪的代码，叫 compatibility（兼容性）。它在这里做了一个格式转换：假如参数中没有 client 也没有 clients，但有 url 参数，就做一个转换。转换成什么格式呢？在原配置外面多套一层：加一个 client 作为 key，把配置都套在 client 里面。为什么要做这个格式转换？后面说明。再往下是可以略过的部分：导入 mongoose，设置 mongoose 全局的 promise 用什么；然后 load 一些 mongoose 的 plugin，如果你提供了 plugins 参数它会进行对应的加载。

接下来是重头戏，特别注意第 34 行：app.addSingleton('mongoose', createOneClient)。先不说 addSingleton 干什么，看 createOneClient 里面。它接受两个参数：config 是配置文件，app 是全局唯一的 app 对象。一开始把几个参数拿过来，中间有个 filterUrl 处理（对 URL 做处理，把里面的密码隐掉），assert 一下没有 url 就报错；还有两行是过滤、修 bug 的处理，fix 了一个 bug 并输出一个日志。然后是我们已经见过的函数：mongoose createConnection，使用 url 和 options 返回连接对象，连接数据库，这里就看到了我们之前插件写的端倪。db 是基于事件的，在不同事件情况下输出不同的日志：error、disconnect、connected、reconnected 各有输出。输出后有个 app.beforeStart，里面有 awaitFirst 等一系列回调，和多个实例相关，讲完后面的代码再说。最后返回 connection 对象。

所以这个函数做的事很简单：连接数据库并返回一个 connection 对象，看起来和我们的逻辑非常相似。现在复盘一下回到 addSingleton：它应该也是往 app 上添加一个对应的属性，属性值就是函数返回的对象。它和直接添加有什么区别？求助文档，《全局实例插件的最佳指南》这个章节回答了这个问题。许多插件的目的都是将已有的服务引入框架，它们需要在 app 上创建对应的实例，会遇到一些普遍性问题。第一个问题：一个应用中同时使用同一个服务的不同实例，比如要连接多个 MySQL 数据库，Mongo 也一样，可以连接多个 Mongo 数据库并返回多个实例。第二个问题：从其他服务获取配置后动态初始化连接，有多个实例时要拿到不同实例相对应的 connection。如果让插件各自实现，会出现各种奇怪的配置方法和初始化方法，所以框架提供了 addSingleton 方法来统一这一类服务的创建。注意使用这个方法时，配置文件中一定要有 client 或 clients 为 key，传给 creator 函数的 config 才会符合要求。

看到这里就解答了之前的疑问：为什么代码一开始要把 url 转换成 client 形式、把 client 作为 key 添加上去。这个函数是针对一个服务的不同实例服务的。举个例子：app.addSingleton('mongoose', createOneClient)，假如配置中只有一个 client，说明只需要创建一个实例。它会检查配置是这种形式，然后在 app 上添加一个属性，属性名就是第一个参数（app.mongoose），值是对应函数返回的实例。所以只有一个实例时，addSingleton 和上节课自己的实现是一样的。使用时通过 app.mongoose 拿到连接对象。第二种情况：配置中要连接多个 clients，配置文件里应该是 clients，并且 clients 有多个 key 代表连接不同的数据库，比如 db1、db2。这时再调用 addSingleton，它发现参数是 clients，就会循环里面的 key，添加多个实例并以 key 区分，相当于 app.mongoose.db1 等于对应创建的实例，db2 等于另一份配置创建的实例。使用时用 app.mongoose.get('db1') 拿第一个实例，get('db2') 拿第二个。简单来说，addSingleton 就是为快速添加多实例服务而生的。当然可以手动循环 clients 对象一一赋值、一一创建，最终效果一样，但用这个方法更规范。

了解 addSingleton 的作用后，beforeStart 的作用就不难理解了。首先明确 beforeStart 也是一个生命周期的阶段，但它是旧版写法。文档里"升级你的生命周期事件函数"说了，函数形式已经作废，仅为兼容保留：beforeStart 在应用开发中应写到 willReady，插件开发中应写到 didLoad。因为这是个写得比较久的库，还没来得及升级，这里相当于 didLoad 生命周期。didLoad 时先打印一行日志，然后调用 awaitFirst，这是一个特殊的第三方库。简单来说，这个库是等某个事件发生后再执行后面的逻辑：等 db 的 connected 事件发生后，再执行后面的逻辑。后面的逻辑打印一行日志，并添加了一个全局变量 count（在外层一开始等于 0），每次连接给它加一，通过这种方式输出是哪个实例启动成功了。这几行代码的作用就是在每个实例启动成功后添加一行带不同 index 的日志。

了解了这两点，继续在最外层入口往下看：addSingleton 结束后，把一些变量做重命名，最后 loadModel。loadModel 调用的是 loadModelToApp，看这个方法就非常熟悉了：和我们写的几乎一样，通过 loadToApp 把 model 加载到 app 对应的属性上。整个流程结束。

复盘一下它完成的三步工作：第一步拼接连接、添加对应的插件配置；第二步使用 addSingleton 创建一个或多个数据库实例，添加到 app 对应属性上；第三步使用 loadToApp 将 model 类添加到 app.model 属性上。

源代码解读到这里告一段落。它和我们的插件实现了非常相似的功能，只不过有更好的参数检查、更多的功能（比如添加 plugin）以及更好的实践。最大的不同是它使用 addSingleton，可以支持创建多实例。具体细节同学们有时间再看。课下希望大家安装官方插件，把我们的插件替换掉，因为人家功能更多、更好用，我这里就不演示了。源代码解读暂时到这里。
