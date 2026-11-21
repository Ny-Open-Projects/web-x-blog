# 12-8-将 bcrypt 添加到应用并完成密码加密和登录解密

上节课简单介绍了不同的密码加密机制，并最终选定了 bcrypt。这节课就在 egg.js 应用中把它添加进来并实践。

## 安装插件与补齐类型定义

首先要安装 egg-bcrypt 模块。遗憾的是这个模块写得很早，没有类型定义文件，但库本身非常简单，其实在 context 上只提供了两个方法：加密方法 generateHash，以及检查密码是否匹配哈希的 compare。所以可以自己写定义文件。当然也可以完全不用 egg 插件，直接使用它内部采用的 bcrypt.js，用的时候引入即可，也完全没问题。这里还是使用 egg-bcrypt 插件。

安装后启用插件：plugin 里 enable 一项 bcrypt，package 写 egg-bcrypt。然后补类型定义，扩展都在 context 上：`interface Context` 里添加 generateHash（参数 plainText，返回 `Promise<string>`，文档描述是 hash password plain text，返回 promise）和 compare（第一个参数是明文 plainText string，第二个是加密后要检查的 string，返回 `Promise<boolean>`）。

此外还要扩展一个 config，只有一行：saltRounds，即经过多少轮加盐，上节课讲过，默认是 10。在 `IAppConfig` 上扩展 `saltRounds: number` 即可。config 里可以设 `config.bcrypt.saltRounds = 10`，默认也是 10，不设置也可以。

## 创建用户时加密

功能上，首先要在创建用户时完成加密，也就是把 password 加密。generateHash 返回的是 Promise，注意要 await：`const hash = await ctx.app.bcrypt.generateHash(password)`。然后把这个加密后的字符串保存到 password 字段上，加密过程就完成了。

## 登录逻辑：loginByEmail

除了加密还有比对，用在登录的时候。所以再添加一个 controller 方法 loginByEmail。暂时不考虑数据持久化和用户状态记录，只看能否拿到对应的用户数据。

第一步从 this 上解构出 ctx、service 和 app，然后检查用户的输入。因为 create 和 login 两个流程都要用用户输入校验，把它提炼成独立方法 `validateUserInput`，放在 controller 上，把校验那几行复制过来，最后 return error。至于 createByEmail 里的替换，课下自己完成。

login 里调用：`const error = this.validateUserInput()`，有 error 就返回对应错误。特别注意这里要加 return 提前返回，因为 ctx.body 不是设置后就结束请求，会继续往下执行。调用 `ctx.helper.error(ctx, errorType, error)`。

顺便把错误类型统一一下：不管是 login 还是 create，输入验证失败都是"用户"这个层面的错误，所以把 createUserValidateFail 改名，去掉 create user 前缀，message 写成"输入信息验证错误"，所有验证失误都用这个类型，再做对应替换，error 要传进去。

第二步，开始匹配密码之前要先判断用户是否存在。从 `ctx.request.body` 上拿出 username 和 password 两个值，用 service 里已有的 findByName 查询：`const user = await service.user.findByName(username)`。user 的类型可能是 null 或者 UserProps 与 Document 的交叉类型，所以先判断 user 是否存在。不存在就 return 错误，这里创建一条新的错误信息 loginCheckFailInfo，代号 101003。注意，用户不存在和密码错误统一写到这一条信息里，不分开。因为给用户的信息最好不要那么精确，太精确反而有安全问题，统称为"用户不存在或密码错误"。写好 errorType 后 return `ctx.helper.error(ctx, 'loginCheckFailInfo')`。

第三步匹配密码。返回值命名为 verifyPwd：`const verifyPwd = await ctx.app.bcrypt.compare(password, user.password)`，第一个参数是输入的未加密明文 password，第二个是数据库里 user 对应的加密值。verifyPwd 是布尔类型，判断验证是否成功：不成功就返回刚才创建的 loginCheckFailInfo；成功就返回 `ctx.helper.success(ctx, user, '登录成功')`，把 user 信息返回出去。

## Router 与测试

整个登录逻辑添加到了 controller 中；service 里改动很少，只需要在创建时用 generateHash 把 password 生成 bcrypt 加密后的值。最后在 router 添加接口：POST `/api/users/login`，对应 controller.user.loginByEmail。

开始测试。第一步测验证好不好用：把密码改短一点发送，返回"输入信息验证错误"，提示密码长度不够，说明验证生效。补齐八位后用一个还没创建的用户登录，返回"用户不存在或密码错误"，说明用户还没创建。于是先在 users/create 创建用户，八位密码八个 1，viking12@...。创建成功后可以看到 password 变成一长串，上节课解释过它的分段结构：算法标识、saltRounds、salt、最终的哈希，说明密码加密成功了。

再用刚创建的用户登录。注意测试时密码多输了一位（九位），改回八个 1，点击 Send，密码匹配成功，返回了正确的数据和"登录成功"。说明明文和哈希值的 compare 比对工作正常。

## 遗留问题

这节课学习了 bcrypt 的加密和解密过程，同时添加了 login 逻辑，可以拿到对应的用户状态。但现在有个问题：返回的数据中直接把 password 也泄露出来了，这是非常不好的做法。返回的数据应该有选择地删除一些字段，而不是把敏感信息都暴露在外。下节课学习 MongoDB 提供的非常简单的 toJSON 方法来完成这个任务。
