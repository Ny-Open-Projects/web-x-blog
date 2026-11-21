# 14-22-mongoDB 权限验证第二部分

这节课继续学 MongoDB 的授权。上节课在 admin 数据库里创建了最高权限的用户 root。MongoDB 可以基于单个数据库创建用户和权限，每个数据库都能有自己的管理员，非常方便。

以我们的应用为例，Docker 容器初始化一个新 MongoDB 实例时，希望按这样的最佳实践来走：

1. 先创建拥有整个 MongoDB 权限的管理员，也就是 admin 级别的 root 用户，roles 为 root。
2. 再创建业务数据库（比如 opsflow），然后为该库创建管理员（比如 xyz）。创建这个管理员要用 root 用户，即先以 root 登录授权验证，新管理员的 roles 应该是 readWrite，可以在库里进行任何读写。
3. 最后在代码中使用 xyz 的用户名密码连接数据库，完成操作。

现在 root 用户已经有了，先抛开 Docker，在本地模拟一遍这个过程。

## 为业务库创建管理员

```bash
mongo -u root -p 123456 --authenticationDatabase admin
```

登录后能看到所有 db。进入 opsflow 这个 db（`use opsflow`），继续用 `db.createUser` 创建用户：

```js
use opsflow
db.createUser({
  user: "viking",
  pwd: "123456",
  roles: [{ role: "readWrite", db: "opsflow" }]
})
```

user 叫 viking，pwd 测试用 123456。roles 是数组，元素也可以用 object 形式指定多项；对数据库管理来说用预设的 readWrite 就够了，它拥有所有的读和写权限。还有个参数 db，指定作用域是 opsflow。回车显示 successfully add user，用户添加完毕。在客户端软件里刷新 opsflow 数据库，点击 user，能看到 viking 创建成功。最好再把数据库重启一遍让它重新运作，注意本地测试也要像之前一样开启 `--auth` 身份验证。

## 在代码中连接

开发环境的 default.ts 默认不需要密码，这里本地数据库开启了 auth 模式，我们也出于学习和调试目的把连接配置补上。MongoDB 的连接除了 URL 参数，还有 options：user 填 viking，pass 填 123456。当然这些敏感信息不应该直接暴露在代码里，应该存到 .env 中，这里只做简单测试。

保存后启动应用，没有报任何错误。请求 api/templates，能拿到所有数据，说明权限验证开启成功，当前用的是 viking 这个用户。

## root 连不上？authenticationSource

再用 root 测试一下：root 有最大权限，操作 opsflow 自然没问题。把用户名密码换成 root 保存重新编译，却发现 root 连接不上了。这很神奇：难道 root 不是最大权限吗？

看代码就明白了：我们直接连的是 opsflow 数据库，但这个库里根本没有 root 这个 user，只创建了 viking。这时需要一个特殊参数 authenticationSource：它填一个数据库的名称，告诉 Mongo 引擎我们的用户来源是内置的 admin 数据库，也就是默认的用户管理数据库。告诉引擎用户信息来自 admin 之后，再试一次，连接成功了，刷新数据也能获取。

这个参数要特别注意：它说明用户来自 admin，而不是当前连接的数据库本身。

通过这两节课，我们学习了 Mongo 的用户权限验证系统。下节课希望在 Docker 启动时按这个最佳实践完成初始化步骤：创建对应的用户，把权限验证都加上。
