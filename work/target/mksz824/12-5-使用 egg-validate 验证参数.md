# 12-5-使用 egg-validate 验证参数

TS 准备做好之后，来完成下一个任务。现在创建数据的功能还很简陋，缺少最基本的数据验证：不管什么数据都来者不拒。而我们希望 username 是 email 类型、password 至少八位。数据验证是最基本的功能，egg 提供了官方插件来完成，插件名是 egg-validate。自行安装后在 plugin 里启用：名称 validate，enable 设为 true，package 是 egg-validate。配置不需要任何修改，用默认的即可。

## 底层库 Parameter

Validate 底层依赖一个通用的验证库，叫 Parameter。它的贡献者大部分就是 egg.js 的作者们。规则可以通过两种格式添加：简单模式和复杂模式，都是 key-value 的形式，前面是要验证的参数名，后面是验证规则。简单模式是复杂模式的快捷方式，所以用复杂模式讲解。

规则中的字段挑几个重要的说：

- `required`：设为 false 时，这个属性可以是 null 或 undefined，默认是 true；
- `type`：最重要的值，代表要验证的数据类型，库内置了大量预写好的类型，比如 int（整数）、integer（int 的别名）、number、date、day、time、id、boolean、string 等。我们需要的 email 和 password 都有固定 type，正则都替我们写好了；
- `convertType`：从 body 获取的数据大部分是 string 类型，即使你传的是数字。它会针对不同类型做自动转换，比如规则设为 int 就把值转成整数。

另外，某些固定 type 还可以附加条件。比如 password 类型的规则可以设置 max 和 min，限定密码的最长、最短长度。至于简写格式，它像一个快捷方式，用一个字符串指代一行特殊规则，对应关系文档里列了很多。这次我们需要两条规则：email 和 password。但密码要求至少八位，默认是六位，所以需要一个简单规则加一个复杂规则。

## 定义规则并验证

数据验证和组装应该在 controller 里完成。遗憾的是 Parameter 没有提供 TS 定义，很不爽，只能手写，或者按照它的文档创建自己的自定义类型。创建规则 userCreateRules：第一个参数 username，希望它是 email 类型，直接用简写；第二个参数 password 用复杂模式，type 是 password，min 设为 8，至少八位。

验证有两种方式。第一种非常简单：在 create 之前调用 `ctx.validate(userCreateRules)`，validate 是插件在 ctx 上添加的方法，内部运行时会自动获取 request body。但测试一下就能发现问题：用错误数据发送请求，它会直接抛出 422 错误并结束整个响应。我们之前文档分析时说过需要自定义错误格式，所以想要自定义格式而不是默认的 422 返回，就得用 try/catch 的写法，不太友好。

## 第二种方式：app.validator.validate + helper.error

所以选择第二种方式：在 app 上的 validator 里调用 validate 方法。写法是 `const errors = app.validator.validate(userCreateRules, ctx.request.body)`，两个参数分别是 rules 和数据（自然是 ctx.request.body）。错误不会直接抛出中断代码，而是作为返回值拿到。

用 `ctx.logger.warn(errors)` 打印观察一下：有错时 errors 是一个错误数组，没有时是 undefined，可以直接拿来判断。有错时进行对应的返回。之前有成功的返回（helper.success），现在要创建一个失败的返回，区别是要有 errorNumber，data 可能没有，message 是错误信息。

先建一个和 success 类似的 interface，叫 ErrorResponseType：传入 ctx（Context 类型），加上 errorNumber（number 类型）和 message（string 类型，可选，可能没有信息）。

然后在 helper 上新添加一个方法，自然就叫返回 error 的信息，参数用刚才定义的 ErrorResponseType。从里面解构出 ctx、message 和 errorNumber，最后返回：`ctx.body` 只需要返回 errorNumber 和 message 两项，message 有就用它，没有就给一个默认的"请求错误"。最后要把 status 设一下，和上面一样等于 200。

这里特别注意：不要直接调用 `ctx.helper.error`，因为 ctx.body 是渐进式的，不是调用后就直接结束请求。所以前面要加一个 return，让它提前返回，否则代码会继续执行下去。error 的入参里，errorNumber 先选一个编号用于验证，之后会详细讲解错误码规则；message 也先写一个"验证错误"。

## 测试

用错误数据测试，直接点击 Send。返回的是"验证错误"，是我们想要的格式。打印出来的错误数组有两项，因为两个条件都没满足：第一条是 should be an email，格式不是 email；第二条是 length should be bigger than eight，密码没有达到八位。

现在修正数据：把 username 改成规范的邮箱格式再 Send，错误只剩一条，提示应该大于八位；把密码从六位改成九位再 Send，创建成功了。至此用 egg-validate 完成了验证功能。

当然，现在输出的信息还有点问题，因为都是写死的。下节课希望把错误信息规范化，根据 errors 里的具体内容来输出。
