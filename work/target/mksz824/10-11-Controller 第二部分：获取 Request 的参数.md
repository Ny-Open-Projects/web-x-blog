# 10-11-Controller 第二部分：获取 Request 的参数

上节课简单介绍了 controller 完成 HTTP 响应。响应比较简单，而 HTTP 的另外一部分 request 要复杂一些，因为 request 经常带着一部分用户的信息和请求数据，我们可以根据这些信息再做进一步的处理。

先看一个典型的 HTTP 请求包含哪些部分。第一行是请求方法 POST、URL 地址和 HTTP 版本。特别注意问号后面添加的 query，`name=Viking` 这样的部分。接下来几行是 headers，可以看到有 host 和 content-type，当然 headers 会有非常多，比如 cookie 等等。之后是空行，空行后面就是发送的请求 body：当请求是 POST、PUT、DELETE 等方法时可以带上请求体，服务器端会根据 content-type 来解析这个请求体。

我们的任务是获取用户输入的信息，分两部分：第一部分在 URL 上，第二部分在 body 上。

先说 URL 上的信息，又可以分为两部分。第一部分是问号后面的 query string，经常用来传递 URL 中的一些条件，在 HTTP 请求中会经常使用。从哪里取得？照猫画虎：有 ctx.response 自然有对应的 ctx.request，request 上面有非常多的属性，和 response 一样，想了解的可以去看文档。这里只需要 query，拿到 query 之后直接把 body 等于这个 query，保存看结果。请求时添加两个 query：`name=Viking&color=blue`，返回就是 name Viking color blue。当然 query 也有简称，可以直接写 `ctx.query`，更快捷地获取参数，和 response 之前的别名一个意思，想获得全部别名可以去文档查看。

第二部分获取参数的方法叫 params。这种方式需要在 router 中进行特殊的绑定，在 Vue Router 中非常常见，我们也用过。做法是在想绑定参数的位置先添加一个冒号，后面是参数的名称。比如添加一个叫 id 的变量，之后在 controller 当中使用 `ctx.params` 拿到这个同名变量。我们简单添加一个 response，把两部分都放进去：第一项看 query 是什么，第二项看 id 是什么，让 body 等于这个 response。访问 test 后面带上 id 为 2，回车后 id 也能成功拿到是 2。这里添加多少个参数都可以，只要保持同名就没问题。

特别注意：params 不是 request 上面的属性，我们拿不到 `ctx.request.params`。大家可能以为它是快捷方式，其实不是。request 上面并没有 params 这个参数，因为 params 不是 Koa 原生的内容，而是 Egg.js 通过 router 新添加的一系列属性，所以它并不在 request 上面，这一点要特别注意。

现在还剩另外一部分重要的数据，就是使用 POST、PATCH、PUT 传递过来的 body。可以使用 request 上面的 body 直接获取。body 其实是经过 Egg.js 内部特殊处理的属性，它使用一个内部的插件叫 body parser，会根据 header 当中的 content-type 对 body 进行特殊处理：当 content-type 是常见的 application/json 等一系列格式时，会按 JSON 格式对请求的 body 进行解析，并限制一个最大的大小，解析返回的是一个 JavaScript object；当请求的 content-type 是 form 形式时（除了 JSON，最常用的发送数据格式就是 form），它会按照 form 的格式对 body 进行解析，返回的也是 object。

现在来测试 POST 请求。首先在 router 当中添加一条路由，复制原来的配置，除了 get 再添加一个对应的 post，保存。测试 POST 不能用浏览器直接输入 URL 的方式，那样发送的是 GET 请求，可以用一个命令行工具 curl 来发送请求，它是在命令行中发送请求非常方便的工具，但参数稍微有点长：`-X` 指定 method 说明发送 POST 请求，后面是 URL（发送到 /test/2），`--data` 代表要发送的数据，比如 name=Viking、hobby=soccer 这样一个 JSON，还要添加 header：`-H 'content-type:application/json'`。

回车之后会看到一串非常长、令人莫名其妙的错误。这是因为 Egg.js 默认开启了一个安全保护，会保护应用的一系列安全，其中有一项是 CSRF，跨站请求伪造的安全保护，发送请求时要添加特殊的 token。这个内容我们在后面的安全部分会讲解，这里先暂时把这个配置关掉。配置在 config 文件夹的 config.default.ts 里，打开后在 middleware 后面添加 config，security 下面设置 CSRF 为一个 object，添加属性 enable 改成 false，就可以关闭这个选项。开启 TS 的好处就是什么都能联想出来。关闭后等服务器重启，重新发送请求，这时就返回了具体的一系列信息，并且把传送的 data（name Viking、hobby soccer）一模一样地反射了出来。

这节课我们学习了在 controller 中获取 request 各种信息的方法。有些同学对命令行不太熟悉，或者有系统兼容性问题不好使用 curl，有没有更简单的方法？下节课给大家介绍一款工具，对 HTTP 的管理和调试非常有用，有的同学在工作中可能已经经常用到，之后我会把它作为我们管理 HTTP 请求的主力工具，它就是 Postman。
