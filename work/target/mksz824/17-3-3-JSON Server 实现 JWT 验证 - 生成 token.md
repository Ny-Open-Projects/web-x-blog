# 17-3-3-JSON Server 实现 JWT 验证 - 生成 token

上节课完成了修改接口 URL、自定义返回结构、添加完全自定义的接口。还剩一个工作没做：接口的权限。我们需要在特定接口用正确的数据获取权限，比如 `loginByPhoneNumber` 用来获取 token；想访问被保护的接口（比如获取用户信息），则要带着特殊的 authorization header 和数据。

所以现在要在 mock server 中模拟和真实实现一样的 token 生成过程。token 与传统的 cookie、session 实现方法的区别，上一阶段已经详细讲过，这里只简单说一点：基于 token 的身份验证是无状态的，服务器不需要记录哪些用户已登录、哪些 token 已被处理；每个请求都带上 token，服务器利用它确认请求的真实性。

## JWT 的结构

我们采用的方案是 JSON Web Token，它是用得最多的 token 实现方式：通过特定的加密算法，把用户登录后的一些信息（用户 ID、过期时间等）储存在一个加密过的字符串里，这个字符串就是最终生成的 token。以后用户与服务器通讯都要发送它，服务器完全靠它认定用户身份，服务器因此变成无状态的，容易扩展。

JWT 官网首页就有一个解码器，可以揭开 token 的秘密。token 是一串很长的字符串，中间用点分割成三个部分：

1. **header**（红色部分）：解码后是一个 JSON 对象，描述 JWT 的元数据，使用了什么 algorithm、什么 type；
2. **payload**（最重要）：也是一个 JSON 对象，存放实际需要传递的数据，比如我们的 `phone number` 和 `verify code` 就存在这里；
3. **verify signature**：需要指定一个密钥，只有服务器知道，不能透露给用户。

这三项组成了完整的 token。

## 整体流程

**生成 token**：在特定路由（比如 `POST /login`）中携带加密信息（用户名和密码、邮箱或密码等），验证这些信息匹配后，用 `jwt.sign` 这个现成方法根据 payload 生成 token 并返回，用户通过这个请求拿到 token。

**验证 token**：访问被保护的路由时，在 header 中带上 token；服务器从 header 中取得 token，用 JWT 提供的 `verify` 方法验证。验证通过（passed）就继续返回成功的数据；解析出问题，说明传的 token 是假的或根本没有 token，直接返回没有权限的信息。

这节课完成第一步：生成 token。

## 编码

安装模块：

```bash
npm install jsonwebtoken --save
```

它就是刚才说的提供 token 解决方案的库。安装完把 server 跑起来，然后写代码。首先引入包：

```js
const jwt = require('jsonwebtoken')
```

做一些准备工作，创建生成 token 的函数：

```js
function createToken(payload) {
  return jwt.sign(payload, SECRET_KEY, { expiresIn: '1h' })
}
```

`jwt.sign` 有三个参数：第一个是 payload，要加密的数据；第二个是 secret key，写定一个常量即可；第三个是 options，里面配置过期时间 `expiresIn`，这里弄一个假的过期时间。

有了函数，就可以创建需要 generate token 的路由。我们使用 `loginByPhoneNumber`，所以要完全模拟对应的接口，删掉原来的：

```js
server.post('/users/loginByPhoneNumber', (req, res) => { ... })
```

作为 mock server，只是简单模拟整个过程，不会验证任何数据的可靠性。参数是 body 里传来的 `phoneNumber` 和 `verifyCode`。要从 body 中拿数据，需要一个 Express 的 middleware，body-parser，安装 JSON Server 时它已经默认安装了，不需要再装。放到最上面：

```js
server.use(bodyParser.json())
```

这样传过来的 body 数据会被解析成 JSON 格式，供我们直接取用。

拿到两个参数后直接生成 token（模拟过程：传上来就认为有效）：

```js
const accessToken = createToken({ phoneNumber, verifyCode })
```

最后设置状态码并返回，格式和真实接口保持一致，外面裹一层 data，data 里是 token：

```js
res.status(200).json({
  errno: 0,
  data: { token: accessToken },
})
```

## 验证

现在用 Postman 试一下：访问 `localhost:3000`，body 传 phoneNumber 和 verifyCode（我是乱写的，什么都能通过），点击 Send，成功生成了 token 值，这就是 JSON Web Token 帮我们生成的。

这节课的任务完成了：了解了 JWT 的运作原理，完成了验证的第一步，生成 token 的整个过程。下节课再做路由保护（验证）的过程。
