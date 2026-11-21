# 17-3-2-JSON server 自定义接口URL 和 返回数据结构

继续讲 JSON Server 的用法。上节课可以非常快地搭建一个支持标准 RESTful 请求的 mock 服务器，奥秘就在 `db.json` 文件中，它根据文件里的节点自动生成一系列路由。现在我添加了 `templates` 节点，自然就生成了对应的数据和路由。

但要让 mock server 和真实后端接口完全相同，还需要下一番功夫，首先是 URL。

## 从 module 方式开始

我们的 URL 带 `/api` 前缀，默认生成的是不带的，所以需要 URL 重写功能。官方文档有一章叫 module，提供了底层的实现，可以基于它做更丰富的构建。mock server 的代码我会放在单独的分支上（`feature/mock-server`），不会合并到 master，后面课程直接使用测试服务器测试，想看源码的可以看这个分支。

在根目录创建 `mock-server.js`，把文档里的基础代码拷过来。会报 ESLint 错误，因为项目里有 TS 规则，Quick Fix 选择 Disable for this line 即可。

可以看到 JSON Server 是基于 Express 封装的，由三部分组成：server（用 `jsonServer.create()` 创建）、router（路由模块）和 middleware（中间件模块）。用过 Express 的同学对这些概念应该很熟悉。直接 `server.use(middlewares)`、再 `use(router)`，然后 `listen` 启动，就能得到和原来一模一样的服务：

```bash
node mock-server.js
```

显示 JSON Server is running，访问 `localhost:3000/templates` 就能看到数据。

由于要频繁修改这个文件、频繁重启服务，每次修改后重打命令很麻烦。推荐一个命令行工具 nodemon（22.1k star），它做的事很简单：监视文件是否更新，更新了就重新运行命令，达到重启的效果。安装 `npm install --save-dev nodemon`，然后在 package.json 里加一条命令：

```json
"mock": "nodemon mock-server.js"
```

`npm run mock` 启动，templates 也能正常显示。

## 自定义 URL：rewriter

JSON Server 提供了写好的 rewriter 来做 URL 重写：

```js
server.use(jsonServer.rewriter({
  '/api/*': '/$1',
}))
```

参数是一个 object，key 是你想要的 URL，value 是原始 URL。这里希望所有请求前面加上 `/api` 前缀，value 用正则 `/$1`，匹配到的部分直接接到 `/api/` 后面，完成重写。服务器自动重启后，访问要加 `/api` 前缀才能拿到数据，URL 至少和真实接口一样了。想探索更多规则可以看文档的 rewrite examples，有各种参数重写的例子。

## 自定义返回结构：router.render

第二个需求是返回结果个性化。现在的结果是直接的数组，而真实 API 返回的是包裹过的数据：外层有 `errno` 和 `data`，data 里是 `list`，最后才是数据本身。mock server 要长得一模一样。

router 上有一个静态方法 `render`，两个参数是 req 和 res（请求和返回）。在里面就可以自定义返回的数据了，调用 `res.jsonp` 把 JSON 数据返回出去：

```js
router.render = (req, res) => {
  res.jsonp({
    errno: 0,
    data: {
      list: res.locals.data,
      count: res.locals.data.length,
    },
  })
}
```

原始数据在 `res.locals.data` 里；`count` 用它的 length 即可（是数组）。刷新后可以看到返回格式变成了 `errno: 0`、`data.list` 是数组、`count` 也在。非常方便。

如果有更多定制需求，不止这一种格式，还有各种丰富的格式，可以拿到 req（request），自然就能拿到一系列关于参数的 URL，根据 URL 判断输出不同的格式即可。

## 自定义不规则路由

最后一个需求：有些路由需要完全自定义，比如请求验证码这种不规则的路由。JSON Server 也支持，直接在 server 上定义，GET、POST 等方法都有：

```js
server.get('/echo', (req, res) => {
  res.jsonp({ test: '123' })
})
```

访问 `/echo`，test 123 出现了，自定义路由生效。不规则的自定义接口都可以这样添加到这里。

通过这节课，我们完成了 JSON Server 的三步自定义：URL 重写规则、返回数据结构、自定义接口。做到这三步，它就能和我们的接口类型高度相似了。
