# 后端接口开发—用户的查询接口开发

> **导语**：登录会签发 token，查询用户信息则是第一个「拿着 token 来要数据」的接口：后端先解密 token、确认没过期、取出用户 id，再查库返回资料。这一集把 token 解密封装成可注入的工具类，走通 `@Headers()` 取 token、Service 按 id 查库的全流程，并强调一个铁律——返回给前端的字段里绝不能带密码。

## 前置知识

- 已完成登录接口并了解 token 由 `JwtService.sign` 签发，可回顾《后端接口开发—用户的登录接口开发》。
- 会用 TypeORM 的 `findOne` 按条件查询，见过 `@Injectable()` 与 Module 的 `providers` 注册，可参考《如何理解Nestjs的提供者Providers》《Nest通过TypeORM链接Mysql数据库》。
- 知道 MD5 加密工具在注册、登录里的用法。

## 正文

### 接口目标与整体思路

接口是 `GET http://localhost:3000/user/find`。它和登录/注册最大的不同是：**必须带 token**。请求头里带上 token，后端解析无误、确认有权限，才返回对应的用户数据。流程拆成三段：

1. 从请求头取出 token；
2. 解密并校验（合法性、是否过期），取出用户 id；
3. 用 id 查库，脱敏后返回用户信息。

因此先要有一个「token 解密工具」，再把它注入 Controller 使用。

### 整理加密工具，新建解密工具

`utils` 目录里原本有一个基于 MD5 的加密工具，本节先把它的命名整理清楚（改名为语义更准确的 `SecretTool`，注入属性用小写 `secretTool`），所有引用处同步改掉，避免后面混淆。接着新建一个 `@Injectable()` 的解密工具类，通过构造函数注入 `JwtService`：

```ts
import { Injectable, BadRequestException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class JwtTool {
  constructor(private readonly jwtService: JwtService) {}

  decode(token: string): number {
    let decodeToken: any;
    try {
      decodeToken = this.jwtService.verify(token);
    } catch {
      throw new BadRequestException('Token 有误');
    }
    if (!decodeToken) {
      throw new BadRequestException('请先登录');
    }
    if (decodeToken.exp * 1000 <= Date.now()) {
      throw new BadRequestException('登录已过期，请重新登录');
    }
    return decodeToken.id;
  }
}
```

几个要点：

- `verify` 遇到非法 token 会抛错，必须用 `try/catch` 兜住，转成 `BadRequestException('Token 有误')`，否则会把原始错误直接抛给前端。
- 解密结果是个对象：除了签发时放进去的 `id`，还带 `iat`（签发时间）和 `exp`（过期时间）。取不到值时提示「请先登录」，比对 `exp` 与当前时间判断过期，过期提示「登录已过期，请重新登录」。
- 这里**只返回 id**，把「解密」和「查库」解耦；当然也可以直接在工具里查库返回用户，但拆开更利于复用（具体判断写法以 `代码（已8期）/9-1/lowcode/packages/server` 下源码为准）。

建好类后，别忘了在 `user.module.ts` 的 `providers` 里注册，否则 Controller 注入不到它。

### Controller：用 @Headers 取 token

新增一个 GET `find` 接口，用 `@Headers()` 拿到请求头，把 `authorization` 传给解密工具，再把得到的 id 交给 Service：

```ts
@Get('find')
find(@Headers() headers: Record<string, string>) {
  const id = this.jwtTool.decode(headers.authorization);
  return this.userService.find(id);
}
```

注意 `authorization` 的大小写要与前端实际传的保持一致。这一步把「鉴权」收敛成一行调用，Controller 只负责编排。

### Service：按 id 查库并脱敏

Service 里新增 `find`，接收 number 类型的 id，用 `findOne` 查一条记录，然后**手动挑选**要返回的字段：

```ts
async find(id: number) {
  const user = await this.userRepository.findOne({ where: { id } });
  return {
    id: user.id,
    username: user.username,
    headImage: user.headImage,
  };
}
```

这是本节最该记住的安全规范：**密码一定不能返回给前端**。直接 `return user` 会把 `password`（即便是加密后的）一起带出去，既有泄露风险也不符合接口规范。只返回 `id`、`username`、`headImage` 这类展示所需字段——访问课程管理页面时，前端正是用 `headImage` 渲染用户头像。

### 联调验证

在接口调试工具里：先调登录接口拿到 token，复制进 `find` 接口的请求头，再发起请求，就能拿到该用户的资料（对应数据库里的那条记录）。可以顺手验证三种异常：不带 token、带过期 token、带乱写的 token，分别应得到「请先登录」「登录已过期，请重新登录」「Token 有误」。工程启动脚本见 `代码（已8期）/9-1/lowcode/package.json` 的 `run:server`。

## 小结

- 查询接口要求请求头带 token，后端解密校验通过后才返回数据。
- 解密封装成 `@Injectable()` 工具类并注册到 Module 的 `providers`，Controller 直接注入复用。
- `verify` 要用 try/catch 兜住非法 token；解密结果含 `id`、`iat`、`exp`，需判断过期。
- `@Headers()` 取 `authorization`，Service 用 `findOne({ where: { id } })` 查库。
- 返回字段必须脱敏，密码绝不外泄，只给页面展示需要的 id / username / headImage。

## 下一步

建议接着看《掌握Nestjs中间件的使用》——「每个接口都要校验 token」这类横切逻辑，后面会抽成中间件或装饰器统一处理，不必在每个 Controller 里重复写。也可以看《后端接口开发—课程的修改接口开发》，把这套「取参—校验—查库—返回」的分层再练一遍。
