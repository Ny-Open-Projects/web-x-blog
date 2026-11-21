# 13-37-添加角色判断到装饰器第三部分：自定义 action

上节课已经完成了权限验证的基本任务，这节课继续完善功能，对付规则定义中的特殊情况。第一个特殊情况是：我们在 rules 中只添加了四个 action（read、update、create、delete），对应不同实体的四种操作，但现在有些实体的 action 比较特殊。

work 中有一个对应的操作，翻到 rules 最下面，它叫 publish。它其实是一个 update 操作，但课程更新之前，旧版的 URL 设计中，另外一位老师把它单独拿出来做成了一个操作。这种方式我认为有些不妥，完全可以使用一个对应的 patch 或者 update 来代替。但既然它已经存在，为了兼容前端的代码，同时扩充功能，我们需要对它进行自定义，也就是这个 publish。

首先在 rules 中添加对应的操作。复制一份 update 的规则，给它起新名称，这个 action 就叫 publish。它是作用在作品上面的，并且一个人只能 publish 自己的作品：can('publish', 'work', {...}, { user: user._id })。

添加完毕后，我们需要一个自定义的参数来操作它。因为现在对应的 map 只对那四个 HTTP 方法做了对应，里面并没有 publish，想获得 publish 就要自定义。想一想，可以给装饰器添加一个 options 参数。先确定它的类型，创建一个 interface 叫 IOptions，里面有一项称为 action（自定义 action）。有了这个 action，就直接使用参数中的 action，不再使用 method mapping，这样就能完成工作。action 是可选的，string 类型。

定义完毕后添加参数。原来有一个 userKey 参数，现在已经没用了，替换成 options，可选，类型是 IOptions。这时发现两个名称重复了（外层变量和 lodash 的 fields options），做一个小的重命名：既然是 fields 相关的配置，把里面那个改称为 fieldOptions，下面的引用也相应修改，现在没问题了。

然后在获取 action 的地方根据这个参数来定义。现在 action 是直接从 mapping 取的，我们用三元表达式来做自定义：假如 options 存在，并且 options.action 也存在（它俩都是可选的），取 options.action，而不是使用 map 关系。修改完毕后，就可以从 rules 中获取对应的操作并进行查询了。

publish 装饰器需要添加第三个参数，因为要自定义 action 名称，action 定义为 publish。修改完毕，来 publish 一个作品看看是否好用。先登录（还是这个用户），拿到 token，到 publish 接口做测试，把 header 添加上。29 不是他的作品，点击 send，返回没有权限完成操作，说明添加得没问题：查询成功，并且取到了 publish 这个 action。再看 30，点击 send，30 是他自己的作品，发布后成功返回了对应的 URL，任务完成。

这个任务看起来很简单。完成之后，我们来对付课程中最有特异性的一个实体：channel。为什么说它有特异性？从代码上一看究竟。这节课先分析要实现它需要做怎样的修改、添加怎样的参数，下节课再完成对应的代码。

第一个问题：虽然 rules 里对应的名称叫 channel，但看代码会发现，它其实都是在 work 这个 collection 中查找数据，因为 channels 只是 work 下面的一个数组。所以查找记录时，需要在 mongoose 的 work 实体中查找，但判断权限时，对应的却是 channel 这个 CASL subject。要解决第一个问题，需要想一个 mapping 关系，并且能传递到 modelName 中去。也就是说 modelName 可以是一个 string：当是 string 的时候直接取；假如是特殊的对应关系（一个 object），就对它做特殊判断。

先确定这个对应关系长什么样。再创建一个 interface 叫 ModelMapping，里面有两个属性：mongoose 是 string，是 mongoose collection 的名称；casl 也是 string，是对应的 CASL subject 的名称。这样两者就产生了对应关系，能解决第一个问题。

第二个问题比第一个复杂一些，还是和查询对应记录相关。用注释的方法写一下。现在查询的 query 很简单：findOne 的 key 是 id，来自 ctx.params。用注释写出来，query 现在应该是 `{ id: ctx.params.id }`。

但假如你去查 channels，因为要先查询获得对应的 work 信息，判断它是不是属于这个用户的，所以这里面肯定有一步查询，而且查询是有条件的。之前我们说过它的查询条件是什么？来到 works 的 controller 可以看到，query 的 key 不是 id，而是一个特殊的格式：`{ 'channels.id': ... }`，后面还是对应的参数。所以这里和普通情况不一样。

还有一个情况：创建 channel 的时候，回到代码中看 createChannel，它也要进行对应的查询。前面是 id 没错，但后面是 workId，workId 来自 ctx.request.body，所以 value 很奇特。写成注释的话，应该是一个这样的对象：前面一样，后面是 `{ 'channels.id': ctx.request.body.workId }`，完全不一样。所以我们的任务是完全满足查询数据的可定制化，需要特殊的参数，把 key 和 value 两部分都做成完全可定制。

自然想到在 IOptions 中添加对应的参数。第一个是 key 可定制，默认为 id，也可以进行定制，string 类型，对应的就是 query 里那个 key。value 也应该可定制，这里要确定一个对象，里面应该有两项。第一项要记录 value 的数据来源，加注释说明：它有两个数据来源，第一个来自 params（parameters），第二个来自 request body，所以添加一个 type，暂时是一个联合类型：'params' 或 'body'。除了来源，还要确定它的键值。看刚才的属性可以发现，键也是可定制的，等于 id 或者 workId，所以还需要一个 valueKey，string 类型。补上对应的注释，这样大家就会看得很清楚，知道 type 和 valueKey 究竟是干什么的。

这样我们就分析好了参数应该有的结构。当然有同学会觉得这个函数变得越来越臃肿，为了适配做了太多修改。如果愿意，你完全可以创建一个新的装饰器来专门完成这个特殊的匹配，把这些条件都不加，而是把逻辑变化一下，而不是采用在原函数上添加参数适配更多特性的方式。

这节课就先讲到这里。我们分析出了为了适配这些特性需要的一系列参数，下节课看看怎样把这些参数对应地添加到函数的实现中。
