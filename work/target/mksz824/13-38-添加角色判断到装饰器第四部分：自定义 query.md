# 13-38-添加角色判断到装饰器第四部分：自定义 query

上节课我们为 channel 这个特异性的存在改造了部分代码的分析，这节课把对应的逻辑添加到代码中，感受一下它能否正常工作。这部分内容主要是添加到函数传递的参数中，所以首先要把注释写得清楚一点。对于这种比较难以理解的函数，写注释是很有必要的。函数参数的注释可以做一个实用主义者，不要为了写而写。

先添加注释。使用 VS Code 的话，打一个斜杠加两个星号，它会自动生成对应的一系列参数和返回。第一个是 modelName，添加上：它应该是 model 的名称，可以是一个普通的字符串，也可以是一个对应的映射关系。第二个是 errorType，应该是返回的错误类型，来自于 global error types。第三个比较复杂，是特殊的配置选项：这个配置选项可以自定义 action 以及查询条件，详见上面 IOptions 里对应的注释，那里写得很清楚。最后确定一下返回：它应该 return 一个对应的 function。这里有个小问题，eslint 报自动生成的 @returns 格式有问题，给它改成 @return 就可以了。

开始改造代码。modelName 之前说了需要一个简单的改造，它应该是一个联合类型：除了 string，还有一个 ModelMapping。这样类型一变，里面会报一些错误，因为代码中期待的是 string。

第一步设置一个 defaultOptions。我们希望 defaultOptions 跟传入的 options 做一个混入，获得一系列的值。defaultSearchOptions 的 key 应该是对应的 id；value 的 type 应该是 params，也就是从 params 里面拿；valueKey 应该对应拿 id 这个参数。这样就完成了默认值。然后做混入：用传入的 options 跟 defaultSearchOptions 做混入。可以使用 lodash 的一个方法 assign，但要特别注意：默认的 assign 方法是 mutable 的，会更改传入的参数格式，options 会被改掉。所以这里要用 lodash/fp，fp 是 function programming，它是 immutable 的，不会更改任何传入的参数。大家特别注意这一点，使用 lodash/fp 就是因为不希望 options 被修改。

写法是 searchOptions = assign(defaultSearchOptions, options || {})，注意 lodash/fp 的参数顺序是从前往后的（前面放 defaultSearchOptions），后面用 options 来覆盖它，没有 options 就传一个空对象。这样就得到了混入以后的结果。混入后把需要的值取出来：从 searchOptions 中拿到 key 和 value，再从 value 中拿到 type 和 valueKey。这些都取出来以后，就可以做对应的替换了。

替换之前还要先把 modelName 进行赋值转换。然后构建一个 query。query 的格式上节课都看过，有一些例子，我们要根据这些值构建出对应的对象。第一步判断 source，也就是数据的来源在哪里，通过 type 来界定 source 等于什么。写一个三元表达式：type 等于 params 的时候，使用 ctx.params；否则使用 ctx.request.body。有了 source 就可以构建 query：query 应该等于一个对象，key 是 searchOptions.key，value 是 source[valueKey]。对比一下现在构建的 query 和我们分析的是否一致，应该是一致的。

拿到 query 后，最后还需要把 modelName 转换一下，因为现在 modelName 是字符串类型。这里也需要一个三元表达式做判断，分两部分。mongooseModelName：typeof modelName === 'string' 的话，说明传入的是 string，直接使用 modelName 就可以；Type Guard 之后类型范围会缩小，现在的 modelName 就是我们定义的 ModelMapping，可以直接拿到上面的 mongoose。照猫画虎，把 caslModelName 也复制过来拿 casl。通过这样就把 modelName 的联合类型分成了两个具体的类型。

下一步做对应的替换。查询处把 mongooseModelName 放进去，也就是在 mongoose 上进行操作；caslModelName 也要替换，relevantRuleFor 里、以及 ability.can 的判断处都要替换。最后把查询用的 query 替换成我们构建的 query。再检查一下，所有位置都被替换完毕，这部分的逻辑就写完了。

现在添加测试 channel 的工作情况，把对应的 permission 装饰器加上。第一个是 createChannel，它比较奇特：拿 query 的值是从 body 中拿的，对应的叫 workId，查询条件是 id 等于 workId。复制一下 checkPermission，特别注意里面的几个参数：modelName 传一个映射对象，casl 是 channel，mongoose 是 work；value 的 type 是 body；valueKey 等于 workId，对应上了，没问题。

第二个添加的是 getWorkChannels。GET 就比较简单了，值是从 params 上拿的，查询条件也是默认的，直接添加就可以，只不过第一个参数改一下。然后是 updateChannel，这里不一样的是查询条件不一样，它要查的是 channels.id，而不是固定的 id，所以 key 要写成 channels.id。最后 deleteChannel 跟 update 一样，添加一下就可以了。保存，修改就结束了。

测试好不好用。我这里测试 GET 和 PATCH 两个请求，其他方法同学们可以自己去测试，看看代码逻辑有没有问题。首先来到 getWorkChannels，10 是对应用户的 channel，点击 send 应该返回对应的结果。可以看到 count 为 2，两个 channel 都返回了。再测试不属于它的 channel 29，提示没有权限完成操作，说明没问题。

接下来测试 update。第一个测试属于它自己的频道，拿到对应的 id 传进去，给它一个更新，name 改成微信Good，点击 send，更新成功，说明权限通过了。还要测试数据越界的情况，也就是给它添加一个 workId，设置为 20，点击 send，提示没有权限完成操作，因为这个 workId 不在它允许修改的范围之内。回看 rules，它允许修改的只有 name，所以这里会报错。最后测试一个完全不属于它的频道，我直接复制一个别人创建的频道的 id，把 name 更新删掉，点击 send，也返回没有权限完成操作，说明我们的开发工作都完成了。

这节课完成了关于角色的所有开发工作，通过一系列个性化的配置满足了目前的权限需求。同学们可以发挥主观能动性，丰富更多的角色进行测试，比如加一个有特殊权限的 VIP 用户。我认为这部分内容很有实用性，工作中可能会遇到，请大家自己展开想象。而且在工作中你不妨把 CASL 拿出来，给同事和领导 show 一下，看看它是否好用，是否会让你在工作中大放异彩。
