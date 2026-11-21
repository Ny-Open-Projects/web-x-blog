---
disableNunjucks: true
title: 11-22 将 models 自动加载到 app 对象
date: 2026-11-17 10:12:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课完成了 mongoose 添加到 egg.js，但还有不尽如人意的地方：所有 model 都定义在 service 上，这是很不 egg 的做法。egg 中全局对象 app 和 ctx 是两个集大成的元素，大多数特性都挂载在这两个变量上。我们也希望把 model 放到特定文件夹下（比如 model 文件夹）定义，然后在 app 上挂载一个属性，通过 this.app.model.User 这种方式访问对应的 model 进行操作。这节课就学怎么完成这个任务。

首先学一个新概念：加载器 loader。loader 是 egg 加载不同模块的核心。egg 按功能差异把不同代码放到不同文件夹管理，比如 controller、middleware、model、extend、service 等等，这些文件一般是类、对象或函数，在整个应用启动时需要被实例化、被调用，最后很多作为 app 的属性在 router 中完成对应功能。这个功能是 egg 通过启动过程中对不同文件进行加载完成的。

文档里给出了文件加载顺序，简单理解一下就好：第一步加载 plugin，然后加载 config，再加载 extend、自定义初始化、service、middleware、controller，最后到 router。有了这个，再理解 app.ts 里的生命周期就好懂了：configDidLoad 就是加载 config 完毕的阶段。我们不会深究，了解这个过程就好。

那么针对某一个文件，加载过程是怎样的？文件里有一系列内容，function、class 怎样被挂载到特定对象上？这是通过底层的 loader API 完成的。loader 提供了一些底层 API，在扩展时可以简化代码，有 loadFile、loadToApp、loadToContext 等函数，都完成刚才说的加载过程。

其中 loadToApp 吸引了我的眼球。它有三个参数：第一个 directory，文件夹路径，从这些文件夹加载文件；第二个 property，要注入到 app 上的属性名称。从 controller 的加载过程就能看到：第一个参数是 directory，第二个是 controller，也就是加载到 controller 属性上；第三个是 loader options，提供一系列参数。文档里的文件加载规则写得很清楚：假如文件夹下有个 userInfo.js，加载完毕后会自动转化成 userInfo 这样的属性，下划线命名会转成驼峰形式；也支持连字符，user-info 也会转成 userInfo。options 里有个 caseStyle，可以强制大小写。例子和我们说的很相似：app/model/user.js 会被转到 app.model.User，指定 caseStyle 选项后转成首字母大写，因为 model 用大写开头的名称更符合语义。

大体了解了 loadToApp 的做法，照猫画虎完成我们的功能。第一步在 app.ts 中调用 loadToApp，把特定文件夹的内容加载进来。写在哪都行，先拿到文件夹路径：用 path 的 join 方法组合两个路径，const dir = join(this.app.baseDir, 'app/model')，baseDir 还记得吧，是应用的基本路径，我们希望把所有 model 放在 app 下的 model 文件夹。有了路径就调用 this.app.loader.loadToApp()，编辑器有补全：第一个参数传 dir；第二个是想注入的变量，model；第三个是 options，希望首字母转换成大写，caseStyle 写 'upper'。

加载完成后效果是什么样？假如一个文件路径是 app/model/user.ts，它会被加载到 app 上的 model 属性下，按文件名转换成大写的 User，通过 app.model.User 就拿到了这个 model。

第二步创建对应的 model。我已在 model 文件夹下新建了 User.ts。里面应该创建什么类型的内容并返回呢？之前写的时候都知道需要拿到 app 全局对象，因为要用 app.mongoose 这个连接实例，所以这里要自定义一个函数，叫 initUserModel。注意 loadToApp 的机制：假如文件是一个函数，它会自动执行这个函数，并在函数中注入一个 app 参数（Application 类型），然后把执行返回的结果和属性对应，也就是 app.model.User 等于函数执行的结果。把 Application 导进来给 app 标注类型，函数体就是之前写的创建 schema 和 model 的代码，和之前 service 里写的完全一致，直接拷贝过来，最后 export default initUserModel。整个过程就是：第一步定义加载过程，第二步把每个 model 一一定义，egg 会依次加载 dir 下的 model 并注入到 app 的属性上。

完成后就可以直接在应用中使用了。首先别忘了定义类型，不然写的时候直接报错。来到 index.d.ts：这个类型应该是 mongoose 返回的 model 类型，而属性名称不确定，所以添加一个 indexer type。添加 type MongooseModels，key 是 string，返回一个 model（它需要泛型，暂时写 any）。然后把 model 属性添加到 Application 上，类型为 MongooseModels，添加完毕。

启动应用 npm run dev，成功后就可以使用了。service 里不再需要 getPersonModel，直接从 this.app.model 上取：因为转换成了大写，写 User，然后 find 进行查询，那个私有方法也可以删掉了。刷新页面，还是能返回对应的 persons，service 改造成功。大家可以把变量打出来看看是不是想要的内容。

通过这个改进，从 app 上的变量就能访问不同的 model 属性，并完成一系列 query 操作。同时关键是了解了 egg 文件加载的机制和简单原理。
